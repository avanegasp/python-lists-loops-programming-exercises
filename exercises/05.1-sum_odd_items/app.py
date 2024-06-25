my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
odds_list = []

def sum_odds(my_list):
    for num in my_list:
        if num % 2 != 0:
            return odds_list.append(num)

sum_odds(my_list)