import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

start = 0
end = 0

GPIO.cleanup()

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

print("Pinos definidos\nTRIG={0}\nECHO={1}".format(TRIG, ECHO))

GPIO.output(TRIG, False)
print("Setando False para TRIG\n")
time.sleep(2)

print("Status pino TRIG: {}\n" .format(str(GPIO.input(ECHO))))

print("Ira realizar o pulso\n")
GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)
print("Pulso realizado\n")

while GPIO.input(ECHO) == False:
    print("ECHO -->  False\n")
    start = time.time()

while GPIO.input(ECHO) == True:
    print("ECHO --> True\n")
    end = time.time()

sig_time = end - start

#CM:
distance = sig_time  * 17150

print('Distance: {} centimeters'.format(distance))

GPIO.cleanup()
