import math
import random as r


def generate_random_angle():
    x = r.uniform(-1 * (math.sqrt(3) / 2), (math.sqrt(3) / 2))
    y = r.uniform(-1 * (math.sqrt(3) / 2), (math.sqrt(3) / 2))
    angle = math.degrees(math.atan2(y, x))

    print(angle)


for i in range(20):
    generate_random_angle()
