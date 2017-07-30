import Tkinter
import RPi.GPIO as GPIO
import time

P_DILDO = 12 # adapt to your wiring
fPWM = 50  # Hz (not higher with software PWM)
duty = 0
event = 0

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_DILDO, GPIO.OUT)
    pwm = GPIO.PWM(P_DILDO, fPWM)
    pwm.start(0)

def read_duty(duty):
    duty = float(duty)
    pwm.ChangeDutyCycle(duty)
    text.delete('1.0', '1.6')
    text.insert('1.0', duty)
    print "D =", duty, "%"

def increase_duty(event):
    global duty
    duty += 3
    if duty >= 100:
       duty = 100
    pwm.ChangeDutyCycle(duty)   
    text.delete('1.0', '1.6')
    text.insert('1.0', duty)
    print "D =", duty, "%"

def decrease_duty(event):
    global duty
    duty -= 3
    if duty <= 0:
       duty = 0
    text.delete('1.0', '1.6')
    text.insert('1.0', duty)
    pwm.ChangeDutyCycle(duty)
    print "D =", duty, "%"
    
setup()


root = Tkinter.Tk()
root.title( "MOSFET PWM Dildo Demo" )
root.geometry( "420x240" )
scale = Tkinter.Scale(orient='horizontal', from_=0, to=100, width=40, length=4000, command=read_duty)
scale.pack()
up = Tkinter.Button(root, text="+", command= lambda: increase_duty(event))
up.pack()
down = Tkinter.Button(root, text="-", command= lambda: decrease_duty(event))
down.pack()
text = Tkinter.Text(root, height=1, width=16)
text.pack()
root.bind("<Up>", increase_duty)
root.bind("<Down>", decrease_duty)


root.mainloop()



