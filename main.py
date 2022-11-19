

#problem3_7("flowers.csv","alyssum")

def problem1_2(x,y):
    print (x+y)
    print (x*y)


num1=6
num2=6
abc=problem1_2(num1,num2)
print("result:",abc)


def problem1_3(n):
    my_sum = 0
    for number in range(n+1):
        my_sum = my_sum + number
        print (number,my_sum,)

problem1_3(4)
print()
l=[2,5,6,2,7,2,6,6,5,89]
l2=[]

for i in l:
    if i not in l2:
        l2.append(i)
        print(i,end=' - ')