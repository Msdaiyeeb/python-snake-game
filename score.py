from turtle import Turtle


class Score(Turtle):
    def __init__(self, high_score):
        super().__init__()
        self.hideturtle()
        self.color("yellow")
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        self.high_score = high_score
        self.write(f"Score : {self.score}        High score : {self.high_score}", move=False, align="center", font=("Fantasy", 14, "normal"))

    def point_increment(self, increase):
        if increase:
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
            self.clear_score_board()
    def clear_score_board(self):
        self.clear()
        self.write(f"Score : {self.score}        High score : {self.high_score}", move=False, align="center", font=("Fantasy", 14, "normal"))

    def change_snake_color(self,increase, animal, nutrient):
        if increase:
            for num in range(0, len(animal.my_snakes)):
                animal.my_snakes[num].color(nutrient.color()[0])

    def game_over(self,score,screen,time):
        screen.tracer(0)
        screen.clear()
        screen.bgcolor("black")
        self.setposition(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Fantasy", 40, "normal"))
        if self.score == self.high_score:
            score.setposition(0, 100)
            score.write(f"Score : {score.score}   New high score : {self.high_score}", move=False, align="center", font=("Fantasy", 14, "normal"))
            with open("High score.txt", "w") as file:
                file.write(str(self.high_score))
        else:
            score.setposition(0, 100)
            score.write(f"Score : {score.score}", move=False, align="center", font=("Fantasy", 14, "normal"))
        time.sleep(0.1)
        screen.update()

