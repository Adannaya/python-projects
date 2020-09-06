from time import sleep #imports sleep (wait) from the time module
from  random import randrange as rr, choice #imports randrange and choice from the random module, and renames randrange to rr
name = input("Hello, what is your name? ") #asks for the user's name and saves it in a variable
sleep(rr(5)) #waits between 0 and 4 seconds
print("Hello " + name) #greets the user with their name

feeling = input("How are you today? ").lower() #asks how the user is feeling and converts it to lowercase
sleep(rr(5)) #waits between 0 and 4 seconds
positive = ["good", "great", "awesome", "fine", "ok", "nice", "happy"] #creates a list of positive emotions
good = False #sets the variable good to False
for x in positive: #starts a for loop with each item in the list
    if x in feeling: #starts a conditional for if the user is feeling one of the emotions in the list
        good = True #sets good to True
        break #ends the for loop
if good == True: print("I'm feeling good too!") #if statement to check if the user is happy
else: print("I'm sorry to hear that!") #else statement for if they are unhappy

sleep(rr(5)) #waits between 0 and 4 seconds
favcolour = input("What is your favourite colour? ") #asks the user's favourite colour and saves it in a variable
colours = ["red", "green", "blue", "pink", "purple"] #creates a list of colours
sleep(rr(5)) #waits between 0 and 4 seconds
print("My favourite colour is " + choice(colours) + "!") #chooses a colour from the list and displays it
