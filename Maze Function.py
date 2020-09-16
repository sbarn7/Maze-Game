#creating a maze
#at one point, i'd love to have it randomly generate a starting room

#should try and understand while loops more, that'll probably help

def Labyrinth():
    print("Hello. You are trapped in a maze. Can you find the way out?")
    print("Instructions: \n 1) You must enter all words with a capital letter \n 2) Once you've investigated all walls in a room, you will be prompted one last time to pick a final wall. If you fail to enter a new room, the game will end.")
    print("Let us begin . . .")

Labyrinth()
#remember that random insult generator you came up with? You should include that so that each time you enter a room it tells you something different
#i think its something about you creating the list and then randomly pulling from that list

def FirstMove():
    print("You are in the middle of a maze, trapped in a room. You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
    Door1 = input("Which door would you like to enter: North, South, or West? ")
    #count_1 = 0
    #count_1 += 1
    #count_1 += 1
    #count_1 += 1
    #count_1 += 1
    #count_1 += 1 #so this works and the function stops, but how to incorporate this into the rest of the function?
    #if count_1 >= 5:
    #    return
    #print(string.count("Room5")) #Can't figure this out

    if Door1 == "North":
        print("Excellent. You chose North.")
        def North1():
            print("You enter a new room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
            Door2 = input("Which door would you like to enter: East or South?")
            #string = "Room4"
            #print(string.count("Room4"))
            if Door2 == "East":
                print("You choose East. You enter a new room. You feel a chilly wind brush against the back of your neck. \n You look around the room. \n On the North wall, there is no door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                Door8 = input("Which door would you like to enter: South or West?")
                if Door8 == "South":
                    print("You choose South. The door creaks loudly as you push it open. \n You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                    Door9 = input("Which door would you like to enter: North or South?")
                    if Door9 == "North":
                        print("You choose North. Yay10")
                    else:
                        print("You choose South. You enter a new room. \n You look around the room. \n On the North wall, there is a door. \n on the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                        Door10 = input("Which door would you like to enter: North or South?")
                        if Door10 == "North":
                            print("You choose North. Yay11")
                        else:
                            print("You choose South. As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                            print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
#END GAME
                else:
                    print("You chose West. Yay8")
                #morehere
            else:
                print("You choose South. You re-enter the starting room.")
                #if string.count == 5:
                #    return (string.count)
                #print(string.count("Room5"))
                print("You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                Door3 = input("Which door would you like to enter: North, South, or West?")
                if Door3 == "North":
                    #Room5 = 2
                    #Room4 = 2
                    print("You enter a room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                    Door7 = input("Which door you like to enter: East or South?")
                    if Door7 == "South":
                        print("You re-enter the starting room.")
                        #Room5 = 3
                        print("You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                        Door4 = input("Which door would you like to enter: North, South, or West?")
                        if Door4 == "North":
                            print("You enter a room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                            Door5 = input("Which door would you like to enter: East or South?")
                            if Door5 == "South":
                                #Room5 = 4
                                print("You re-enter the starting room. This is the last time you will be allowed back in this room.")
                                print("You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                                Door6 = input("Which door would you like to enter: North, South, or West?")
                                if Door6 == "North":
                                    print("You enter a room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                                    Door7 = input("Which door would you like to enter: East or South?")
                                    if Door7 == "South":
                                        print("You re-enter the starting room.")
                                        #Room5 = 5
                                        print(" ... G ... \n .... A .... \n ..... M ..... \n ...... E ...... \n ... O ... \n .... V .... \n ..... E ..... \n ...... R ...... ")
                                        print("Thanks for playing!")
#GAME OVER
#I think I stopped over here??
                elif Door3 == "West":
                    print("Yay7")
                else:
                    print("Yay8")
        North1()

    elif Door1 == "South":
        print("Wonderful. You chose South.")
        def South1():
            #Room6
            print("You enter a new room. It smells faintly of cinnamon.")
            print("You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is no door. \n On the West wall, there is a door.")
            Door11 = input("Which door would you like to enter: North or West?")
            if Door11 == "North":
                print("Yay13")
            else:
                #Room1
                print("You choose West. You enter a new room. \n You look around the room. \n On the North Wall, there is a door. \n On the East wall, there is a door. \n On the South wall, there is no door. \n On the West wall, there is no door.")
                Door12 = input("Which door would you like to enter: North or East?")
                if Door12 == "North":
                    print("You choose North. You enter a new room.")
                    #Room2
                    print("You look around the room. There is a large stain above the North wall that drips into the crevice between the top of the door and the wall... \n On the North wall, there is a door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                    Door13 = input("Which door would you like to enter: North, East, or South?")
                    if Door13 == "North":
                        #Room3
                        print("You choose North. You enter a new room.")
                        print("You look around the room. \n On the North wall, there is no door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                        DeadorAlive = input("Would you like to stay in the room or return to the previous room? Enter: 'Stay' OR 'Go'")
                        if DeadorAlive == "Stay":
                            print("As you wait in the room, the stain creeps in from the other room. You watch as the walls crumble to reveal darkness all around you. Soon enough, the floor crumbles and you fall into the abyss.")
                            print(" ... G ... \n .... A .... \n ..... M ..... \n ...... E ...... \n ... O ... \n .... V .... \n ..... E ..... \n ...... R ...... ")
                            print("Thanks for playing!")
#GAME OVER
                        else:
                            print("You re-enter the previous room.")
                            #Room2
                    elif Door13 == "East":
                        print("You re-enter the starting room.")
                        #Room5
                        print("You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                        Door14 = input("Which door would you like to enter: North, South, or West?")
                        if Door14 == "North":
                            print("Excellent. You chose North.")
                            def North2():
                                print("You enter a new room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                                Door2 = input("Which door would you like to enter: East or South?")
                                #string = "Room4"
                                #print(string.count("Room4"))
                                if Door2 == "East":
                                    print("You choose East. You enter a new room. You feel a chilly wind brush against the back of your neck. \n You look around the room. \n On the North wall, there is no door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                                    Door8 = input("Which door would you like to enter: South or West?")
                                    if Door8 == "South":
                                        print("You choose South. The door creaks loudly as you push it open. \n You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                                        Door9 = input("Which door would you like to enter: North or South?")
                                        if Door9 == "North":
                                            print("You choose North. Yay10")
                                        else:
                                            print("You choose South. You enter a new room. \n You look around the room. \n On the North wall, there is a door. \n on the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                                            Door10 = input("Which door would you like to enter: North or South?")
                                            if Door10 == "North":
                                                print("You choose North. Yay11")
                                            else:
                                                print("You choose South. As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
#END GAME
                                    else:
                                        print("You chose West. Yay8")
                                    #morehere
                                else:
                                    print("You choose South. You re-enter the starting room.")
                #if string.count == 5:
                #    return (string.count)
                #print(string.count("Room5"))
                                    print("You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                                    Door3 = input("Which door would you like to enter: North, South, or West?")
                                    if Door3 == "North":
                    #Room5 = 2
                    #Room4 = 2
                                        print("You enter a room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                                        Door7 = input("Which door you like to enter: East or South?")
                                        if Door7 == "South":
                                            print("You re-enter the starting room.")
                        #Room5 = 3
                                            print("You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                                            Door4 = input("Which door would you like to enter: North, South, or West?")
                                            if Door4 == "North":
                                                print("You enter a room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                                                Door5 = input("Which door would you like to enter: East or South?")
                                                if Door5 == "South":
                                #Room5 = 4
                                                    print("You re-enter the starting room. This is the last time you will be allowed back in this room.")
                                                    print("You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
                                                    Door6 = input("Which door would you like to enter: North, South, or West?")
                                                    if Door6 == "North":
                                                        print("You enter a room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
                                                        Door7 = input("Which door would you like to enter: East or South?")
                                                        if Door7 == "South":
                                                            print("You re-enter the starting room.")
                                        #Room5 = 5
                                                            print(" ... G ... \n .... A .... \n ..... M ..... \n ...... E ...... \n ... O ... \n .... V .... \n ..... E ..... \n ...... R ...... ")
                                                            print("Thanks for playing!")
#GAME OVER
                                    elif Door3 == "West":
                                        print("Yay7")
                                    else:
                                        print("Yay8")
                            North2()
                        elif Door14 == "South":
                            print("Yay19")
                        else: #West
                            print("Yay20")
            
                    #else:
                     #   print("Yay18") #South
                        #Room1 ; count += 1
                #else:
                 #   print("Yay15")
        South1()

    else:
        print("Fantastic. You chose West.")
        def West1():
            print("Yay3")
        West1()
FirstMove()
