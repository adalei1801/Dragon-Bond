# Ashley King
# Allows the game to take pauses inbetween prompts when written
import time

# Start of the game. Introduces setting (the cave) and the dragon. time.sleep() breaks up the story starting and the input instructions
print("Welcome to Dragon Bond")
time.sleep(2)
print("--Input answers exactly as they are written in the prompt--")
time.sleep(2)

print("You arrive at the cave on the map and walk in")

print(""" 
        ___..-.              
     ._/  __ \_`-.__       
     / .'/##\_ `-.  \--.  
     .-_/#####\  /-' `\_      
      /###@@###\_  \._   `-  
___ _|###########\_`.  -' \    
    " "'"''"'"'''" ''"'"''"  

    """)

print("You see a dragon")

print("""
                \||/
                |  @___oo
      /\  /\   / (__,,,,|
     ) /^\) ^\/ _)
     )   /^\/   _)
     )   _ /  / _)
 /\  )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___)\
 | \____(      )___) )___ 
  \______(_______;;; __;;;

  """)


# First choice, asks if player wants to kill the dragon or feed it. Stores answer in variable for if and elif statements to use
killorfeed = input("Do you kill it or feed it? ")

# If and elif statements that move the game accoridng to the player's choice of killing the dragon or feeding it.
if killorfeed == "kill it":
  print("You draw your sword")
  print("""
  
  ====|-------------
  
  """)
  # Pauses the game for 2 seconds 
  time.sleep(2)
  print("The dragon sets you on fire")
  print("GAME OVER")
  exit(print("Incorrect Responses, restart"))
  
elif killorfeed == "feed it":
  print("You take out the egg you brought")
  print("""
  
  ,'"`.
 /     \
:       :
:       :
 `.___,'
 
 
 """)
  print("The dragon happily accepts  and lowers their head")
  # Stops the game and tells the player to restart the game as a result of invalid input
else: 
  exit(print("Incorrect Response, restart"))

# Asks player whether they want to kill the dragon or leave the cave and stores answer in variable to use for if and elif statements.
killorleave = input("Do you kill it or leave? ")

# Outlines the game's path depending on if the player kills the dragon or leaves the cave.
if killorleave == "kill it":
  print("You slowly draw your sword and swipe at the dragon")
  time.sleep(3)
  print("You injure the dragon, but it burns you alive")
  print("GAME OVER")
  exit(print("Incorrect Responses, restart"))
elif killorleave  == "leave":
  print("You bid the dragon goodbye, with headpats, and go home")
  time.sleep(3)
  print("NEXT DAY")
  print("""
  
          |
          |   .
   `.  *  |     .'
     `. ._|_* .'  .
   . * .'   `.  *
-------|     |-------
   .  *`.___.' *  .
      .'  |* `.  *
    .' *  |  . `.
        . |
          |    
          
          """)
  # Tells player that the game has ended since responses were invalid
else:
  exit(print("Incorrect Response, restart"))

print("You return to the cave and go inside")

# Gives the player the opportunity to feed the dragon or play a game. Stores answer for if and elif statements
feedorgame =  input("Do you feed the dragon or play catch? ")

# Outlines the different paths depending on the player's choice
if feedorgame == "play catch":
  print("You dangle the egg and toss it. The dragon does not want games and eats you.")

  print("""                            /|               |\                              
                           / | ___-------___ | \                             
                          /  \/ ^ /\   /\ ^ \/  \                            
                         |   (  O-. \ / .-O  )   |                           
                      /-\/   ^-----^-V-^-----^   \/-\                        
                    /-      (~ 0O0 ~) (~ 000 ~)     -\                       
                   <        (~ OOO ~) (~ 000 ~)       >                      
                    \-      (____---===---____)     -/                       
                     \-   /\ \ \|         |/ / /\  -/                        
                     -/\-/  \ \ V         V / /  \-/\-                       
                        v    \ \           / /    v                          
                              \ \ A     A / /                                
                               \_\^-----^/_/                                 
                                \_/\___/\_/                                  
                                  \_____/""")
  print("""

    __         __
   |  |       |  |
   _||_       _||_ 
  |    |     |    |
  |____|     |____|
  |    |_    |    |_
  |      |   |      |
  ````````   ````````
  
  """)
  print("GAME OVER")
  time.sleep(1)
  exit(print("Restart"))
