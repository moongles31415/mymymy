import cv2
import numpy as np 
import matplotlib.pyplot as plt
import time
import pygame
from aip import AipSpeech
from aip import AipOcr
from PIL import Image

# 定义常量
APP_ID_WZ = '15155701'
API_KEY_WZ = 'tpiAH59yHC2SF736GMdhB19D'
SECRET_KEY_WZ = 'txZOB0dmY5GePp8oFNtoRKATaeaLdHCE'
APP_ID_YY = '15289981'
API_KEY_YY = 'Lpiv5SsGxA90GnWwM7cRDa5C'
SECRET_KEY_YY = '14SvBenB2sGm6XqyTcFZKK1j9DiFdPpn'

# 摄像头截取图片
cap = cv2.VideoCapture(0)
while True:
   ret,frame = cap.read()    
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) == 32:
      cv2.imwrite("kk.png",frame)
      
# 初始化AipFace对象
      aipOcr = AipOcr(APP_ID_WZ, API_KEY_WZ, SECRET_KEY_WZ)
      aipSpeech = AipSpeech(APP_ID_YY, API_KEY_YY, SECRET_KEY_YY)
      
# 读取图片
      filePath = "kk.png"
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
      audioMp3 = aipSpeech.synthesis(penWords, 'zh', 1, {
         'vol': 9,'per':1,'spd':6,'pit':5
            })

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
      if not isinstance(audioMp3, dict):
         with open('auido.mp3', 'wb') as f:
            f.write(audioMp3)

# mp3play
      file=r'/home/moongles/Git/auido.mp3'
      pygame.mixer.init()
      track = pygame.mixer.music.load(file)
      pygame.mixer.music.play()

   if cv2.waitKey(1) == 13:break
        
# 关闭程序释放窗口test
cap.release() 
cv2.destroyAllWindows()


