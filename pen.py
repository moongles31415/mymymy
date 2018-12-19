import cv2
import numpy as np 
import matplotlib.pyplot as plt
import pytesseract 
import pyttsx3
from PIL import Image
#需要的库

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 32:
      cv2.imwrite("kk.png",frame)
#摄像头截取图片

      kkk=Image.open("kk.png")
      kkk=kkk.convert("L")
      kkk.save("kkk.png")
#转换为灰度图片
      
      image = Image.open('kkk.png')
      penWords=pytesseract.image_to_string((image),lang='chi_sim')
      print(penWords)
#转换为文字信息
      
      engine = pyttsx3.init()
      engine.say(penWords)
      engine.runAndWait()
#文字转语音        

    if cv2.waitKey(1) == 13:break
        
cap.release() 
cv2.destroyAllWindows()

#关闭程序释放窗口
