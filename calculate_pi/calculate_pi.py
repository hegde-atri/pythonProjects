import random
import time

def calculate_pi(i):

    num_point_circle = 0
    num_point_total = 0

    for _ in range(i):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2 #distance between the origin and the coordinate x,y

        if distance <= 1: #if it is inside the radius of the circle or outside.
            num_point_circle += 1

        num_point_total += 1
    #re arrangement of the  a=pi * r **2 formula to give us the value of pi

    return 4 * (num_point_circle / num_point_total)

tic = time.perf_counter()
print(calculate_pi(200_000_000))
toc = time.perf_counter()
print(f"Time taken: {toc - tic:0.4f} seconds.")
# run calculate_pi(n) where n is the number of iterations;
# the more the number of iterations, the closer to the value of pi
