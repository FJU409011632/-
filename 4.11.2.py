# -*- coding: utf-8 -*-
"""4.11.2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Iqh4JF_cLrkVuSE2A8Rnr-NEz8qRTZma
"""

def is_odd(x):
    if x%2==1:
        return True
    else:
        return False
x=eval(input("x="))
z=is_odd(x)
print(z)

#講義說"如果 x 是奇數則回傳 Ture "，因此有以下：
def is_odd(x):
    if x%2==1:
        return "Ture"
    else:
        return False
x=eval(input("x="))
z=is_odd(x)
print(z)
