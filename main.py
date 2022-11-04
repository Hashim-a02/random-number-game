import random

num = 0


def generate_random_number():
  num = random.randint(0, 99999999999999999999)
  return num


print(generate_random_number())