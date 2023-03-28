import cv2
face_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.9/dist-packages/ cv2/data/haarcascade_frontalface default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.9/dist-packages/cv2/data/haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('./haarcascade_mcs_nose.xml')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read( )
    frame = cv2.resize(frame,None,fx = 0.5, fy = 0.5, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor( frame,cv2.COLOR_BGR2GRAY)
    face_rects = face_cascade.detectMultiScale(gray,1.1, minNeighbors = 5)
    for(x,y,w,h) in face_rects:
        cv2.rectangle(frame,(x,y),(x + w, y+ h),(255,0,0),2)#用蓝色框标记人脸
        roi_gray = gray [y:y+ h,x:x+w]#提取人脸区域
        roi_color = frame[y:y+ h, x:x + w]# 视频帧中的人脸区域图像
    eye_rects = eye_cascade. detectMultiScale(roi_gray) #在人脸区城检测眼睛
    nose_rects = nose_cascade.detectMultiscale(roi_gray,1.3,5)#在人脸区城检测鼻子
    for(x_eye,y_eye, w_eye,h_eye) in eye_rects:
        center = (int(x_eye + 0.5 * w_eye), int(y_eye + 0.5* h_eye))
        radius = int(0.3 *(w_eye + h_eye))
        cv2.circle(roi_color,center,radius,(0,255,0),2)
    for(x_nose,y_nose,w_nose,h_nose) in nose_rects:
        cv2.rectangle(roi_color,(x_nose,y_nose), (x_nose + w_nose,y_nose + h_nose),(0,0,255),2)
        break
    cv2.imshow('Eye and nose Detector', frame)
    if cv2.waitKey(1) & 0xff == ord("g"):
            break
cap.release()
cap.destroyAliwindows()

