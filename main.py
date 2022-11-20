# import statistics
# import random, re
#
#
# def test_try():
#     num = input("enter a number")
#     print(type(num))
#     try:
#         num = float(num)
#         print(num)
#     except Exception as e:
#         print("Exception error", e)
#
#
# test_try()
#
#
# def tempe():
#     temperature_list = []
#     sum = 0
#     for i in range(0, 10):
#         temperature_list.append(random.randint(50, 90))
#         sum = sum + temperature_list[i]
#         print("sum is : ", temperature_list[i], sum)
#
#     num = len(temperature_list)
#     avg = sum / num
#     print("Average is : ", sum)
#     print(temperature_list)
#     print("Mean is : ", statistics.mean(temperature_list))
#     print("mode is : ", statistics.mode(temperature_list))
#     print("Average is : ", avg)
#     l = temperature_list
#     print('llll', l)
#     abc = l[1:-1]
#     print("list slicing", [abc])
#
#     # method1 to reverse
#     print("reverse list")
#     for i in range(len(l) - 1, -1, -1):
#         print('list1', l[i])
#
#     # method2 to reverse
#     print("reverse list2")
#     print(l[::-1], end='-')
#
#     print('liste5')
#     for i in l:
#         print(i, end=' - ')
#     print()
#     ch = iter(l)
#     print('iterator1:', next(ch))
#     print('iterator2:', next(ch))
#
#     # example with slice
#
#
# print('-------------------------------')
#
# # on  basis of operations usage
#
# # initializing a with range()
# a = range(1, 6)
#
# # initializing a with xrange()
# # x = xrange(1, 6)
#
# # testing usage of slice operation on range()
# # prints without error
# print("The list after slicing using range is : ")
# print(a[2:5])
# t = [5, 7, 10, 19, 3, 1]
# abc1 = slice(3, -1)
# print('slicesssssssssssssss', t[abc1])
#
# # testing usage of slice operation on xrange()
# # raises error
# print("The list after slicing using xrange is : ")
# print(a[2:5])
# st = 'ABDCFEHHS'
# print('string:', st.lower())
# st = 'abdillahi'
# print('string:', st.capitalize())
#
# tempe()
#
# # help()
# import array as arr
#
# num = arr.array('i', [2, 8, 7, 4, 23, 1])
#
# print('---------------Python array------------')
# for x in num:
#     print(x, end=" ")
#     print()
#
# for x in num:
#     print(x / 2, end=" ")
#
# print()
#
# print('---------------Python array2------------')
# num.append(66)
# for x in num:
#     print(x, end="- ")
# print()
# num.remove(7)
# for x in num:
#     print(x, end=" ")
#
# import copy
#
# x = [1, 2, 3]
# z = copy.deepcopy(x)
# print()
# print('x before deepcopy---:', x)
# print()
# print('z before deepcopy---:', z)
# print()
# print('----- deepcopy-----')
# print()
# x[2] = 'Hello'
# print('x after deepcopy---:', x)
# print()
#
# print('z after deepcopy---:', z)
# print('********************os module ************************')
# import os
#
# # print(dir(os))
# print(os.getcwd())
# # print(os.listdir())
# os.chdir('C:/Users/shahm/OneDrive/Desktop/OtherFiles/')
# print(os.getcwd())
# print(os.listdir())

# how to verify duplicate

print('testiing')

def verify_dupl():
   # l = ['ALI', 'med', 'fozia', 'ali', 'MED', 'Ali', 'Hassan']
    l={10,15,6,4,8,10,4,88}
    l2=(10,15,7,10,5,7,15)
    noms={'osman','med','Ali','MED','djama','ALI','med','musassasaa'}
    for item in l:
        print(float(item), end=' ')
    print()
    print("list2")
    for item2 in l2:
        print(item2,end=' ')
    print()

    noms1={}


verify_dupl()


noms3 = ['ali','osman', 'med', 'Ali', 'MED', 'djama', 'ALI', 'med','ali','omar','farah']
noms4=[]
print("list without duplicate")
for item3 in noms3:
    item = item3.lower()

    if item not in noms4:
        noms4.append(item)
        print(item.capitalize(), end=' ')


print()
#comprension list
number_list = [ x for x in range(20) if x % 2 == 0]

print(number_list)