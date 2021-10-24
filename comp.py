import cv2
import dropbox
import time
import random

startTime = time.time()
def take_snapshot():
    num = random.randint(0,100)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(num) + ".png"
        cv2.imwrite(img_name,frame)
        
        startTime = time.time()
        result = False
    return(img_name)
    print("Snapshot Taken")
    

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    accessToken = 'sl.A6cr0p1l1kcgIgzMj5U68tJrBHxyQKBMRzHl-h2ZXabYmrgj9jXqj3AIiVg83nzRtMmDn-aSORtep0egepAACjNfJbvO-QewXmiJSpk2VMQ50KvPSiPMPTITE80X0VZyTMPWLE8'
    file = img_name
    fileFrom = file
    fileTo =  "/testFolder/" + (img_name)
    dbx = dropbox.Dropbox(accessToken)

    with open(fileFrom, 'rb') as f:

        dbx.files_upload(f.read(), fileTo,mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while (True):
        if ((time.time() - startTime)>= 10):
            name = take_snapshot()
            uploadFile(name)

main()



  