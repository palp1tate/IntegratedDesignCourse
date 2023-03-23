import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
# 调用摄像头摄像头
cap = cv2.VideoCapture(0)

while(True):
    # 获取摄像头拍摄到的画面
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    img = frame
    for (x,y,w,h) in faces:
        # 画出人脸框，蓝色，画笔宽度微
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
        face_area = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_area)
        # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
        for (ex,ey,ew,eh) in eyes:
            #画出人眼框，绿色，画笔宽度为1
            cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)

    # 实时展示效果画面
    cv2.imshow('frame2',img)
    # 每5毫秒监听一次键盘动作
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 最后，关闭所有窗口
cap.release()
cv2.destroyAllWindows()

import cv2
import dlib

# 加载面部检测器
detector = dlib.get_frontal_face_detector()

# 加载图像
img = cv2.imread("example.jpg")

# 将图像转换为灰度图像，以便进行面部检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 在图像中查找所有的面部，并将它们存储在faces列表中
faces = detector(gray)

# 在图像中绘制面部框
for face in faces:
    x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

# 显示结果
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

