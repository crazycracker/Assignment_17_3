from scipy.stats import binom

# no of red balls
n = 4
# no of black balls
m = 6

#there are three possiblities
# red red
# red black
# black black

# first turn probability of drawing red ball
p = 4/10
# second turn probability of drawing red ball
p1 = 3/9

total_probability = p + p1
print('probability of red and red - %.2f' %(total_probability))


# first turn probability of drawing red ball
p = 4/10
# second turn probability of drawing black ball
p1 = 6/9

total_probability = p + p1
print('probability of red and black - %.2f' %(total_probability))


# first turn probability of drawing black ball
p = 6/10
# second turn probability of drawing black ball
p1 = 5/9

total_probability = p + p1
print('probability of black and black - %.2f' %(total_probability))
