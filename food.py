import random
from turtle import Turtle
food_color = ["red","blue","orange"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color(random.choice(food_color))
        self.speed("fastest")
        self.refresh_food()


    def refresh_food(self):
        self.color(random.choice(food_color))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)


