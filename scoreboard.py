from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 15, "bold")
with open("data.text") as file:
    contents = int(file.read())


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = contents
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High score : {self.highscore}", align=ALIGN, font=FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.text", mode= "w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_score()

        # def game_over(self):

    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
