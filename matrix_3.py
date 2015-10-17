import RPi.GPIO as GPIO
import time

ROW_1 = 6
ROW_2 = 16
ROW_3 = 25
ROW_4 = 19
ROW_5 = 4
ROW_6 = 24
ROW_7 = 17
ROW_8 = 18
COL_1 = 12
COL_2 = 27
COL_3 = 22
COL_4 = 13
COL_5 = 23
COL_6 = 26
COL_7 = 20
COL_8 = 21
ALL_COL = [COL_1, COL_2, COL_3, COL_4, COL_5, COL_6, COL_7, COL_8]
ALL_ROW = [ROW_1, ROW_2, ROW_3, ROW_4, ROW_5, ROW_6, ROW_7, ROW_8]

GPIO.setmode(GPIO.BCM)
GPIO.setup(ALL_ROW, GPIO.OUT, initial=0)
GPIO.setup(ALL_COL, GPIO.OUT, initial=0)

time.sleep(2)

GPIO.cleanup()
