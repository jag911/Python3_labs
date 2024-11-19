import random

balls = []
while len(balls) < 6:
    num = random.randint(1,50)
    if num in balls:
        print(f"duplicate {num}")
    else:
        balls.append(num)

print(f" Lotto numbers are: {balls}")