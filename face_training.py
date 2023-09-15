import cv2
import numpy as np
import os
path = './dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()

def ImageandLabel(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples =[]
    ids = []
    for imagePath in imagePaths:
        img = cv2.imread( imagePath, cv2.IMREAD_GRAYSCALE)
        face_id = int(os.path.split(imagePath)[ -1].split(".")[1])
        faceSamples.append (img)
        ids.append(face_id)
    return faceSamples, ids

print("训练人脸样本...")
faces,ids = ImageandLabel(path)
recognizer.train(faces,np.array (ids))
#训练样本集
recognizer.write( 'trainer/trainer.yml')
#保存模型
print("样本训练完毕")


