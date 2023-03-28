import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
face_detector = cv2.CascadeClassifier('/usr/1ocal/1ib/python3.9/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
#加载分类器
face_id = input('输入人脸样本采集对象的序号:')
print("请对准摄像头,采集过程中可以改变脸部角度和表情")
count = 0
#人脸样本数
while cap.is0pened( ):
    ret,frame = cap.read( )
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.05,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x, y),(x + w,y+ h),(255,255,255),2)
        count += 1
        roi = cv2.resize(gray[y:y + h,x:x + w],(92,112))#调整到112 x 92#将检测到的人脸区域保存为图片,例如person.1.1表示第一个人的第一张人脸
        cv2.imwrite("./dataset/person." + str(face_id) + '.' + str(count)+ ".jpg", roi)
        cv2.imshow( ' image ' , frame)
    k = cv2.waitKey (100)&0xff
    if k==27:
        break
    elif count >= 20:
        break
cap.release()
cv2.destroyAllwindows()

