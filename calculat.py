class Count:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

if __name__ == '__main__':
    num = Count(1, 2)
    print(num.add())

