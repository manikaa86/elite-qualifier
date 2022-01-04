import time

# colored text, source: geeksforgeeks 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))

def fun():
    prCyan("What do you like to do for fun? Paint, read, or play sports?")
    user_input = input()
    user_input = user_input.lower()
    time.sleep(0.5)
    if (user_input == "paint"):
        prCyan("Sounds fun! Unfortunately I am an AI and cannot paint. My favorite painting is Starry Night. Have you seen it?")
        user_input = input()
        user_input = user_input.lower()
        if (user_input == "yes"):
            time.sleep(0.5)
            prCyan("Awesome. Van Gogh is one of my favorite painters.")
            time.sleep(0.5)
            goodbye()
        elif (user_input == "no"):
            time.sleep(0.5)
            prCyan("It is a beautiful painting. Hope you get to see it some day!")
            time.sleep(0.5)
            goodbye()
     
    elif (user_input == "read"):
        prCyan("Sounds fun! My favorite book is The Book Thief. Have you read that?")
        user_input = input()
        user_input = user_input.lower()
        if (user_input == ("yes" or "yeah")):
            prCyan("Nice. It is a sad book but very good.")
            time.sleep(0.5)
            goodbye()
        else:
            prCyan("You should read it!")
            time.sleep(0.5)
            goodbye()
    # if ((age>= 8) and (age<= 12)):
    elif ((user_input == "sports") or ( user_input == "play sports") or user_input == ("play")):
        prCyan("Sounds fun! Have you played soccer before? ")
        user_input = input()
        user_input = user_input.lower()
        if (user_input == ("yes") or ("yeah")):
            time.sleep(0.5)
            prCyan("Awesome. Unfortunately I am an AI and cannot play soccer, but I love to watch it.")
            time.sleep(0.5)
            goodbye()
        else:
            prCyan("Me too. I'm an AI so I can't play soccer, but I love to watch!")
            time.sleep(0.5)
            goodbye()
    else:
        prCyan("Sorry, I do not understand. Do you want to quit?")
        user_input = input()
        user_input = user_input.lower()
        if(user_input == ("no")):
            time.sleep(0.5)
            prCyan("Ok!")
            time.sleep(0.5)
            fun()
        else:
            time.sleep(0.5)
            goodbye()

def goodbye():
        prPurple("Nice talking to you. Goodbye!")
    # ends program


def mood():
    prCyan("How are you doing? Good, bad, or so-so?")
    user_input = input()
    user_input = user_input.lower()
    if (user_input == ("good" or "Good")):
        prCyan("Glad to hear that! ")
        time.sleep(0.5)
        fun()
    elif (user_input == ("bad" or "Bad")):
        prCyan("Sorry to hear that! ")
        time.sleep(0.5)
        fun()
    elif (user_input == ("so-so" or "So-so" or "So-so" or "so so")):
        prCyan("That's ok.")
        time.sleep(0.5)
        fun()
    else:
        prCyan("Sorry, I do not understand. Do you want to quit?")
        user_input = input()
        user_input = user_input.lower()
        if(user_input == ("no")):
            time.sleep(0.5)
            prCyan("Ok!")
            time.sleep(0.5)
            mood()
        else:
            time.sleep(0.5)
            goodbye()


def init_chat():

    prCyan("Hi! Welcome to chatbot. What's your name? ")
    user_input = input()
    prCyan("Hello " + user_input + ", you can exit whenever you want by typing 'q'. Type 'ok' to show you understand.")
    user_input = input()
    user_input = user_input.lower()
    if(user_input == ("ok")):
        prCyan("Great! Let's talk.")
        time.sleep(0.5)
        mood()
    elif(user_input == ("q")):
        time.sleep(0.5)
        goodbye()
    else:
        prCyan("You appear to have not typed 'ok'. Please type 'ok' if you understand or 'q' to quit.")
        user_input = input
        user_input = user_input.lower()
        if(user_input == ("ok")):
            prCyan("Great! Let's talk.")
            time.sleep(0.5)
            mood()
        else:
            time.sleep(0.5)
            goodbye()

if __name__ == "__main__":
    init_chat()
