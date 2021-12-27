# bounce.py
#
# Exercise 1.5

ball_bounce = 0
ball_height = 100

while ball_bounce < 10:
    ball_height *= 0.6
    ball_bounce += 1
    print(ball_bounce, round(ball_height, 4))