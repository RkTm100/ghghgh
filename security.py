import cv2

import dropbox

import time

import random
start_time=time.time()

def take_snapshot():
    numbers=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result= True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img" + str(numbers) + ".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapshots taken")
    videoCaptureObject.release()


def upload_file(img_name):
    access_token="jep7VWggKN0AAAAAAAAAAXtff0mTkitmjRuqGC6lnw2s7Gr0DrZrIHXoaSyGZ9Po"
    file=img_name
    file_from=file
    file_to="/newfolder1" + (img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.writeMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()