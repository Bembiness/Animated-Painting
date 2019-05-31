#credits-https://www.youtube.com/watch?v=4fHL6BpJrC4

import time
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

A = 7
B = 11
C = 13
D = 15

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(10, GPIO.IN) 


"""
      1  2  3  4  5  6  7  8
      
Pin1  x  x                 x
Pin2     x  x  x
Pin3           x  x  x
Pin4                 x  x  x

"""

def GPIO_SETUP(a,b,c,d):
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)
    GPIO.output(D, d)
    time.sleep(0.001)

def RIGHT_TURN(deg):

    half_circle = 360.0
    degree = half_circle/360*deg
    GPIO_SETUP(0,0,0,0)

    while degree > 0:
        GPIO_SETUP(1,0,0,0)
        GPIO_SETUP(1,1,0,0)
        GPIO_SETUP(0,1,0,0)
        GPIO_SETUP(0,1,1,0)
        GPIO_SETUP(0,0,1,0)
        GPIO_SETUP(0,0,1,1)
        GPIO_SETUP(0,0,0,1)
        GPIO_SETUP(1,0,0,1)
        degree -= 1

def LEFT_TURN(deg):

    half_circle = 360.0
    degree = half_circle/360*deg
    GPIO_SETUP(0,0,0,0)

    while degree > 0:
        GPIO_SETUP(1,0,0,1)
        GPIO_SETUP(0,0,0,1)
        GPIO_SETUP(0,0,1,1)
        GPIO_SETUP(0,0,1,0)
        GPIO_SETUP(0,1,1,0)
        GPIO_SETUP(0,1,0,0)
        GPIO_SETUP(1,1,0,0)
        GPIO_SETUP(1,0,0,0)
        degree -= 1

#MAIN #########################
n=1
while n>0:
    RIGHT_TURN(100)
    LEFT_TURN(100)
    RIGHT_TURN(100)
    LEFT_TURN(100)
    RIGHT_TURN(100)
  
    GPIO_SETUP(0,0,0,0)
            
    n-=1
