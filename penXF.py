import cv2
import numpy as np 
import matplotlib.pyplot as plt
import time
#import pygame
import base64
import json
import hashlib
import urllib.request
import urllib.parse
from aip import AipOcr
from PIL import Image


#定义常量
APP_ID = '15155701'
API_KEY = 'tpiAH59yHC2SF736GMdhB19D'
SECRET_KEY = 'txZOB0dmY5GePp8oFNtoRKATaeaLdHCE'

#摄像头截取图片
cap = cv2.VideoCapture(0)
while True:
   ret,frame = cap.read()    
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) == 32:
      cv2.imwrite("kk.png",frame)
      
#初始化AipFace对象
      aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

#读取图片
      filePath = "kkk.jpg"
      def get_file_content(filePath):
         with open(filePath, 'rb') as fp:
            return fp.read()

#图片处理转为文字信息
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

#转为语音文件
      # API请求地址、API KEY、APP ID等参数，提前填好备用
      api_url = "http://api.xfyun.cn/v1/service/v1/tts"
      API_KEY = "e14d01b774bc5c64f0209a4c21ae838e"
      APP_ID = "5c24eb24"
      OUTPUT_FILE = "/home/moongles/Git/auido_k.mp3"    # 输出音频的保存路径，请根据自己的情况替换

# 构造输出音频配置参数
      Param = {
         "auf": "audio/L16;rate=16000",    #音频采样率
         "aue": "lame",    #音频编码，raw(生成wav)或lame(生成mp3)
         "voice_name": "xiaoyan",
         "speed": "50",    #语速[0,100]
         "volume": "77",    #音量[0,100]
         "pitch": "50",    #音高[0,100]
         "engine_type": "aisound"    #引擎类型。aisound（普通效果），intp65（中文），intp65_en（英文）
      }
# 配置参数编码为base64字符串，过程：字典→明文字符串→utf8编码→base64(bytes)→base64字符串
      Param_str = json.dumps(Param)    #得到明文字符串
      Param_utf8 = Param_str.encode('utf8')    #得到utf8编码(bytes类型)
      Param_b64 = base64.b64encode(Param_utf8)    #得到base64编码(bytes类型)
      Param_b64str = Param_b64.decode('utf8')    #得到base64字符串

# 构造HTTP请求的头部
      time_now = str(int(time.time()))
      checksum = (API_KEY + time_now + Param_b64str).encode('utf8')
      checksum_md5 = hashlib.md5(checksum).hexdigest()
      header = {
         "X-Appid": APP_ID,
         "X-CurTime": time_now,
         "X-Param": Param_b64str,
         "X-CheckSum": checksum_md5
      }

# 构造HTTP请求Body
      body = {
         "text": penWords
      }
      body_urlencode = urllib.parse.urlencode(body)
      body_utf8 = body_urlencode.encode('utf8')

# 发送HTTP POST请求
      req = urllib.request.Request(api_url, data=body_utf8, headers=header)
      response = urllib.request.urlopen(req)

# 读取结果
      response_head = response.headers['Content-Type']
      if(response_head == "audio/mpeg"):
         out_file = open(OUTPUT_FILE, 'wb')
         data = response.read() # a 'bytes' object
         out_file.write(data)
         out_file.close()
         print('输出文件: ' + OUTPUT_FILE)
      else:
         print(response.read().decode('utf8'))

#调用pygame进行mp3播放
#      file=r'/home/moongles/Git/auido_k.mp3'
#      pygame.mixer.init()
#      track = pygame.mixer.music.load(file)
#      pygame.mixer.music.play()


   if cv2.waitKey(1) == 13:break
   
#关闭程序释放窗口test
cap.release() 
cv2.destroyAllWindows()


