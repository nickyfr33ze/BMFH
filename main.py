# Author: Nick Friesen
# Date: 01/28/2024
# Description: This program will ask the user how they are feeling, and will respond with a quote based on their response from Charlie Mackey's : The Boy, The Mole, The Fox, and The Horse.

import random
import time
# might use the 'webbrowser', might not

print("How are you feeling right now?")
userInput = input("Good or bad?: ")
# Asks how the user is feeling to start

goodFeelings = ["good", "great", "happy", "excited", "confident", "estatic", "fearless"] # houses all the possible keywords for good feelings
badFeelings = ["bad", "sad", "terrible", "scared", "worried", "terrified", "fearful", "not"] # houses all the possible keywords for bad feelings

responses = {
    # houses all the possible responses
    1: "'The great illusion, is that life should be perfect.' -The Mole",
    2: "'We all need someone to lean on.' -The Boy",
    3: "'Asking for help, isn't giving up. It is refusing to give up.' -The Horse",
    4: "'When the big things feel out of control, focus on what you love right under your nose.' -The Horse",
    5: "'What is the bravest thing you've ever said?' -The Boy  |  'Help.' -The Horse",
    6: "'Help is always given to those who ask for it.' -The Fox"
}

if any(keyword in userInput for keyword in goodFeelings):
    print("")
    print(random.choice(list(responses.values())))
    print("")

elif any(keyword in userInput for keyword in badFeelings):
    print("")
    print("I'm sorry you're feeling this way...")
    time.sleep(2)
    print("You are not alone in this. No matter what you see on social media, everyone has their own struggles.")
    time.sleep(2)
    print("Read this aloud: ")
    time.sleep(2)
    print("")
    print(random.choice(list(responses.values())))
    print("")


repeatUserInput = input("Would you like to read another quote? (Y/N): ")

while repeatUserInput == "Y":
    print("")
    print(random.choice(list(responses.values())))
    print("")
    time.sleep(2)
    repeatUserInput = input("Would you like to read another quote? (Y/N): ")

if(repeatUserInput == "N"):
    print("")
    print("I hope this made you feel a little better today. \nI'm so gald you're here <3")
    print("")