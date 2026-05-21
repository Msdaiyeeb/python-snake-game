from turtle import Turtle
#from snake import Snake
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.my_colors = ["blue", "purple", "yellow", "green"]
        self.speed(0)
        self.penup()
        self.shapesize(0.5)
        self.setposition(random.randint(-280, 280), random.randint(-280, 280))
        self.shape("circle")
        self.color(random.choice(self.my_colors))

    def gen_food(self):
        self.color(random.choice(self.my_colors))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def check_food_collision(self,nutrient,animal):
        if animal.my_snakes[0].distance(nutrient) < 15:
            return True

