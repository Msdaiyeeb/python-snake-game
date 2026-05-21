from turtle import Screen
from score import Score
from snake import Snake
from food import Food
import time

with open("High score.txt", "r") as file:
    for line in file:
        high_score = int(line)
my_screen = Screen()

my_screen.setup(width = 600, height = 600)
my_screen.bgcolor("black")
my_screen.title("Snake game")
my_screen.tracer(0)
my_screen.listen()

snake = Snake()
food = Food()
score = Score(high_score)



my_screen.onkey(key='Up',fun=snake.move_up)
my_screen.onkey(key='Down',fun=snake.move_down)
my_screen.onkey(key='Right',fun=snake.move_right)
my_screen.onkey(key='Left',fun=snake.move_left)


is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    point = food.check_food_collision(food,snake)
    if point:
        snake.add_square()
        score.change_snake_color(point, snake, food)
        food.gen_food()

    score.point_increment(point)


    if snake.my_snakes[0].position()[0] > 290 or snake.my_snakes[0].position()[0] < -290 or snake.my_snakes[0].position()[1] > 290 or snake.my_snakes[0].position()[1] < -290 :
        if snake.my_snakes[0].position()[0] > 290:
            snake.my_snakes[0].teleport(-(snake.my_snakes[0].position()[0]), snake.my_snakes[0].position()[1])
        elif snake.my_snakes[0].position()[0] < -290:
            snake.my_snakes[0].teleport(-(snake.my_snakes[0].position()[0]), snake.my_snakes[0].position()[1])
        elif snake.my_snakes[0].position()[1] > 290:
            snake.my_snakes[0].teleport(snake.my_snakes[0].position()[0], -(snake.my_snakes[0].position()[1]))
        elif snake.my_snakes[0].position()[1] < -290:
            snake.my_snakes[0].teleport(-(snake.my_snakes[0].position()[0]), -(snake.my_snakes[0].position()[1]))

    for ___ in snake.my_snakes[1:len(snake.my_snakes)-1]:
        if snake.my_snakes[0].distance(___) < 15:
            score.game_over(score, my_screen, time)
            is_game_on = False


my_screen.exitonclick()
