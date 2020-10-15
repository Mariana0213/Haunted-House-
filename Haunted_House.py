import time  # Imports a module to add a pause

# Figuring out how users might respond


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Grabbing objects
knife = 0
flower = 0

required = ("\nUse only A, B, or C\n")  # Cutting down on duplication


# The story is broken into sections, starting with "intro"
def intro():
    print("During a dinner with your friends, you overhear"
          " a family talking about a haunted house that is not far "
          "from your hotel, you and your friends decide to visit the house "
          "and it is as creepy as the family said. You now have a decision to make. "
          " Will you:")

    time.sleep(2)
    print("""  A. Go inside the house
  B. Go back to the hotel 
  C. Wait outside of the house""")
    choice = input(">>> ")  # Here is your first choice.
    if choice in answer_A:
        option_inside()
    elif choice in answer_B:
        print("\nThat was quick. "
              "\n\nHave fun heading back to the hotel!")
    elif choice in answer_C:
        option_stair()
    else:
        print(required)
        intro()


def option_inside():
    print("\nThe house has two floors. You decide that you should"
          "split up to investigate. Which floor will you explore?:")
    time.sleep(1)
    print("""  A. First floor
  B. Go back outside
  C. Second floor""")
    choice = input(">>> ")
    if choice in answer_A:
        option_first()
    elif choice in answer_B:
        print("\nThe house must have creeped you out too much!"

              "\n\nHave fun heading back to the hotel!")
        option_playagain()
    elif choice in answer_C:
        option_second()
    else:
        print(required)
        option_inside()


def option_first():
    time.sleep(1)
    print("As you start exploring the first floor you notice a door to the basement"
          " You open the door and notice that it is dark. What will you do?")
    print("""A. Go down alone 
      B. Call for a friend 
      C. Go back to the outside""")
    choice = input(">>>")
    if choice in answer_A:
        print("\nAs you get to the bottom, you sense you are not the only one down there."
              "You try to turn and make a run for it but you trip,"
              "the ghost got you and you died.")
        option_playagain()
    elif choice in answer_B:
        print("\nYou and your friend cautiously walk down the steps, "
              "your friend found a flashlight upstairs and shines it around the room."
              "You see a shadow rush towards you from the corner and gets a hold of you friend."
              "You run up the stairs and make it back to your car. You're a bad friend, but you survive.")
    elif choice in answer_C:
        print(print("\nThe house must have creeped you out too much!"

                    "\n\nHave fun heading back to the hotel!"))
    else:
        print(required)
        option_first()


def option_second():
    print("\nYou were hesitant, but you decided to head up to "
          "the second floor. While walking upstairs you hear a noise. You "
          "notice a knife on the ground. Do you pick up the knife. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        knife = 1
    else:
        knife = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""  A. Stand at the top of the stairs  
      B. Figure out where the noise came from  
      C. Head back downstairs""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nReally? Your going to stand at the top of the steps when you heard a noise"
              "in a haunted house ? I guess you don't watch many scary movies"
              "...\nYou died!")
        option_playagain()
    elif choice in answer_B:
        if knife > 0:
            print("\nYou made a noise which attracted "
                  "the ghost, which thought you were no match. As he floated "
                  "closer and closer, your heart beat rapidly. As the ghost "
                  "reached out to grab you, you pierced the knife into "
                  "their chest and it startled them. It gave you enough time to run away. \nYou survived!")
        else:
            print("\nYou should have picked up that knife. You're "
                  "defenseless.\nYou died!")
            option_playagain()
    elif choice in answer_C:
        print("\n As you are walking down the stairs, you here the noise"
              "again. You don't take any chances and run back to the car "
              "and wait for your friends ")
        option_run()
    else:
        print(required)
        option_second()


def option_run():
    print("\nAs you you get to the car you realize the doors are locked."
          "Do you:")
    time.sleep(1)
    print("""A. Wait outside of the car 
          B. Go back inside""")
    choice = input(">>>")
    if choice in answer_A:
        print("It seems like those noises were just your friends trying to scare you."
              "They came back to the car laughing. You will hear that story forever,"
              "but at least you survived!")
    elif choice in answer_B:
        print("You should have listened to your intuition,"
              "the ghost got you as soon as you walked through the door.")
        option_playagain()
    else:
        print(required)
        option_second()
        option_run()


def option_stair():
    print("\nWhile you were waiting and staring at the outside of the house you"
          " see a man's shadow near the window. You will:")
    time.sleep(1)
    print("""  A. Slowly back away from the house  
  B. Run towards the car  
  C. Go into the house to take a closer look""")
    choice = input(">>> ")
    if choice in answer_A:
        print("Did the shadow scare you? "
              "\n\nMaybe the house isn’t abandoned! "
              " What do you want to do?")
        option_scared()
    elif choice in answer_B:
        print("\nThe shadow must have scared you! "
              "\n\nHave fun heading back to the hotel!")
    elif choice in answer_C:
        option_house()
    else:
        print(required)
        option_stair()

def option_scared():
    print("""A. Go inside where your friends are
          B. Call out to your friends
          C. Make your way to the car as fast as possible""")
    choice = input(">>>")
    if choice in answer_A:
        print("The door closes behind you and there is the shadow standing in front of you"
              " You freeze because you are afraid. The air is cold. It turned out to be a ghost that lived in the "
              "house."
              " You died!")
        option_playagain()
    elif choice in answer_B:
        print("That was not smart. The night is dark and there are creepy sounds coming from everywhere."
              " Your shouts attracted the mysterious man and he turned out to be a ghost. You died!")
        option_playagain()
    elif choice in answer_C:
        print("You start off by walking slowly then end up running to the car. "
              " You notice that the car is locked. Then you hear your friends laughter. "
              " They were trying to scare you and you know that you will never hear the end of that story. "
              " But you are safe and sound!")
    else:
        print(required)


def option_house():
    print("\nWhile  running, you notice a "
          "sword lying in the mud. You quickly reach down and to try to grab it, "
          "but miss. You try to calm your heavy breathing as you hide "
          "behind a dilapidated building, waiting for the shadow to come "
          "charging around the corner. You notice a purple flower "
          "near your foot. Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        flower = 1
    else:
        flower = 0
    print("You hear its heavy footsteps and ready yourself for "
          "the figure.")
    time.sleep(1)
    if flower > 0:
        print("\nYou quickly hold out the purple flower, somehow "
              "hoping it will stop this figure. It does! The ghost was looking "
              "for love. "
              "\n\nThis got weird, but you survived!")
    else:
        print("\nMaybe you should have picked up the flower. "
              "\n\nYou died!")
def option_playagain():
    wants_to_play = True
    while wants_to_play:
        print("Oh no! Would you like to play again?")
        choice = input(">>>")
        if choice in yes:
            intro()
        elif choice in no:
            print("Thank you for playing!")
            wants_to_play = False








if __name__ == '__main__':
    intro()