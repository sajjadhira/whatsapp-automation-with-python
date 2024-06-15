import os
import pyautogui
import time
import webbrowser
    
def send_message(contact, message):
    
    number = contact
    
    contact = contact.strip().replace(' ', '').replace('-', '')
    
    if not contact.startswith('+'):
        return
    
    # Open the WhatsApp web URL for the given phone number
    url = f'https://wa.me/{contact}'
    webbrowser.open(url)
    
    time.sleep(10)  # Wait for WhatsApp Web to open and load the chat
    
    # Click on the message box (coordinates need to be adjusted for your screen)
    pyautogui.click(800 , 900)
    
    # Type the message and press Enter
    pyautogui.write(message)
    # pyautogui.press('enter')
    
    
    # remove the used number from the numbers file
    with open(numbersFile, 'r') as file:
        lines = file.readlines()
    with open(numbersFile, 'w') as file:
        for line in lines:
            if line.strip() != number:
                file.write(line)
    
    
    usedNumbersFile = os.path.join('utils', 'used_numbers.txt')
    # write the used number to the used numbers file
    if not os.path.exists(usedNumbersFile):
        with open(usedNumbersFile, 'w') as file:
            file.write(number)
    else:
        # append the used number as a new line
        with open(usedNumbersFile, 'a') as file:
            file.write(number + '\n')
            
            
    time.sleep(3)


messageFile = os.path.join('utils', 'message.txt')
# read content of message file
with open(messageFile, 'r') as file:
    message = file.read()
    
numbersFile = os.path.join('utils', 'numbers.txt')
# read content of numbers file
with open(numbersFile, 'r') as file:
    numbers = file.readlines()

for number in numbers:
    send_message(number, message)
# make number file empty
open(numbersFile, 'w').close()
