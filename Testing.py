#creating a maze
#at one point, i'd love to have it randomly generate a starting room

#should try and understand while loops more, that'll probably help

def Labyrinth():
    print("Hello. You are trapped in a maze. Can you find the way out?")
    print("Instructions: \n 1) You must enter all words with a capital letter \n 2) Once you've investigated all walls in a room, you will be prompted one last time to pick a final wall. If you fail to enter a new room, the game will end.")
    print("Let us begin . . .")

Labyrinth()

def FirstMove():
#User in Room5
    print("You are in the middle of a maze, trapped in a room. You look around the room. Which wall would you like to investigate?")
    Wall1 = input("North, East, South, or West? ")
    if Wall1 == "North":
        print("Excellent. You chose North. There is a door.")
        Door1 = input("Would you like to go through the door? Y/N ")
        if Door1 == "Yes": #North
            print("You enter another room.")
#User in Room4
            def SecondMove():
                print("You look around the new room. Which wall would you like to investigate?")
                Wall2 = input("North, East, South, or West? ")
                if Wall2 == "North":
                    print("There is no door on this wall.")
                    print("You look around the room. Which wall would like to investigate?")
                    xWall2 = input("North, East, South, or West? ")
                    while xWall2 == "North" or "West":
                        print("There is no door on this wall.")
                        xWall3 = input("You look around the room. Which wall would like to investigate? \n North, South, East, or West? ")
                        while xWall3 == "North" or "West":
                            print("There is no door on this wall.")
                            #xWall4 = input("Hello") stopped here
                    else:
                        print("yay") #morehere
                    #more here
                elif Wall2 == "East":
                    print("There is a door.")
                    Door8 = input("Would you like to go through the door? Y/N ")
                    if Door8 == "Yes":
                        print("A chilly wind brushes against the back of your neck as you enter the new room.")
#User in Room 9
            #here
#User in Room5
                        #more here
                    else:
                        print("You did not enter the other room. \n You look around the room. Which wall would you like to investigate?")
                        #more here
                elif Wall2 == "South":
                    print("There is a door.")
                    Door9 = input("Would you like to go through the door? Y/N ")
                    if Door9 == "Yes":
                        print("You re-enter the starting room.")
                        #more here
                    else:
                        print("You did not enter the other room. \n You look around the room. Which wall would you like to investigate?")
                        #more here
                else:
                    print("There is no door on this wall.")
                    print("You look around the room. Which wall would like to investigate?")
                    #more here
            SecondMove()
#User in Room5
        else: #North
            print("You did not enter the other room. \n You look around the room. Which wall would you like to investigate?")
            Door2 = input("North, East, South, or West?")
            if Door2 == "East":
                print("There is no door on this wall.")
                print("You look around the room. Which wall would like to investigate?")
            #more here
            if Door2 == "South":
                print("There is a door on this wall.")
                Door12 = input("Would you like to go through the door? Y/N ")
                if Door12 == "Yes":
                    print("Excellent. You enter another room.")
                    #more here
                else:
                    print("You did not enter the new room.")
                    print("You look around the room. Which wall would like to investigate?")
                    #morehere
#User in Room5
    elif Wall1 == "East":
        print("There is no door on this wall.")
        print("You look around the room. Which wall would you like to investigate?")
        Door7 = input("North, East, South, West?")
        if Door7 == "North":
            print("Wonderful. You choose North. There is a door.")
            Door13 == input("Would you like to go through the door? Y/N ")
            if Door13 == "Yes":
                print("You enter another room.")
                #more here
            else:
                print("You did not enter the new room.")
                print("You look around the room. Which wall would like to investigate?")
#WHERE I STOPPED LAST
               # Door14 = input("North, East, South, West")
               # if Door14 =
        #more here
#User in Room5
    elif Wall1 == "South":
        print("Fantastic. You choose South. There is a door.")
        Door3 = input("Would you like to go through the door? Y/N ")
        if Door3 == "Yes": #South
            print("You enter another room.")
#User in Room6
            def ThirdMove():
                print("As you enter, you can faintly smell cinnamon.")
                print("You look around the room. Which wall would you like to investigate?")
                Door9 = input("North, East, South, or West?")
                if Door9 == "North":
                    print("You re-enter the starting room.")
                    #more here
                elif Door9 == "East":
                    print("There is no door on this wall.")
                    print("You look around the room. Which wall would like to investigate?")
                    #more here
                elif Door9 == "South":
                    print("There is no door on this wall.")
                    print("You look around the room. Which wall would like to investigate?")
                    #more here
                else:
                    print("There is a door.")
                    Door10 = input("Would you like to go through the door? Y/N ")
                    if Door10 == "Yes":
                        print("You enter another room.")
#UserinRoom1
                     #morehere
                    else:
                        print("You did not enter the other room. \n You look around the room. Which wall would you like to investigate?")
                        #morehere
            ThirdMove()
#User in Room5
        else: #South
            print("You did not enter the other room. \n You look around the room. Which wall would you like to investigate?")
            #Door4 = input("North, East, South, or West?")
            #more here

    else: #West
        print("Amazing. You chose West. There is a door.")
        Door5 = input("Would you like to go through the door? Y/N ")
        if Door5 == "Yes":
            print("You enter another room.")
#User in Room2
            #more here
            def FourthMove():
                print("As you enter, you notice a dark stain on the northern wall.")
                print("You look around the room. Which wall would you like to investigate?")
                Door11 = input("North, East, South, or West? ")
                if Door11 == "West":
                    print("There is no door on this wall.")
                    #more here
                elif Door11 == "North":
                    print("You see that the stain above the door seems to reach down with long fingers into the crack between the top of the door and the wall.")
                    Door13 = input("Would you like to go through the door? Y/N ")
                    if Door13 == "Yes":
                        print("You enter another room.")
#User in Room3
                        #morehere
#User in Room2
                    else:
                        print("You did not enter the other room.")
                        #more here
                elif Door11 == "South":
                    print("There is a door on this wall.")
                    Door12 = input("Would you like to go through the door? Y/N ")
                    if Door12 == "Yes":
                        print("You enter another room.")
#User in Room 1
                        #more here
#User in Room2
                    else:
                        print("You did not enter the other room.")
                        #more here
            FourthMove()
#User in Room5
        else: #West
            print("You did not enter the other room. \n You look around the room. Which wall would you like to investigate?")
            #Door6 = input("North, East, South, or West?")
            #more here
FirstMove()
