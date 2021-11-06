import RPi.GPIO as GPIO          
from time import sleep

pump = 37

GPIO.setwarnings(False)
GPIO.setup(pump,GPIO.OUT)

print("START")
print("\n")    

while(1):

    x=input()
    
    if x=='p':
        print("pump")
        GPIO.output(pump,GPIO.HIGH)

    elif x=='s':
        print("stop")
        GPIO.output(pump,GPIO.LOW)
    
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
