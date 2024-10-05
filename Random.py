import random


list = [1, 2]
result500 = random.choices(list, weights = [1000, 1], k = 500)
result = random.choices(list, weights = [2, 1], k = 1)
result2 = random.choices(list, weights = [1, 1], k = 1)
print(result)
print(result500)
if result[0] == 1:
    print("I'm right, you're wrong")
else:
    print("I'm right still, but we will go with your idea")
n = 0
for i in result500:
    if i == 1:
        n = n + 1
    else:
        print("you may be partially biased with your viewpoint, but sure we will go with your idea")
if n == 500:
    print("I am right, my opinion is objectively correct")
print(result2)