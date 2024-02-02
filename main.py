# Author: Nick Friesen
# Date: 01/28/2024
# Description: This program will ask the user how they are feeling, and will respond with a quote based on their response from Charlie Mackey's : The Boy, The Mole, The Fox, and The Horse.

import random
import webbrowser 
# might use the 'webbrowser', might not

print("How are you feeling right now?")
userInput = input("Good or bad?: ")
# Asks how the user is feeling to start

goodFeelings = ["good", "great", "happy", "excited", "confident", "estatic", "fearless"] # houses all the possible keywords for good feelings
badFeelings = ["bad", "sad", "terrible", "scared", "worried", "terrified", "fearful"] # houses all the possible keywords for bad feelings

responses = {
    # houses all the possible responses
    1: "'The great illusion, is that life should be perfect.' -The Mole",
    2: "'We all need someone to lean on.' -The Boy",
    3: "'Asking for help, isn't giving up. It is refusing to give up.' -The Horse",
    4: "'When the big things feel out of control, focus on what you love right under your nose.' -The Horse",
    5: "'What is the bravest thing you've ever said?' -The Boy",
    6: "'Help is always given to those who ask for it.' -The Fox"
}

if any(keyword in userInput for keyword in goodFeelings):
    print("That's great!")
#   What do we print when someone is feeling good? Should we redirect to a funny cat pic/video?
#    print("Here's a quote to make you feel even better:")
#    print(random.choice(list(responses.values())))

elif any(keyword in userInput for keyword in badFeelings):
    print("That's too bad.")
    print("Read this aloud: ")
    print(random.choice(list(responses.values())))

else:
    print("I don't understand that feeling.")

