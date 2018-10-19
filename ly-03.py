for i in range(100,1000):
    s = list(str(i))
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)

for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green == 8:
                print("red:{0}====yellow:{1}===green:{2}".format(red,yellow,green))