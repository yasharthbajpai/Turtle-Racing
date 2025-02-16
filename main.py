"""
Title          : Turtle Racing Game
Author         : Yasharth Bajpai
Created        : 10th January 2025
Last Modified  : 16th February 2025
Version        : 1.0

Description    : A graphical turtle racing game where players can choose the number of racers
                 and watch them compete in a randomized race to the finish line.

Dependencies   : 
    - Python 3.x
    - turtle module
    - time module
    - random module

Usage          : Run the script to start the game. Follow prompts to:
                 1. Enter the number of racers (2-10)
                 2. Watch the race unfold
                 3. See which turtle wins

Features       :
    - Customizable number of racers (2-10)
    - Colorful turtle racers
    - Randomized movement for unpredictable races
    - Visual race track using the turtle graphics window

Game Rules     :
    - Players select the number of turtle racers
    - Turtles move forward randomly each turn
    - The first turtle to reach the top of the screen wins
    - Race results are displayed in the console

License        : Creative Commons Zero v1.0 Universal

Copyright (c) [2025] [Yasharth Bajpai]
"""


import turtle
import time
import random

WIDTH, HEIGHT = 1000, 700
color = ["Red", "Blue", "Green", "Orange", "Purple", "Pink", "Yellow", "Brown", "Black", "Cyan", "Magenta"]




def get_number_of_racers():
    racers  = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try again!")




def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")



def create_turtles(colors,racers):
    turtles = []
    for i ,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * (WIDTH // (racers + 1)), -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles



def race(colours, racers):
    init_turtle()
    turtles  = create_turtles(colours, racers)

    while True:
        for racer in turtles:
            move = random.randint(1, 10)
            racer.forward(move)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 20:
                print(colours[turtles.index(racer)] + " wins!")
                return
            


def main():
    random.shuffle(color)
    racers = get_number_of_racers()
    colours = color[:racers]
    race(colours, racers)
    time.sleep(2)




if __name__ == "__main__":
    main()
