# -*- coding: utf-8 -*-
"""3.3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-NEwTqnITSyqIMflQoCafhiwvpuKt8gE
"""

u=[]
d=[]
t=0
while t!=-1:
  t=eval(input("請輸入學生成績(輸入-1表則結算)="))
  if t>=60:
    u.append(t)
  elif t==-1:
    t=t
  else:
    d.append(t)
nu=len(u)
nd=len(d)
na=nu+nd
ae=(sum(u)+sum(d))/na
print("全班人數=",na,"及格人數=",nu,"不及格人數=",nd,"全班平均值",ae)