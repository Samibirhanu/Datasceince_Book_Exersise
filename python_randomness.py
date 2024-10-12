# randomness 
import random
random.seed(10)     # this ensures we get the same result every time

four_uniform_randoms = [random.random() for _ in range(4)]

random.seed(10)            # set the seed to 10
print(random.random())     # 0.5714...
random.seed(10)
print(random.random())     # the same random again

# random.randrange 
random.randrange(10)        # choose randomly from range(10) = [0, 1, 2,...9 ]
random.randrange(3, 6)      # choose randomly from range(3, 6) = [3, 4, 5]

# random.shuffle
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)

# randomly pick one element
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])     # "bob" for me

# choose a sample of elements without replacment
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6) # [16, 36, 10, 625, 9]
print(winning_numbers)

# choose sample element with replacemnet
four_with_replacemnet = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacemnet)        #[9, 2, 3, 9]


