list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
sorted_list = []
even = []
new_list = []

def sort_odd_even(list):
    for num in list:
        if (num % 2 == 0):
            even.append(num)
        else: sorted_list.append(num)
new_list = sorted_list + even
print(new_list)


print(sort_odd_even(list_of_numbers))

