'''
V3 - 2 Port Variation
'''
# Import libraries needed for blinking the LED
import board
import digitalio
def pressed(count):
    if(count == 0):
        print(count)
        count = 1
        led1.value = True
    elif(count == 1):
        print(count)
        count = 2
        led2.value = True
    elif(count == 2):
        print(count)
        led1.value = False
        led2.value = False
        count = 0
    while True:
        if(button.value):
            break

# Configure the GPIO pin connected to the LED as a digital output
led1 = digitalio.DigitalInOut(board.GP19) #blue and red
led1.direction = digitalio.Direction.OUTPUT

# Configure the GPIO pin connected to the LED as a digital output
led2 = digitalio.DigitalInOut(board.GP14) #green
led2.direction = digitalio.Direction.OUTPUT

# Configure the GPIO pin connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP21)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor

# Print a message on the serial console
print('Hello! My LED is controlled by the button.')

# Loop so the code runs continuously
count = 0
while True:
    if(not button.value):
        if(count == 0):
            pressed(0)
            count = 1
        elif(count == 1):
            pressed(1)
            count = 2
        else:
            pressed(2)
            count = 0
