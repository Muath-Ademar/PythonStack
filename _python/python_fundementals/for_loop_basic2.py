def biggie(big):

    for i in range(len(big)):
        if big[i] > 0:
            big[i] = "big"
    return big
print (biggie([-1,3,5,-5]))

def count_positives(positve):
    counter = 0
    for i in range(len(positve)):
        if positve[i]> 0:
            counter +=1
            positve[len(positve)-1] = counter
    return positve
x = count_positives([-1,1,1,1])
print(x)

def sum_total(total):
    sum = 0
    for i in range(len(total)):
        sum+= total[i]
    return sum
    

print(sum_total([1,2,3,4]))
print(sum_total([3,6,3,7,8,29]))


def average(avg):
    Avg = 0
    sum = 0
    for i in range(len(avg)):
        sum+=avg[i] 
        Avg = sum/len(avg)
    return Avg

print(average([1,2,3,4]))

def Length(list):
    total = 0
    for i in range(len(list)):
        total = len(list)
    return total

print(Length([37,2,1,-9]))

def minimum(list):
    for i in range(len(list)):
        Min = min(list)
        return Min

print(minimum([37,2,1,-9]))

def maximum(list):
    for i in range(len(list)):
        Max = max(list)
        return Max

print(maximum([37,2,1,-9]))

def ultimate_analysis(list):
        my_dictionary = {
        'Sum' : sum(list),
        'average' : sum(list)/len(list),
        'Min' : min(list),
        'maximum' : max(list),
        'length' : len(list),
        }
        return my_dictionary
print(ultimate_analysis([37,2,1,-9]))


def Rev(list):
    left =0
    right=len(list)-1
    while left<right:
        temp = list[left]
        list[left]=list[right]
        list[right] = temp
        left+=1
        right-=1
    return list
    
print(Rev([37,2,1,-9]))

 
    




