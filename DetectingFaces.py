from pickle import TRUE
import cv2 as cv2
import face_recognition
import sys
# import warnings
# warnings.filterwarnings('ignore')
import os, shutil


class DetectingFaces:
    fvs = None
    videofile = None

    def __init__(self, vf):
        self.videofile = vf

    def detect(self):
        """
        :param videofile: mp4 video file
        reading frame's from the video file and recognize faces in them, creating a jpg image file for
        each face in the people folder.
        using face_recognition library as our face detection model,using builtin methods
        we used interval of 15 frames for better time complexity(skipping frames).
        """

        fvs = cv2.VideoCapture(self.videofile)
        parent_dir = os.getcwd()
        people_dir = parent_dir + "/People"
        if (os.path.isdir(people_dir) == 1):
            shutil.rmtree('People', ignore_errors=True)
        else:
            os.mkdir(people_dir)
        faces_count = 0
        framecounter = 40
        while fvs.isOpened():
            fvs.set(cv2.CAP_PROP_POS_FRAMES, framecounter)
            ret, frame = fvs.read()
            if not ret:
                break
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                cv2.imwrite(str(people_dir) + '/' + str(faces_count) + ".jpg",
                            frame[top - 25:bottom + 25, left - 25:right + 25])
                faces_count += 1
            print(" [INFO] Processing frame", framecounter)
            sys.stdout.flush()
            framecounter += 15
        print("\n [INFO] Finish detecting faces")
        sys.stdout.flush()
        fvs.release()
        cv2.destroyAllWindows()
        return None
