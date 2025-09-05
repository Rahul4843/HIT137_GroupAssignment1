import turtle

def draw_bumpy_line(turtle_pen, line_length, detail_level):
    """
    Drawing a bumpy line using triangle shapes.
    Increasing the detail by repeating the process at a smaller scale.
    """
    if detail_level == 0:
        # Drawing a straight line when no more detail is needed
        turtle_pen.forward(line_length)
    else:
        # Splitting the line into 3 smaller parts
        piece_length = line_length / 3

        # Drawing the first part of the line
        draw_bumpy_line(turtle_pen, piece_length, detail_level - 1)

        # Turning right to begin the bump
        turtle_pen.right(60)
        # Drawing the first side of the bump
        draw_bumpy_line(turtle_pen, piece_length, detail_level - 1)

        # Turning left to make the peak of the bump
        turtle_pen.left(120)
        # Drawing the second side of the bump
        draw_bumpy_line(turtle_pen, piece_length, detail_level - 1)

        # Turning back to original direction
        turtle_pen.right(60)
        # Drawing the final part of the line
        draw_bumpy_line(turtle_pen, piece_length, detail_level - 1)

def create_pattern(number_of_sides, side_length, detail_level):
    """
    Creating a shape with bumpy sides to make a cool pattern.
    """
    # Setting up the window
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Cool Pattern: {number_of_sides} sides, detail level {detail_level}")
    window.setup(width=1000, height=1000)

    # Creating a turtle for drawing
    pen = turtle.Turtle()
    pen.speed(0)  # Drawing as fast as possible
    pen.color("black")
    pen.pensize(1)

    # Calculating the angle to turn for each side
    turn_angle = 360 / number_of_sides

    # Estimating how big the shape will be with the detail added
    size_growth = (4 / 3) ** detail_level
    estimated_size = side_length * size_growth

    # Moving the pen to the starting position
    start_x = -estimated_size // 2 + 150
    start_y = estimated_size // 4
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()

    # Drawing each side with bumps
    for side_number in range(number_of_sides):
        draw_bumpy_line(pen, side_length, detail_level)
        # Turning to face the next side
        pen.right(turn_angle)

    # Hiding the turtle and waiting for a click to close
    pen.hideturtle()
    window.exitonclick()

def ask_user_for_settings():
    """
    Asking the user to choose the shape settings.
    """
    while True:
        try:
            sides = int(input("How many sides do you want? "))
            if sides < 3:
                print("You need at least 3 sides to make a shape.")
                continue
            break
        except ValueError:
            print("Please type a whole number.")

    while True:
        try:
            side_length = int(input("How long should each side be? "))
            if side_length <= 0:
                print("The side length needs to be bigger than 0.")
                continue
            break
        except ValueError:
            print("Please type a number.")

    while True:
        try:
            detail_level = int(input("How much detail do you want (0-5)? "))
            if detail_level < 0:
                print("Detail level can't be negative.")
                continue
            if detail_level > 5:
                print("Warning: High detail levels take a long time to draw.")
                if input("Do you want to continue anyway? (y/n): ").lower() != 'y':
                    continue
            break
        except ValueError:
            print("Please type a number.")

    return sides, side_length, detail_level

def start_program():
    """
    Starting the program and drawing the pattern.
    """
    print("Welcome to the Cool Pattern Maker!")
    print("This program creates awesome patterns with bumpy, detailed edges.\n")

    # Asking the user for input
    sides, side_length, detail_level = ask_user_for_settings()

    # Showing the settings to the user
    print(f"\nI'm going to draw a pattern with:")
    print(f"- {sides} sides")
    print(f"- Each side {side_length} pixels long")
    print(f"- Detail level: {detail_level}")
    print("\nOpening the drawing window now... Click on it to close when you're done looking!\n")

    # Creating the pattern
    create_pattern(sides, side_length, detail_level)

# Starting the program
start_program()
