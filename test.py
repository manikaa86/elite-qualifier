import random

# premade responses
def generate_response(user_input):
  responses = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "Programming is fun!"
  ]
  return random.choice(responses)

# fun topic to talk about
def fun(user_input): 
     print ("That sounds exciting. I like to " + user_input + " too.")

def init_chat():
  quit_character = 'q'

  #talking begins here
  user_input = input("Hi! Welcome to chatbot. What's your name? " + "\n")
  user_input = input("Hello " + user_input + ", you can exit whenever you want by typing 'q'. How are you?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    if user_input == "bad":
        print ("Sorry to hear that. We can talk about somethign else.") 
        user_input = input("We can talk about something else. What do you like to do for fun? ")
        fun(user_input)
        break
    else:
        print ("What do you like to do for fun? ")
        break
        # user_input = input(generate_response(user_input) + "\n")
    
    #user types q
  if user_input == quit_character:
     print("You have selected to quit. Goodbye!")


if __name__ == "__main__":
  init_chat()




  
  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    if user_input == "bad":
        print ("Sorry to hear that. We can talk about somethign else.") 
        user_input = input("We can talk about something else. What do you like to do for fun? ")
        fun(user_input)
        break
    else:
        print ("What do you like to do for fun? ")
        break
        # user_input = input(generate_response(user_input) + "\n")
    
    #user types q
  if user_input == quit_character:
     print("You have selected to quit. Goodbye!")