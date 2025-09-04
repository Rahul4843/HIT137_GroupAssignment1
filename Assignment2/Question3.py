import turtle

def draw_recursive_edge(t, length, depth):
    """
    Drawing a fractal edge by recursively modifying a line segment.

    At each recursive call:
    - Splitting the line into three parts
    - Replacing the middle part with a triangular bump
    - Repeating the same steps for each new segment
    """
    if depth == 0:
        # Drawing a straight line when recursion ends
        t.forward(length)
    else:
        # Splitting line and inserting indentation
        segment = length / 3

        # Drawing the first segment
        draw_recursive_edge(t, segment, depth - 1)

        # Turning right to start the triangle
        t.right(60)
        # Drawing the first side of the bump
        draw_recursive_edge(t, segment, depth - 1)

        # Turning left to form the peak
        t.left(120)
        # Drawing the second side of the bump
        draw_recursive_edge(t, segment, depth - 1)

        # Returning to original direction
        t.right(60)
        # Drawing the final segment
        draw_recursive_edge(t, segment, depth - 1)

def polygon_pattern_draw(sides, side_length, recursion_depth):
    """
    Creating a geometric pattern by applying recursion to each polygon side.
    """
    # Setting up the turtle window
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title(f"Recursive Pattern: {sides} sides, depth {recursion_depth}")
    screen.setup(width=1000, height=1000)

    # Creating the turtle pen
    t = turtle.Turtle()
    t.speed(0)  # Using the fastest drawing speed
    t.color("black")
    t.pensize(1)

    # Calculating the angle between sides
    angle = 360 / sides

    # Estimating pattern growth for better centering
    growth = (4 / 3) ** recursion_depth
    size_estimate = side_length * growth

    # Positioning the turtle at a better starting location
    start_x = -size_estimate // 2 + 150
    start_y = size_estimate // 4
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    # Drawing each side of the polygon
    for _ in range(sides):
        draw_recursive_edge(t, side_length, recursion_depth)
        # Turning the turtle to align with next side
        t.right(angle)

    # Hiding the turtle and waiting for click to close
    t.hideturtle()
    screen.exitonclick()

def get_user_input():
    """
    Collecting user input for sides, side length, and recursion depth.
    """
    while True:
        try:
            sides = int(input("Enter the number of sides: "))
            if sides < 3:
                print("A polygon needs at least 3 sides.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    while True:
        try:
            side_length = int(input("Enter the side length: "))
            if side_length <= 0:
                print("Side length should be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            recursion_depth = int(input("Enter the recursion depth: "))
            if recursion_depth < 0:
                print("Depth cannot be negative.")
                continue
            if recursion_depth > 5:
                print("Warning: Please note that depths above 5 can take a long time to draw.")
                if input("Continue anyway? (y/n): ").lower() != 'y':
                    continue
            break
        except ValueError:
            print("Please enter a valid number.")

    return sides, side_length, recursion_depth

def main():
    """
    Running the main program that gathers input and draws the pattern.
    """
    print("Welcome to the Recursive Geometric Pattern Generator!")
    print("Creating detailed patterns by recursively modifying polygon edges.\n")

    # Collecting input from the user
    sides, side_length, recursion_depth = get_user_input()

    # Displaying summary before drawing
    print(f"\nDrawing a pattern with:")
    print(f"- {sides} sides")
    print(f"- Side length of {side_length} pixels")
    print(f"- Recursion depth: {recursion_depth}")
    print("\nOpening the drawing window... Click on it to close when done.\n")

    # Generating the pattern
    polygon_pattern_draw(sides, side_length, recursion_depth)

if __name__ == "__main__":
    main()
