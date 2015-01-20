# Doodle

Doodle is a simple games library created for python. It's uses the pygame library to let you build awesome games really easily in just a few lines of code.

There's no real examples yet, so if you want to use it you'll have to rely on the function list below, but I'll get some examples up soon to make it easier to learn from.

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
