# Imports
import turtle
import player
import car

# Objects
cars = car.Car()
player1 = player.Player()
screen = turtle.Screen()

# Hi

# Setup
screen.setup(width=800, height=450, startx=100, starty=None)

player1.seth(90)  # Set the heading to go up
player1.goto(0, -200)  # Make it go to the bottom of the Window

turtle.listen()
turtle.onkey(player1.player_forward, "space")  # Makes player go forward
turtle.onkey(player1.player_backward, "Right")  # Makes the player go back ("It's a Dev thing")

running = True  # The while loop thing
levels_beat = 0  # The amount of levels beat

while running:
    # Checking if player beat the level
    if player1.ycor() >= 215:
        levels_beat += 1
        print(levels_beat)  # FIND ~ remove pls
        player1.goto(0, -200)
