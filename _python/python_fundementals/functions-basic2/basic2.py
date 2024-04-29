def countdown(number):
    newList = []
    for i in range(number, -1, -1):
        newList.append(i)
    return newList

x=countdown(5)
print(x)

def twoNumbers(numbers):
    first_num=numbers[0]
    second_num=numbers[1]

    print(first_num)
     
    return second_num
    

x=twoNumbers([1,2])

print(x)


def First_Length(data):

    first_element=data[0]
    last_element=len(data)

    sum=first_element+last_element

    return sum

x=First_Length([1,2,3,4])
print(x)

def Greater(second):
    newList=[]

    
    
def greaterThanScnd(para):
    newList = []
    scndvalue = para[1]

    for k in range(len(para)):
        if para[k] > scndvalue:
            newList.append(para[k])

    if len(newList) < 2:
        return False
    else:
        return newList

h = greaterThanScnd([1, 2, 3, 4, 5, 6])   
print(len(h))          


def length_and_value(num5, value):
    result = []
    for g in range(num5):
        result.append(value)
    return result


print(length_and_value(4, 7))  
print(length_and_value(6, 2))