# BSF - Blur selected people in a video
Bluer Selected Face's - Web App

Recognize face's and select which face you want to blur in a video file

# Dependencies
we used python version 3.7.0<br>
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32<br>
https://www.python.org/downloads/release/python-370/<br>

for python install those libraries:<br>

<code>pip install face-recognition</code><br>
<code>pip install numpy</code><br>
<code>pip install opencv-python</code><br>
<code>pip install pytest-shutil</code><br>

<br>
use nodejs version 14.15.1<br>
https://nodejs.org/en/blog/release/v14.15.1/<br>


# Operation:

  Starting the backend:
    navigate to BSF folder using "cd" command then run the following command:<br>
      <code>node server.js</code>
  
  next step navigate to http://localhost:8080/ in your broswer, you will prompt to the main page<br>
  upload MP4 video file and click "upload" button<br>
    ![image](https://user-images.githubusercontent.com/48179479/184368548-c79f9339-6cdd-4519-b5b0-8787a68c5e34.png)


  next click Run to start the python script to detect face's inside the video <br>
  ![image](https://user-images.githubusercontent.com/48179479/184368791-cc92dab6-c702-454f-9115-0579ddaef56c.png)


frame's reading will run in interval of 15 frames, each frame will recognize face's using Face_Recognition libray, and .jpg file of the face's will be saved in the "People"       folder next to the script
  ![image](https://user-images.githubusercontent.com/48179479/184368948-4f15617c-72e9-4f02-b849-47b9179609f0.png)

![2022-02-27_19-08-55_2](https://user-images.githubusercontent.com/48179479/155892447-d5646dc6-0dca-40fc-9c59-5c275f70c1bf.gif)

  ![image](https://user-images.githubusercontent.com/48179479/155890628-8699e230-56e3-471b-a6c4-0dc7c63a8074.png)

 image will appear with the recognized face's from the video, select which face's you would like to be blured sepreated with spaces
  
    Example1: "Please Select person numbers you would like to blur: 0"
    
    Example2: "Please Select person numbers you would like to blur: 0 1 2"
    
 
 ![image](https://user-images.githubusercontent.com/48179479/184372720-554f04d4-38a4-4a55-bacc-d58227614155.png)

 


  5.the BlurFaces method will run blur the selected people face's and will add the link to download the result at the end
  
   ![image](https://user-images.githubusercontent.com/48179479/155890785-aeca2b63-6150-43f3-a833-2aaab80aff6b.png)
      
    ![image](https://user-images.githubusercontent.com/48179479/184374790-7747d2c5-4921-4134-90c5-a2217e6d5ae9.png)
  
      
**Final Results** (Person 1 selected to be blured):

![output_1_3](https://user-images.githubusercontent.com/48179479/155891282-12b74f7d-9787-46d9-acf4-30eabf70fe18.gif)

controling the **blur amount** using this line 65 in "BlurSelectedPeople.py" change the X to the amount

    65: frame[top-25:bottom+25, left-25:right+25] = cv2.blur(frame[top-25:bottom+25, left-25:right+25], (X, X))



