import RPi.GPIO as GPIO
import time

ROW_5 = 18
ROW_7 = 24
COL_2 = 20
COL_3 = 16
ROW_8 = 25
COL_5 = 19
ROW_6 = 23
ROW_3 = 27
ROW_1 = 4
COL_4 = 12
COL_6 = 26
ROW_4 = 22
COL_1 = 21
ROW_2 = 17
COL_7 = 13
COL_8 = 6
ALL_COL = [COL_1, COL_2, COL_3, COL_4, COL_5, COL_6, COL_7, COL_8]
ALL_ROW = [ROW_1, ROW_2, ROW_3, ROW_4, ROW_5, ROW_6, ROW_7, ROW_8]

GPIO.setmode(GPIO.BCM)
GPIO.setup(ALL_ROW, GPIO.OUT, initial=0)
GPIO.setup(ALL_COL, GPIO.OUT, initial=0)

GPIO.output(6, 1)
GPIO.output(13, 1)

time.sleep(2)

GPIO.cleanup()
