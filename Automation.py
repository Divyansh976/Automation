import cv2
import dropbox
import time
import random
import shutil
import os

from dropbox.files import WriteMode

startTime = time.time()

def takeSnapshot():
    number = random.randint(1, 100)
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = VideoCaptureObject.read()
        imageName = "div_img" + str(number) + ".png"
        cv2.imwrite(imageName, frame)
        startTime = time.time()
        result = False
    return imageName
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token = "tWLldhCfrAkAAAAAAAAAAQyDNWW-mvQkgNYFauitfYe-pAm9tVdzgBPL6zqcfCSC"
    file = imageName
    file_from = file
    file_to = "/newFolder/" + (imageName)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time() - startTime)>=5):
            name = takeSnapshot()
            upload_file(name)

main()