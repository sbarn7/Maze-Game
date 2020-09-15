def MazeGame3():
#index   
    def Room1():
        print("You enter a room. You look around the room. \n On the North wall, there is a door. \n On the East wall, there is a door. \n On the South wall, there is no door. \n On the West wall, there is no door.")
        print("Which door would you like to enter: North or East?") 
    #Room1()
    def Room2():
        print("You enter a room. You look around the room. \n On the North wall, there is a door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
        print("Which door would you like to enter: North, East, or South?")
    #Room2()
    def Room3():
        print("You enter a room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
        print("You may go back to the previous room or wait here. Which do you pick: Stay or Go? ")
    #Room3()
    def Room4():
        print("You enter a room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is a door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
        print("Which door would you like to enter: East or South?")
    #Room4()
    def Room5():
        print("You enter a room. You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
        print("Which door would you like to enter: North, South, or West?")
    #Room5()
    def Room6():
        print("You enter a room. You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is no door. \n On the West wall, there is a door.")
        print("Which door would you like to enter: North or West?")
    #Room6()
    def Room7():
        print("You enter a room. You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
        print("Which door would you like to enter: North or South?")
    #Room7()
    def Room8():
        print("You enter a room. You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is no door.")
        print("Which door would you like to enter: North or South?")
    #Room8()
    def Room9():
        print("You enter a room. You look around the room. \n On the North wall, there is no door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
        print("Which door would you like to enter: South or West?")
    #Room9()

#game
    print("Welcome to Maze Game. You are trapped in a maze. Can you find the way out? \n Instructions: \n 1) You start in a room. You will have the opportunity to investigate all walls. From there, you must decide which door to enter. \n 2) If you go back into the same room five times, the game will end. \n 3) Make sure to enter all keywords with a capital starting letter; ex: 'Yes' \n Let us begin . . .")
    print("You are in the middle of a maze, trapped in a room. You look around the room. \n On the North wall, there is a door. \n On the East wall, there is no door. \n On the South wall, there is a door. \n On the West wall, there is a door.")
    print("Which door would you like to enter: North, South, or West?")
    Door1 = input(" ")
    if Door1 == "North":
        Room4()
        Door2 = input(" ")
        if Door2 == "East":
            Room9()
            Door3 = input(" ")
            if Door3 == "South":
                Room8()
                Door4 = input(" ")
                if Door4 == "North":
                    Room9()
                    #INCR COUNT FOR ROOM 9
                    Door5 = input(" ")
                    if Door5 == "West":
                        Room4()
                        #INCR COUNT FOR ROOM 4
                    else: #South
                        Room8()
                        Door6 = input(" ")
                        if Door6 == "South":
                            Room7()
                            Door7 = input(" ")
                            if Door7 == "North":
                                Room8()
                                #INCR COUNT FOR ROOM 8
                                Door8 = input(" ")
                                if Door8 == "South":
                                    Room7()
                                    #INCR COUNT FOR ROOM 7
                                    Door9 = input(" ")
                                    if Door9 == "North":
                                        Room8()
                                        #INCR COUNT FOR ROOM 8
                                    else: #South
                                        print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                        print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                else: #North
                                    Room9()
                                    #INCR COUNT FOR ROOM 9
                            else: #South
                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")

                        else: #North
                            Room9()
                            #INCR COUNT FOR ROOM 9
                else: #South
                    Room7()
                    Door5 = input(" ")
                    if Door5 == "North":
                        Room8()
                        #COUNT FOR ROOM 8 INCR BY 1
                        Door6 = input(" ")
                        if Door6 == "North":
                            Room9()
                            Door8 = input(' ')
                            if Door8 == "West":
                                Room4()
                                Door11 = input(" ")
                                if Door11 == "South":
                                    Room5()
                                    Door12 = input(" ")
                                    if Door12 == "North":
                                        Room4()
                                        Door13 = input(" ")
                                        if Door13 == "East":
                                            Room9()
                                            Door14 = input(" ")
                                            if Door14 == "South":
                                                Room8()
                                                Door15 = input(" ")
                                                if Door15 == "South":
                                                    Room7()
                                                    Door16 = input(" ")
                                                    if Door16 == "South":
                                                        print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                        print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                    else: #north
                                                        Room8()
                                                else: #North
                                                    Room9()
                                            else: #West
                                                Room4()
                                        else: #South
                                            Room5()
                                    elif Door12 == "West":
                                        Room2()
                                        Door17 = input(" ")
                                        if Door17 == "East":
                                            Room5()
                                            Door18 = input(" ")
                                            if Door18 == "North":
                                                Room4()
                                                Door19 = input(" ")
                                                if Door19 == "East":
                                                    Room9()
                                                    Door20 = input(" ")
                                                    if Door20 == "South":
                                                        Room8()
                                                        Door21 = input(" ")
                                                        if Door21 == "South":
                                                            Room7()
                                                            Door22 = input(" ")
                                                            if Door22 == "South":
                                                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                            else: #North
                                                                Room8()
                                                        else: #North
                                                            Room9()

                                                    else: #West
                                                        Room4()
                                                else: #South
                                                    Room5()
                                            elif Door18 == "South":
                                                Room6()
                                            else: #West
                                                Room2()
                                        elif Door17 == "North":
                                            Room3()
                                            Door18 = input(" ")
                                            if Door18 == "Stay":
                                                print("As you wait in the room, a stain creeps in from the other room. You watch as the walls crumble to reveal darkness all around you. Soon enough, the floor crumbles and you fall into the abyss.")
                                                print(" ... G ... \n .... A .... \n ..... M ..... \n ...... E ...... \n ... O ... \n .... V .... \n ..... E ..... \n ...... R ...... ")
                                                print("Thanks for playing!")
                                            else: #Go
                                                Room2()
                                                Door32 = input(" ")
                                                if Door32 == "North":
                                                    Room3()
                                                elif Door32 == "East":
                                                    Room5()
                                                else: #South
                                                    Room1()
                                                    Door33 = input(" ")
                                                    if Door33 == "North":
                                                        Room2()
                                                    else: #East
                                                        Room6()
                                                        Door34 = input(" ")
                                                        if Door34 == "North":
                                                            Room5()
                                                            Door35 = input(" ")
                                                            if Door35 == "North":
                                                                Room4()
                                                                Door36 = input(" ")
                                                                if Door36 == "East":
                                                                    Room9()
                                                                    Door37 = input(" ")
                                                                    if Door37 == "South":
                                                                        Room8()
                                                                        Door38 = input(" ")
                                                                        if Door38 == "South":
                                                                            Room7()
                                                                            Door39 = input(" ")
                                                                            if Door39 == "South":
                                                                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")                                         
                                                                            else: #North
                                                                                Room8()
                                                                        else: #North
                                                                            Room9()
                                                                    else: #West
                                                                        Room4()
                                                                else:#South
                                                                    Room5()
                                                            elif Door35 == "West":
                                                                Room2()
                                                            else: #South
                                                                Room6()
                                                        else: #West
                                                            Room1()
                                                #else: #South
                                                #    Room1()                      
                                        else: #South
                                            Room1()
                                            Door17 = input(" ")
                                            if Door17 == "East":
                                                Room6()
                                                Door18 = input(" ")
                                                if Door18 == "North":
                                                    Room5()
                                                    Door19 = input(" ")
                                                    if Door19 == "North":
                                                        Room4()
                                                    elif Door19 == "West":
                                                        Room2()
                                                        Door20 = input(" ")
                                                        if Door20 == "East":
                                                            Room5()
                                                            Door21 = input(" ")
                                                            if Door21 == "South":
                                                                Room6()
                                                                Door22 = input(" ")
                                                                if Door22 == "West":
                                                                    Room1()
                                                                    Door23 = input(" ")
                                                                    if Door23 == "North":
                                                                        Room2()
                                                                        Door24 = input(" ")
                                                                        if Door24 == "East":
                                                                            Room5()
                                                                            Door25 = input(" ")
                                                                            if Door25 == "North":
                                                                                Room4()
                                                                                Door26 = input(" ")
                                                                                if Door26 == "East":
                                                                                    Room9()
                                                                                    Door27 = input(" ")
                                                                                    if Door27 == "South":
                                                                                        Room8()
                                                                                        Door28 = input(" ")
                                                                                        if Door28 == "South":
                                                                                            Room7()
                                                                                            Door29 = input(" ")
                                                                                            if Door29 == "South":
                                                                                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                                                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                                                            else: #North
                                                                                                Room8()
                                                                                        else: #North
                                                                                            Room9()
                                                                                    else: #West
                                                                                        Room4()
                                                                                else: #South
                                                                                    Room5()
                                                                            elif Door25 == "West":
                                                                                Room2()
                                                                            else: #South
                                                                                Room6()
                                                                        elif Door24 == "North":
                                                                            Room3()
                                                                        else: #South
                                                                            Room1()
                                                                    else: #East
                                                                        Room6()
                                                                else: #North
                                                                    Room5()
                                                            elif Door21 == "North":
                                                                Room4()
                                                            else: #West
                                                                Room2()
                                                        elif Door20 == "North":
                                                            Room3()
                                                            Door21 = input(" ")
                                                            if Door21 == "Stay":
                                                                print("As you wait in the room, a stain creeps in from the other room. You watch as the walls crumble to reveal darkness all around you. Soon enough, the floor crumbles and you fall into the abyss.")
                                                                print(" ... G ... \n .... A .... \n ..... M ..... \n ...... E ...... \n ... O ... \n .... V .... \n ..... E ..... \n ...... R ...... ")
                                                                print("Thanks for playing!")
                                                            else: #Go
                                                                Room2()
                                                                Door22 = input(" ")
                                                                if Door22 == "East":
                                                                    Room5()
                                                                    Door23 = input(" ")
                                                                    if Door23 == "South":
                                                                        Room6()
                                                                        Door24 = input(" ")
                                                                        if Door24 == "West":
                                                                            Room1()
                                                                            Door25 = input(" ")
                                                                            if Door25 == "North":
                                                                                Room2()
                                                                                Door26 = input(" ")
                                                                                if Door26 == "East":
                                                                                    Room5()
                                                                                    Door27 = input(" ")
                                                                                    if Door27 == "North":
                                                                                        Room4()
                                                                                        Door28 = input(" ")
                                                                                        if Door28 == "East":
                                                                                            Room9()
                                                                                            Door29 = input(" ")
                                                                                            if Door29 == "South":
                                                                                                Room8()
                                                                                                Door30 = input(" ")
                                                                                                if Door30 == "South":
                                                                                                    Room7()
                                                                                                    Door31 = input(" ")
                                                                                                    if Door31 == "South":
                                                                                                        print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                                                                        print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                                                                    else: #North
                                                                                                        Room8()
                                                                                                else: #North
                                                                                                    Room9()
                                                                                            else: #West
                                                                                                Room4()
                                                                                        else: #South
                                                                                            Room5()
                                                                                    elif Door27 == "West":
                                                                                        Room2()
                                                                                    else: #South
                                                                                        Room6()
                                                                                elif Door26 == "North":
                                                                                    Room3()
                                                                                else: #South
                                                                                    Room1()
                                                                            else: #East
                                                                                Room6()
                                                                        else: #North
                                                                            Room5()
                                                                    elif Door23 == "North":
                                                                        Room4()
                                                                    else: #West
                                                                        Room2()
                                                                elif Door22 == "North":
                                                                    Room3()
                                                                else: #South
                                                                    Room1()
                                                        else: #South
                                                            Room1()
                                                    else: #South
                                                        Room6()
                                                        Door20 = input(" ")
                                                        if Door20 == "West":
                                                            Room1()
                                                            Door21 = input(" ")
                                                            if Door21 == "North":
                                                                Room2()
                                                                Door22 = input(" ")
                                                                if Door22 == "East":
                                                                    Room5()
                                                                    Door23 = input(" ")
                                                                    if Door23 == "North":
                                                                        Room4()
                                                                        Door24 = input(" ")
                                                                        if Door24 == "East":
                                                                            Room9()
                                                                            Door25 = input(" ")
                                                                            if Door25 == "South":
                                                                                Room8()
                                                                                Door26 = input(" ")
                                                                                if Door26 == "South":
                                                                                    Room7()
                                                                                    Door27 = input(" ")
                                                                                    if Door27 == "South":
                                                                                        print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                                                        print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                                                    else: #North
                                                                                        Room8()
                                                                                else: #North
                                                                                    Room9()
                                                                            else: #West
                                                                                Room4()
                                                                        else: #South
                                                                            Room5()
                                                                    elif Door23 == "West":
                                                                        Room2()
                                                                    else: #South
                                                                        Room6()
                                                                elif Door22 == "North":
                                                                    Room3()
                                                                else: #South
                                                                    Room1()
                                                            else: #East
                                                                Room6()
                                                        else: #North
                                                            Room5()
                                                else: #West
                                                    Room1()
                                                    Door20 = input(" ")
                                                    if Door20 == "North":
                                                        Room2()
                                                        Door21 = input(" ")
                                                        if Door21 == "North":
                                                            Room3()
                                                        elif Door21 == "East":
                                                            Room5()
                                                            Door22 = input(" ")
                                                            if Door22 == "North":
                                                                Room4()
                                                                Door23 = input(" ")
                                                                if Door23 == "East":
                                                                    Room9()
                                                                    Door24 = input(" ")
                                                                    if Door24 == "South":
                                                                        Room8()
                                                                        Door25 = input(" ")
                                                                        if Door25 == "South":
                                                                            Room7()
                                                                            Door26 = input(" ")
                                                                            if Door26 == "South":
                                                                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                                            else: #North
                                                                                Room8()
                                                                        else: #North
                                                                            Room9()
                                                                    else: #West
                                                                        Room4()
                                                                else: #South
                                                                    Room5()
                                                            elif Door22 == "South":
                                                                Room6()
                                                            else: #West
                                                                Room2()
                                                        else: #South
                                                            Room1()
                                                    else: #East
                                                        Room6()
                                                    #Door23 = input(" ")
                                                    #if Door23 == "North":
                                                        #Room3()
                                                        #Door31 = input(" ")
                                                        #if Door31 == "Stay":
                                                        #    print("As you wait in the room, a stain creeps in from the other room. You watch as the walls crumble to reveal darkness all around you. Soon enough, the floor crumbles and you fall into the abyss.")
                                                        #    print(" ... G ... \n .... A .... \n ..... M ..... \n ...... E ...... \n ... O ... \n .... V .... \n ..... E ..... \n ...... R ...... ")
                                                        #    print("Thanks for playing!")
                                                        #else: #Go
                                                            #Room2()
                                                            #Door32 = input(" ")
                                                            #if Door32 == "North":
                                                            #    Room3()
                                                            #elif Door32 == "East":
                                                            #    Room5()
                                                            #else: #South
                                                            #    Room1()
                                                            #    Door33 = input(" ")
                                                            #    if Door33 == "North":
                                                            #        Room2()
                                                            #    else: #East
                                                            #        Room6()
                                                            #        Door34 = input(" ")
                                                            #        if Door34 == "North":
                                                            #            Room5()
                                                            #            Door35 = input(" ")
                                                            #            if Door35 == "North":
                                                            #                Room4()
                                                            #               Door36 = input(" ")
                                                            #                if Door36 == "East":
                                                            #                    Room9()
                                                            #                    Door37 = input(" ")
                                                            #                    if Door37 == "South":
                                                            #                        Room8()
                                                            #                        Door38 = input(" ")
                                                            #                        if Door38 == "South":
                                                            #                            Room7()
                                                            #                            Door39 = input(" ")
                                                            #                            if Door39 == "South":
                                                            #                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                            #                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                            #                            else: #North
                                                            #                                Room8()
                                                            #                        else: #North
                                                            #                            Room9()
                                                            #                    else: #West
                                                            #                        Room4()
                                                            #                else: #South
                                                            #                    Room5()
                                                            #            elif Door35 == "West":
                                                            #                Room2()
                                                            #            else: #South
                                                            #                Room6()
                                                            #        else: #West
                                                            #            Room1()

                                                    #elif Door23 == "East":
                                                    #    Room5()
                                                    else: #South
                                                        Room1()
                                                        Door24 = input(" ")
                                                        if Door24 == "East":
                                                            Room6()
                                                            Door25 = input(" ")
                                                            if Door25 == "North":
                                                                Room5()
                                                                Door26 = input(" ")
                                                                if Door26 == "North":
                                                                    Room4()
                                                                    Door27 = input(" ")
                                                                    if Door27 == "South":
                                                                        Room5()
                                                                    else: #East
                                                                        Room9()
                                                                        Door28 = input(" ")
                                                                        if Door28 == "South":
                                                                            Room8()
                                                                            Door29 = input(" ")
                                                                            if Door29 == "South":
                                                                                Room7()
                                                                                Door30 = input(" ")
                                                                                if Door30 == "South":
                                                                                    print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                                                    print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                                                else: #North
                                                                                    Room8()
                                                                            else: #North
                                                                                Room9()
                                                                        else: #West
                                                                            Room4()
                                                                elif Door26 == "West":
                                                                    Room2()
                                                                else: #South
                                                                    Room6()
                                                            else: #West
                                                                Room1()
                                                        else: #North
                                                            Room2()
                                            else: #North
                                                Room2()
                                                Door19 = input(" ")
                                                if Door19 == South:
                                                    Door1()
                                                elif Door19 == "East":
                                                    Room5()
                                                    Door20 = input(" ")
                                                    if Door20 == "North":
                                                        Room4()
                                                        Door21 = input(" ")
                                                        if Door21 == "East":
                                                            Room9()
                                                            Door22 = input(" ")
                                                            if Door22 == "South":
                                                                Room8()
                                                                Door23 = input(" ")
                                                                if Door23 == "South":
                                                                    Room7()
                                                                    Door24 = input(" ")
                                                                    if Door24 == "South":
                                                                        print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                                        print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                                    else: #North
                                                                        Room8()
                                                                else: #North
                                                                    Room9()
                                                            else: #West
                                                                Room4()
                                                        else: #South
                                                            Room5()
                                                    elif Door20 == "West":
                                                        Room2()
                                                    else: #South
                                                        Room6()
                                                else: #North
                                                    Room3()
                                        else: #North
                                            Room5()
                                            Door18 = input(" ")
                                            if Door18 == "North":
                                                Room4()
                                                Door19 = input(" ")
                                                if Door19 == "East":
                                                    Room9()
                                                    Door20 = input(" ")
                                                    if Door20 == "South":
                                                        Room8()
                                                        Door21 = input(" ")
                                                        if Door21 == "South":
                                                            Room7()
                                                            Door22 = input(" ")
                                                            if Door22 == "North":
                                                                Room8()
                                                            else: #South
                                                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                                        else: #North
                                                            Room9()
                                                    else: #West
                                                        Room4()
                                                else: #South
                                                    Room5()
                                            elif Door18 == "West":
                                                Room2()
                                            else: #South
                                                Room6()
                                else: #East
                                    Room9()
                                    Door12 = input(" ")
                                    if Door12 == "West":
                                        Room4()
                                    else: #South
                                        Room8()
                                        Door13 = input(" ")
                                        if Door13 == "North":
                                            Room9()
                                        else: #South
                                            Room7()
                                            Door14 = input(" ")
                                            if Door14 == "North":
                                                Room8()
                                            else: #South
                                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")

                            else: #South
                                Room8()
                                Door9 = input(" ")
                                if Door9 == "South":
                                    Room7()
                                    Door10 = input(" ")
                                    if Door10 == "North":
                                        Room8()
                                    else: #South
                                        print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                        print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                                else: #North
                                    Room9()
                
                        else: #South
                            Room7()
                            Door7 = input(" ")
                            if Door7 == "North":
                                Room8()
                            else: #South
                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
                    else: #South
                        print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                        print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")
            else: #West from Room 9
                Room4()
                #COUNT FOR ROOM 4 INCR BY 1
                Door12 = input(" ")
                if Door12 == "East":
                    Room9()
                    #INCR COUNT FOR ROOM 9
                    Door13 = input(" ")
                    if Door13 == "South":
                        Room8()
                    else: #West
                        Room4()
                        #INCR COUNT FOR ROOM 4
                        Door14 = input(" ")
                        if Door14 == "East":
                            Room9()
                            #INCR COUNT FOR ROOM 9
                            Door15 = input(" ")
                            if Door15 == "West":
                                Room4()
                                #INCR COUNT FOR ROOM 4
                                Door16 = input(" ")
                                if Door16 == "East":
                                    Room9()
                                    Door17 = input(" ")
                                    if Door17 == "West":
                                        print("Oh no, you've entered this room too many times.")
                                        print(" ... G ... \n .... A .... \n ..... M ..... \n ...... E ...... \n ... O ... \n .... V .... \n ..... E ..... \n ...... R ...... ")
                                        print("Thanks for playing!")
                                    else: #South
                                        Door8()
                            else: #South
                                Room8()
                        else: #West
                            Room4()
                            #INCR COUNT FOR ROOM 4
                            Door15 = input(" ")
                            if Door15 == "East":
                                Room9()
                                #INCR COUNT FOR ROOM 9

                            else: #South
                                Room5()
                                #INCR COUNT FOR ROOM5
                else: #South
                    Room5()
                    #INCR COUNT FOR ROOM 5
        else: #North--> South-->
            Room5()
            #COUNT FOR ROOM 5 INCR BY 1
            Door6 = input(" ")
            if Door6 == "North":
                Room4()
                #COUNT FOR ROOM 4 INCR BY 1
                Door8 = input(" ")
                if Door8 == "East":
                    Room9()
                    Door9 = input(" ")
                    if Door9 == "South":
                        Room8()
                        Door10 = input(" ")
                        if Door10 == "North":
                            Room9()
                            #COUNT FOR ROOM 9 INCR BY 1
                        else: #South
                            Room7()
                            Door11 = input(" ")
                            if Door11 == "North":
                                Door8()
                                #COUNT FOR ROOM 8 INCR BY 1
                            else: #South
                                print("As you push open the door, you are greeted by a bright light and the loud chirping of birds overhead. As you look around, you see dense forest surrounding you. \n How did you get into this jungle? And how will you escape?")
                                print("Find out next time with Jungle Game. \n Thanks for playing! We hope you enjoyed the maze.")

                    else: #West
                        Room4()
                        #COUNT FOR ROOM 4 INCR BY 1
                else: #South
                    Room5() 
                    #COUNT FOR ROOM 5 INCR BY 1
            elif Door6 == "South":
                Room6()
                Door7 = input(" ")
                if Door7 == "North":
                    Room5()
                else: #West
                    Room1()
            else: #West
                Room2()

    elif Door1 == "South":
        Room6()
    else: #West from OG Room
        Room2()
        Door10 = input(" ")
        if Door10 == "North":
            Room3()
        elif Door10 == "East":
            Room5()
            #INCR COUNT FOR ROOM5
        else: #South
            Room1()
    
    
MazeGame3()
