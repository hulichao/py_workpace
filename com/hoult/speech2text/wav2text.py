#! /usr/bin/env python
# -*- coding:utf-8 -*-


from ibm_watson import SpeechToTextV1
from ibm_watson import ApiException

username = "jsu_hlc@163.com"
password = "Hu123456."
url = "https://gateway-lon.watsonplatform.net/speech-to-text/api"

speech_to_text = SpeechToTextV1(
    username = username,
    password = password,
    url= url
)


try:
    1# Invoke a Speech to Text method
except ApiException as ex:
    print ("Method failed with status code " + str(ex.code) + ": " + ex.message)