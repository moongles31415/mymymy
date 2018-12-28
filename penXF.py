import cv2
import numpy as np 
import matplotlib.pyplot as plt
import time
import pygame
from aip import AipSpeech
from aip import AipOcr
from PIL import Image
#需要的库

# 定义常量
APP_ID = '11352343'
API_KEY = 'Nd5Z1NkGoLDvHwBnD2bFLpCE'
SECRET_KEY = 'A9FsnnPj1Ys2Gof70SNgYo23hKOIK8Os'
#摄像头截取图片
cap = cv2.VideoCapture(0)
while True:
   ret,frame = cap.read()    
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) == 32:
      cv2.imwrite("kk.png",frame)
# 初始化AipFace对象
      aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
      aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取图片
      filePath = "kkk.jpg"
      def get_file_content(filePath):
         with open(filePath, 'rb') as fp:
            return fp.read()
# 图片处理转为文字信息
      options={}
      options["detect_direction"] = "true"    #检测朝向
      options["detect_language"] = "true"     #检测语言      
      result= aipOcr.webImage(get_file_content(filePath),options)
      penWords=result['words_result']
      a = []
      for i in range(len(penWords)):
         a.append(penWords[i]['words'])
      penWords = ''.join(a)
      print(penWords)
# 转为语音文件
      audioMp3  = aipSpeech.synthesis(penWords, 'zh', 1, {
         'vol': 9,'per':1,'spd':6,'pit':5
            })

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
      if not isinstance(audioMp3, dict):
         with open('/home/moongles/Git/auido_k.mp3', 'wb') as f:
            f.write(result)
#调用百度ai进行语音合成
      file=r'/home/moongles/Git/auido_k.mp3'
      pygame.mixer.init()
      track = pygame.mixer.music.load(file)
      pygame.mixer.music.play()
#mp3 play        

   if cv2.waitKey(1) == 13:break
        
cap.release() 
cv2.destroyAllWindows()

#关闭程序释放窗口test
