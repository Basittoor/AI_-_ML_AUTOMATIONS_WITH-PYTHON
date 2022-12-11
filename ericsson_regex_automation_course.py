# -*- coding: utf-8 -*-
"""Ericsson_REGEX_AUTOMATION COURSE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pxwTGXf4AibHGx4Dxsfw7vufdvG8FFRj
"""

import re

mobilenumberex = re.compile(r'\d\d\d\d-\d\d\d\d\d\d\d')

m = mobilenumberex.search('0332-5319973')
m = mobilenumberex.search('0340-3771177')

print(m.group())

TR = re.compile(r'.ap')
TR.findall('rap tap cat mat hat jazz pap uap tap')



"""**Task Scheduler By Using Python**"""

import sched,time
myscheduler = sched.scheduler(time.time,time.sleep)
def fun1(): 
  print ('From Scheduler', time.time())

def print_sch_time(): 
  print(time.time())
  myscheduler.enter(3,4,fun1,())
  myscheduler.enter(5,2,fun1,())
  myscheduler.enter(2,3,fun1,())
  myscheduler.enter(7,1,fun1,())
  myscheduler.enter(3,5,fun1,())
  myscheduler.run()
  print(time.time())

print_sch_time()



"""**Manipulate images by Using Python**

"""

from PIL import Image
from google.colab import files
uploaded = files.upload()
uploaded.show()

# Imports PIL module 
from PIL import Image
  
# open method used to open different extension image file
im = Image.open(r"/content/oak-tree-7507678.jpg") 
  
# This method will show image in any image viewer 
im.show()

im.size

im.format

newImage = Image.new('RGBA',(200,200),'red')

newImage.save('newimage1.png')

im.rotate(180).save('newimage2.png')

im.rotate(90).save('newimage3.png')

im.transpose(Image.FLIP_TOP_BOTTOM).save('indextrans.png')

