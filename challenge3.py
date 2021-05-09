import random

hat = [1,2,4,8,16,32,64]

sum_check = 124
probable_sum = 0

while sum_check > probable_sum :
    random_card = random.choice(hat)
    probable_sum += random_card
    hat.remove(random_card)

print(probable_sum)
