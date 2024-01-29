print("How are you feeling right now?")
userInput = input("Good or bad?: ")
# Asks how the user is feeling to start

goodFeelings = ["good", "great", "happy"] # houses all the possible keywords for good feelings
badFeelings = ["bad", "sad", "terrible"] # houses all the possible keywords for bad feelings

if any(keyword in userInput for keyword in goodFeelings):
    print("That's great!")

elif any(keyword in userInput for keyword in badFeelings):
    print("That's too bad!")

else:
    print("I don't understand that feeling.")

