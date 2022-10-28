#Pyautogui is for controlling the keyboard.
from pyautogui import *
from time import *

#Getting user input.
message_amount = int(input('How many messages do you want to send? >>>  '))
message_content = str(input('What do you want the messages to be? >>>  '))
message_speed = int(input('How fast do you want to send the messages?(delay in seconds) >>>  '))

#A 10 second delay for the user to move their curser into a text field.
print('You have 10 seconds to place your cursor in a text field.')
sleep(10)

#The main function
def spammer():
    #Executes the indented code 'message_amount' times.
    for i in range(message_amount):
        #typewrite writes message content to the text field.
        typewrite(message_content)
        #press('button') presses a button on the keyboard.
        press('enter')
        #pauses the code for 'message_speed' amount of time.
        sleep(message_speed)

spammer()
