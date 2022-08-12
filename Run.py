
from DetectingFaces import DetectingFaces
from ClassifiedPersons import ClassifiedPersons
from BlurSelectedFaces import BlurSelectedFaces
import os, shutil
from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt
import random
import sys
import time
def open_file(file_path):
    while not os.path.exists(file_path):
        time.sleep(1)

    if os.path.isfile(file_path):
        return open(file_path).read()
    else:
        raise ValueError("%s isn't a file!" % file_path)
if __name__ == '__main__':
    # first we recieve path to video and check it, then we find faces in the video and classify them to directories.
    while True:
        fileselect = sys.argv[1]
        pathcheck = Path(fileselect)
        if not pathcheck.exists():
            print("File Doesn't Exist try upload again!")
            sys.stdout.flush()
            exit()        
        else:
            break
    choice_dir = os.getcwd()+"/choice"
    if (os.path.isdir(choice_dir) == 1):
        shutil.rmtree('choice', ignore_errors=True)
    else:
        os.mkdir(choice_dir)

    df = DetectingFaces(fileselect)
    df.detect()
    cp = ClassifiedPersons()
    cp.mergeSimilars()
    # next we show the user the faces in the video with numbers to identify each one.
    pepole_counter = -1
    for dirs in os.walk("People"):
        pepole_counter += 1
    dim = int(np.ceil(np.sqrt(pepole_counter)))
    for i in range(pepole_counter):
        filename = "People/{0}/".format(i) + random.choice(os.listdir("People/{0}".format(i)))
        plt.subplot(dim, dim, i + 1)
        img1 = plt.imread(filename)
        plt.axis('off')
        plt.imshow(img1)
        plt.title("Person " + str(i))
    #plt.show()
    #

    # user enter the numbers for the person's he would like to be blured and it will be blured using the BlurFaces method
    # format for input is numbers with whitespace between them

    plt.savefig('public/images/out.png')
    selection = open_file("./choice/choice.txt")

    people_arr = list(map(int, selection.split()))
    bsf = BlurSelectedFaces(people_arr,fileselect)
    bsf.BlurFaces()
    shutil.rmtree('choice', ignore_errors=True)
