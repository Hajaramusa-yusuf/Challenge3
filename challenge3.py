import random

hat = [1,2,4,8,16,32,64]

# since k = 1, 2, ..., 7.
# we will initilaze all the numbers in the list to use 2^k-1 staring from k=1 to k=7 
#this will give us hat = [1,2,4,8,16,32,64]

sum_check = 124
probable_sum = 0

while sum_check > probable_sum :
    random_card = random.choice(hat)
    probable_sum += random_card
    hat.remove(random_card)

print(probable_sum)