elif feedorgame == "feed the dragon":
  print("The dragon eats the egg")
  # Tells player that the game ended due to incorrect responses
else:
  exit(print("Incorrect Response, restart"))

# Allows the player to feed the dragon or relax. Also stores the answer in a variable that the if and elif statements use.
feedorrest = input("Do you feed the dragon or rest? ")

# Determines the game's progress depending on whether or not the player feeds the dragon again or rest.
if feedorrest == "feed the dragon":
  print("You give the dragon another egg")
  time.sleep(2)
  print("The dragon accepts the egg  and lowers their head, you pet the dragon")
elif feedorrest == "rest":
  print("You sit down and relax as the dragon rests beside you")
  print("You pet the dragon")

# Allows the player restart the game if input is invalid
else:
  exit(print("Incorrect Response, restart"))

# Allows the player to leave the cave or stay with the dragon. Answer is stored in variable iin order for if and elif statements to progress the game.
leaveorstay = input("Do you go home or stay? ")

# Chart's the game's course depending on the player's choice of leaving or staying
if leaveorstay == "go home":
  print("You get up, say goodbye, and go home")
elif leaveorstay == "stay":
  print("You stay awhile longer")
  time.sleep(2)
  print("You go home after a hour")
  time.sleep(3)

# Time skip for the game and details for what happened inbetween previous interaction and the next one. time.sleep() breaks up text to make reading easier.
print("You see the dragon every day for a month")
time.sleep(2)
print("Today the dragon lies on its stomach after breakfast")

# Asks player to climb on the dragon or hesitate. Answer is stored in variable for later use
climborquestion = input("Do you climb on or question? ")

# Puts the "climb on" route into a function in case player picks "question" option. 
def climbquestion():
  print("You get on the dragon and it flies off")
  print("""
  
    <>=======() 
    (/\___   /|\\          ()==========<>_
        \_/ | \\        //|\   ______/ \)
          \_|  \\      // | \_/
            \|\/|\_   //  /\/
             (oo)\ \_//  /
            //_/\_\/ /  |
           @@/  |=\  \  |
                \_=\_ \ |
                  \==\ \|\_ 
               __(\===\(  )\
              (((~) __(_/   |
                   (((~) \  /
                   ______/ /
                   '------'
                   
                   """)

# Runs climb on path function if player chooses to climb on the dragon
if climborquestion == "climb on":
  climbquestion()
  # If the player decides to question the dragon it allows the ending to run by calling the climbquestion function
elif climborquestion == "question":
  print("You indictate some confusion")
  print("The dragon gestures towards its back, they want you to climb on")
  print("You do so")
  climbquestion()

#Tells player that the response is incorrect and to restart as well as ending the game
else:
  exit(print("Incorrect Response, restart"))


# Ending text to the game after the player rides the dragon
print("The dragon lands after a short ride")
print("You have accomplished your goal")
print("You have tamed a dragon")

# Spaces out epilogue by pausing the game
time.sleep(3)
print("While the rest of the world lives in fear of these creatures, you see potential")
print("Now, you can move on to your next goal...")
time.sleep(3)

#Sets up possible sequel
print("Conquest")
time.sleep(3)
print("""

 _____ _                 _          _____          
|_   _| |__   __ _ _ __ | | _____  |  ___|__  _ __ 
  | | | '_ \ / _` | '_ \| |/ / __| | |_ / _ \| '__|
  | | | | | | (_| | | | |   <\__ \ |  _| (_) | |   
 _|_| |_| |_|\__,_|_|_|_|_|\_\___/ |_|  \___/|_|   
|  _ \| | __ _ _   _(_)_ __   __ _| |              
| |_) | |/ _` | | | | | '_ \ / _` | |              
|  __/| | (_| | |_| | | | | | (_| |_|              
|_|   |_|\__,_|\__, |_|_| |_|\__, (_)              
               |___/         |___/                 
               
               """)