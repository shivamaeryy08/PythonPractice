import math
import random as r


def generate_random_angle():
    while True:
        x = r.uniform(-1 * (math.sqrt(3) / 2), (math.sqrt(3) / 2))
        if x == 0.0:
            continue
        y = r.uniform(-1 * (math.sqrt(3) / 2), (math.sqrt(3) / 2))
        angle = math.degrees(math.atan2(y, x))
        invalid_pos_angle = 80 <= angle <= 100 or 250 <= angle <= 290
        invalid_neg_angle = -80 <= angle <= -100 or -250 <= angle <= -290
        if not (invalid_neg_angle or invalid_pos_angle):
            print(angle)


for i in range(5):
    generate_random_angle()
