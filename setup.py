from setuptools import setup
import subprocess
import os

os.system("echo hello")
os.system('sudo apt-get install libcblas-dev')
os.system('sudo apt-get install libhdf5-dev')
os.system('sudo apt-get install libhdf5-serial-dev')
os.system('sudo apt-get install libqtwebkit4')
os.system('sudo apt-get install libqt4-test')
os.system('sudo apt-get install libatlas-base-dev')
os.system('sudo apt-get install libjasper-dev')

setup(
    name = "Pi20",
    version = "0.0.6",
    author = " Emre Dayangac, Poyraz Ozzengi",
    author_email = "emre.dayangac@hisarschool.k12.tr, poyraz.ozzengi@hisarschool.k12.tr",
    description = "Library that makes use of sensors, motors, and servos in the PiWars Turkey robot kit by HisarCS",
    packages = ["Piwars-2023-Library"],
    classifiers=["Development Status :: 1 - Alpha"],
    install_requires=[
        'picamera',
        'pygame',
        'RPi.GPIO',
        'wiringpi',
        'numpy',
        'opencv-contrib-python==4.5.3.56'
    ]

)
