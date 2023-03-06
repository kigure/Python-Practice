import random

lucky = random.randint(1, 10)

# if lucky == 1:
#     print("You are lucky")
# else:

while lucky != 1:
    print(lucky)
    lucky = random.randint(1, 10)
print("おめでとう")
