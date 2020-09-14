# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:08:57 2020

@author: Dogukan
"""

from gtts import gTTS
import PyPDF2

pdfFileObj = open('Davenport - 2014 - Big Data at Work - Chapter 2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
text = ""
for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text += pageObj.extractText()

file = gTTS(text=text, lang='en')
file.save("tts.mp3")