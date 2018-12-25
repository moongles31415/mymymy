import cv2
import numpy as np 
import matplotlib.pyplot as plt
import pytesseract 
import time
import pygame
from PIL import Image
from aip import AipSpeech
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
      
      image = Image.open('/home/moongles/Downloads/kkk.jpg')
      penWords=pytesseract.image_to_string((image),lang='chi_sim')
      penWords=penWords.replace('\n','')
      print(penWords)
#转换为文字信息
      APP_ID = '15130446'
      API_KEY = '05xORmBbw7s0pm5TP2PtPvtB'
      SECRET_KEY = 'v89XrGYZOGMIxs3t1VTBVgjCglBW6Y2f'
      client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
      result  = client.synthesis(penWords, 'zh', 1, {
         'vol': 9,'per':1,'spd':7,'pit':5
            })

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
      if not isinstance(result, dict):
         with open('auido.mp3', 'wb') as f:
            f.write(result)
#调用百度ai进行语音合成
      file=r'/usr/git/mymymy/auido.mp3'
      pygame.mixer.init()
      track = pygame.mixer.music.load(file)
      pygame.mixer.music.play()
#mp3 play        

    if cv2.waitKey(1) == 13:break
        
cap.release() 
cv2.destroyAllWindows()

#关闭程序释放窗口test
