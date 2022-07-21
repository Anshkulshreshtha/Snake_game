from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.highscore = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
