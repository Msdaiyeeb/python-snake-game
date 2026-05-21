from turtle import Turtle
X = 0
Y = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.my_snakes = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            global X
            my_snake = Turtle()
            my_snake.penup()
            my_snake.color("white")
            my_snake.shape("square")
            my_snake.setposition(X, Y)
            X += -20
            self.my_snakes.append(my_snake)

    def move(self):
        for num in range(len(self.my_snakes) - 1, 0, -1):
            self.my_snakes[num].goto(self.my_snakes[num - 1].xcor(), self.my_snakes[num - 1].ycor())
        self.my_snakes[0].forward(20)

    def move_up(self):
        direction = self.my_snakes[0].heading()
        if direction == 0:
            self.my_snakes[0].setheading(90)
        elif direction == 180:
            self.my_snakes[0].setheading(90)

    def move_down(self):
        direction = self.my_snakes[0].heading()
        if direction == 0:
            self.my_snakes[0].setheading(270)
        elif direction == 180:
            self.my_snakes[0].setheading(270)

    def move_right(self):
        direction = self.my_snakes[0].heading()
        if direction == 90:
            self.my_snakes[0].setheading(0)
        elif direction == 270:
            self.my_snakes[0].setheading(0)

    def move_left(self):
        direction = self.my_snakes[0].heading()
        if direction == 90:
            self.my_snakes[0].setheading(180)
        elif direction == 270:
            self.my_snakes[0].setheading(180)
    def add_square(self):
        my_snake = Turtle()
        my_snake.setposition(self.my_snakes[-1].position())
        my_snake.isvisible()
        my_snake.color("black")
        my_snake.penup()
        my_snake.shape("square")
        self.my_snakes.append(my_snake)
        my_snake.color(self.my_snakes[0].color()[0])
