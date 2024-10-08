# import random module
import random
random.seed(10)  # this ensures we get the same results every time

four_uniform_randoms = [random.random() for _ in range(4)] # generates 4 random number list
print(four_uniform_randoms)    

random.seed(10)
print(random.random())

random.seed(10)
print(random.random())

# use random.randrange
random.randrange(10)                # choose randomly from range(10) = [0, 1, ...., 9]
print(random.randrange(3, 6))       # choose randomly from range(3, 6) = [3, 4, 5]

# random.shuffle randomly orders
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)           # [5, 6, 9, 2, 3, 7, 8, 4, 1, 10]
print(up_to_ten) 

# randomly pick one element from list random.choice
me_best_friend = random.choice(["Alice", "Bob", "charlie"])     # 'Bob' 
print(me_best_friend)

# choose a sample of elements without replacement/ or duplicate random.sample
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)     # [4, 15, 47, 23, 2, 26]
print(winning_numbers)

# to choose a sample element with replacement calling multiple times random.choice
four_with_replacment = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacment)
