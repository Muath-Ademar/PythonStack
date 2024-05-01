import random
def randInt(min=0, max=100):
    if max<min:
        min, max = max,min
    num = random.random()*(max-min) + min
    return round(num)
print(randInt()) 		
print(randInt(max=50)) 	
print(randInt(min=50)) 	
print(randInt(min=50, max=500))    

# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.