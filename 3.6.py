# -*- coding: utf-8 -*-
"""3.6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KOuIqmB_OmfdT2IzXxiB1OJs5mBjp36v
"""

n=0
while n%2==0:
  n=eval(input("請輸入奇數行數="))
n=int((n-1)/2)+1
for i in range(1,n+1):
  i=1+2*(i-1)
  ii=int((2*n-i)/2)
  if ii<0:
    ii=-ii
  else :
    ii=ii
  print(" "*ii,"*"*i)
for t in range(1,n+1):
  iii=i-2*t
  print(" "*t,'*'*iii)

#or

n=5
n=int((n-1)/2)+1
for i in range(1,n+1):
  i=1+2*(i-1)
  ii=int((2*n-i)/2)
  if ii<0:
    ii=-ii
  else :
    ii=ii
  print(" "*ii,"*"*i)
for t in range(1,n+1):
  iii=i-2*t
  print(" "*t,'*'*iii)

