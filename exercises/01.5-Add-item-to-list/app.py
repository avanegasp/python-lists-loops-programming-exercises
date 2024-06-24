# Remember to import random function here
import random

my_list = [4, 5, 734, 43, 45]

# The magic goes below

for num in range(10):
    random_num = random.randint(1,20)
    my_list.append(random_num)

print(my_list)