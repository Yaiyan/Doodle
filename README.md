# Doodle

Doodle is a simple games library created for python. It's uses the pygame library to let you build awesome games really easily in just a few lines of code.

When I first learnt to program, all I wanted to do was make games. Making games is hard! Pygame is pretty simple, but there's still some weird things you need to learn, and it took me ages to actually be able to make a game with it. I want to make making games easy, and that's why I've made Doodle - it hides the weird stuff for you, allowing you to concentrate on the fun parts.

For an example game made using Doodle, look at snake.py. It's fairly well commented, but if you *really* don't understand anything, open an issue on github and I'll take a look at trying to simplify it. You may also find it helpful looking at the lists below - they name all the functions and variables in Doodle.

## Functions

* **make_window**(*x_size*, *y_size*) - Creates a window for drawing on
* **load**(*location*) - Loads an image
* **draw_picture**(*picture*, *position*) - Draws a picture on the screen
* **draw_box**(*colour*, *size*, *position*) - Draws a box on the screen
* **fill**(*colour*) - Fills the screen with colour
* **write**(*text*, *position*, *colour*) - Writes some text on the screen. By default the colour is white
* **keydown**(*key*) - Tells you if a key is pressed or not
* **rand**(*lower*, *upper*) - Gives a random number between the upper and lower limits
* **get_fps**() - Tells you the fps
* **done**() - Gives you a basic program loop
* **stop**() - Quits the program
* **next_frame**() - Does all the loop logic for you. Gives you a lot more control than **done**()

## Variables

*Warning: These are all cases sensitive*

Colours:

* "red"
* "green"
* "blue"
* "yellow"
* "black"
* "white"

Keys:

* "a"
* "b"
* "c"
* "d"
* "e"
* "f"
* "g"
* "h"
* "i"
* "j"
* "k"
* "l"
* "m"
* "n"
* "o"
* "p"
* "q"
* "r"
* "s"
* "t"
* "u"
* "v"
* "w"
* "x"
* "y"
* "z"
* "right"
* "left"
* "up"
* "down"
* "spacebar"
* "escape"

## Requirements

* Python 2
* Pygame

It should work on Python 3, but this hasn't been tested.

## I've made a bunch of games in Doodle! What now?

Good job! Now it's time to move on from Doodle, and use a big game library so you have more control and can do cooler stuff! I recommend using Pygame (www.pygame.org), since it's really simple to learn, and it's what Doodle is based on.

Maybe you want to learn to make web-games? For that you need to learn something new called Javascript. For this I highly recommend Codecademy (http://www.codecademy.com). It's a great website for learning to program, and the Javascript section will teach you everything you need to know to make a game (as long as you're prepared to experiment!)