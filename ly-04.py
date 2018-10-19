class student():
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_scores(self):
        return max(self.scores)

if __name__ == '__main__':
    stu = student("xhweek", "25", [12,20,30,40,50,60])
    print(stu.get_age())
    print(stu.get_name())
    print(stu.get_scores())
