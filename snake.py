from doodle import *

# A function to add a berry to the screen
def add_berry(berries, snake):
    # First try and place the berry randomly
    new_berry = [rand(0,31), rand(0,23)]
    
    # If it's hitting the snake, or another berry, move it
    while new_berry in berries or new_berry in snake:
        new_berry = [rand(0,31), rand(0,23)]
    
    # When it's a good place, add it to the list of berries!
    berries.append(new_berry)


# Directions
RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)

# Load the images
berry_image = load("berry.png")
snake_image = load("snake.png")
head_image = load("head.png")
rotated_head_image = head_image

# Create our snake and berries
snake = [[3,5],[4,5],[5,5],[6,5]]
berries = [[rand(0,31), rand(0,23)]]
add_berry(berries, snake)

# Keep track of the score
score = 0

# The direction the snake is travelling in
direction = (1, 0)
last_direction = direction

# These help us keep control of time
time_since_update = 0
game_speed = 0.3

# Finally make the window
make_window(640,480)

while True:
    # If fps is 0, we will be dividing by 0
    # This is bad, so make sure the fps is over 0
    if get_fps() > 0:
        # This tells us how many seconds have passed since the last loop
        time_since_update += 1.0 / get_fps()
    
    # Check for input from the player
    # We check the last direction so going the opposite direction
    # doesn't kill you!
    if keydown("left") and last_direction != RIGHT:
        direction = LEFT
        rotated_head_image = rotate_picture(head_image, 180)
    elif keydown("right") and last_direction != LEFT:
        direction = RIGHT
        rotated_head_image = rotate_picture(head_image, 0)
    elif keydown("up") and last_direction != DOWN:
        direction = UP
        rotated_head_image = rotate_picture(head_image, 90)
    elif keydown("down") and last_direction != UP:
        direction = DOWN
        rotated_head_image = rotate_picture(head_image, 270)
    
    
    # Draw the world, and write the score
    fill("green")
    write("Score: "+str(score), (20, 20), "black")
    
    # Draw each snake segment in turn
    # We miss the last segment as this is the head, which we want to draw separately
    for segment in snake[:-1]:
        segment_x = segment[0] * 20
        segment_y = segment[1] * 20
        
        draw_picture(snake_image, (segment_x, segment_y))
    
    # Draw the head
    segment_x = snake[-1][0] * 20
    segment_y = snake[-1][1] * 20
    
    draw_picture(rotated_head_image, (segment_x, segment_y))
    
    
    # And the same for the berries
    for berry in berries:
        berry_x = berry[0] * 20
        berry_y = berry[1] * 20
        
        draw_picture(berry_image, (berry_x, berry_y))
    
    
    # Move the snake, but only when enough time has passed
    if time_since_update > game_speed:
        # Find the position in front of the snake
        new_segment = [snake[-1][0] + direction[0],
                       snake[-1][1] + direction[1]]
        
        # Check the snake didn't hit itself!
        if new_segment not in snake[1:]:
            # Check the snake hasn't gone off the side of the screen
            if new_segment[0] >= 0 and new_segment[0] <= 31:
                # And make sure it hasn't gone off the top or bottom
                if new_segment[1] >= 0 and new_segment[1] <= 23:
                    snake.append(new_segment)
                    
                    # Check if we hit a berry
                    if new_segment not in berries:
                        # If we didn't, don't grow!
                        snake.pop(0)
                    else:
                        # If we did, add a new berry and remove the old one
                        add_berry(berries, snake)
                        berries.remove(new_segment)
                        
                        score += 1
                    
                    # We want to make the game faster if they hit a snake
                    game_speed = 1.5 / len(snake)
                else:
                    stop()
            else:
                stop()
        else:
            stop()
        
        # We updated now, so set the time to 0
        time_since_update = 0
        last_direction = direction
        
    next_frame()