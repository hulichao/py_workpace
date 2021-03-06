#! /usr/bin/env python
#coding:utf-8
## from:http://www.iwangsen.com/2018/09/06/IBM-speech-to-text/

# pip install SpeechRecognition

import os
import speech_recognition as sr
import time
import datetime

starttime = datetime.datetime.now()
i = 1
for name in os.listdir(r'../input'):
    print("%d %s 开始转换" % (i, name))

    # 音频分块识别
    r = sr.Recognizer()
    try:
        with sr.WavFile(r'../input/%s' % name) as source:
            audio = r.record(source)
            IBM_USERNAME = 'jsu_hlc@163.com'
            IBM_PASSWORD = 'Hu123456.'
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='zh-CN')
            print(text)
            open(r'./' % name, 'a+').write(text)
            time.sleep(5)
            temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('%s %d %s 已完成' % (temptime, i, name))

    except Exception as e:
        print(e)
        temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s %d %s 未完成' % (temptime, i, name))
        continue
    i += 1
endtime = datetime.datetime.now()
last = endtime - starttime
print('总共花费时间：%s' % last)