from time import sleep
import RPi.GPIO as GPIO 

class Servo:

    def __init__(self, pin, GPIOMode= GPIO.BCM):
        GPIO.setmode(GPIOMode)
        
        GPIO.setup(pin, GPIO.OUT)
        self.pwm.start(0)
        self.pin = pin
        self.hedefAci = 90
        self.suankiAci = 90
        self.uykumodu = True
        self.surekli = False

    def surekliDonme(self):
        self.surekli = True
        GPIO.output(self.pin ,True)

    def secilenAci(self):
        self.surekli = False
        GPIO.output(self.pin ,False)
    
    def __surekliAciAyarla__(self, aci): #__functionName__ is used to create a secret function to be used in other functions
        dcycle =  aci/18 +2.5
        self.pwm.ChangeDutyCycle(dcycle)
    
    def __tekAciAyarla__(self,aci):
        sinyalUzunluğu = self.hedefAci/ 18 + 2.5
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(sinyalUzunluğu)
        dcycle =  aci/18 +2.5
        self.pwm.ChangeDutyCycle(dcycle)

    def uyu(self):
        dAci = abs(self.hedefAci - self.suankiAci)
        gUyku = dAci / 180
        sleep(gUyku)
        GPIO.output(self.pin,False)
        self.pwm.ChangeDutyCycle(0)
        self.suankiAci = self.hedefAci
        self.uykumodu = True

    def aciAyarla(self, aci):        

        self.uykumodu = False

        self.hedefAci = aci


        if self.surekli:
            self.__surekliAciAyarla__(self.hedefAci)
        if not self.surekli and not self.uykumod:
            self.__tekAciAyarla__(self.hedefAci)
        if self.uykumodu and self.suankiAci != self.hedefAci:
            self.uykumodu = False
