import RPi.GPIO as GPIO
from time import sleep, time
from threading import Thread

class Ultrasonik_S:
    def __init__(self, echo, trig, setup=GPIO.BCM):
        self.echo = echo
        self.trig = trig
    
        self.aradakiSure = 0
        self.anlikOlcum = 0

        GPIO.setmode(setup)

        GPIO.setup(self.trig,  GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

        GPIO.setup(trig, False)
        
        
    def OlcmeyeBasla(self):
        Thread(target=self.__Olc__).start()  
        sleep(0.2)

    def Oku(self):
        return self.anlikOlcum

    def __Olc__(self):

        while True:
            GPIO.output(self.trig, True)
            sleep(0.0001)
            GPIO.output(self.trig, False)

            sinyal_baslama = time()

            while GPIO.input(self.echo) == 1:

                sinyal_bitis = time()

                self.aradakiSure = sinyal_bitis - sinyal_baslama
                self.anlikOlcum = self.aradakiSure * 17150

