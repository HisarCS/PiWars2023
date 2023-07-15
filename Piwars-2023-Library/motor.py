from pololu_drv8835_rpi import motors
import math

class Motor:
    def __init__(self):
        self.channel1 = 0
        self.channel2 = 0
        self.jchannel1=0
        self.jchannel2 = 0

    def hiz(self, hizSag, hizSol):
        self.channel1 = hizSag
        self.channel2 = hizSol

        480 if hizSag > 480 else hizSag
        -480 if hizSag < -480 else hizSag

        480 if hizSol > 480 else hizSol
        -480 if hizSol < -480 else hizSol

        motors.setSpeeds(hizSag, hizSol)
    
    def sagHiz(self,hSag):
         self.jchannel1 = hSag
         480 if hSag > 480 else hSag
         -480 if hSag < -480 else hSag
        
        motor.motor1.setSpeed(hSag)
        
    def solHiz(self,hSol):
         self.jchannel2 = hSol
         480 if hSol > 480 else hSol
         -480 if hSol < -480 else hSol
        
        motor.motor2.setSpeed(hSol)
