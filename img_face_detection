import cv2
def detect(filename) :
    #加载XML文件生成级联分类器
    face_detector = cv2.CascadeClassifier( '/usr/local/1ib/python3.9/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)#转化成灰度图
    face_rects = face_detector.detectMultiScale(gray, scaleFactor = 1.1,minNeighbors=3)#用矩形框框出每张人脸
    for(x,y,w, h) in face_rects:
        cv2.rectangle(img,(x,y),(x + w,y+ h),(255,0,0),2)
        cv2.imshow( 'Face Detector' , img)
        k = cv2.waitKey(0)
        if k == 27:#按Esc键退出
            cv2.destroyAllwindows()
        elif k == ord( 's ') :#按S键保存图像并退出
            cv2.imwrite('face.jpg', img)
            cv2.destroyAllwindows()
detect('HEAT.jpg ')

