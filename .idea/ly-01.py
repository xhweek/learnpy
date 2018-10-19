#循环打印
#print('* ' * 5)

"""
for i in range(0,4):
    for j in range(0,5):
        print("* ",end=" ")
    print()
"""


for i in range(4):
    for j in range(5):
        #print(i,"-===========",j)
        if i == 0 or i == 3 or j == 0 or j == 4:
            print("* ",end = " ")
        else:
            print("  ",end = " ")
    print("")

for i in range(5):
    for j in range(i+1):
        if i == 4 or j == 0 or j == i:
            print("* ",end=" ")
        else:
            print("  ",end = " ")
    print()