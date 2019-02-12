class ListInfo(object):
    def __init__(self,val_list):
        self.slist = val_list

    def add_key(self,values):
        self.slist.append(values)
        print(self.slist)
        return self.slist

    def get_key(self,index):
        if isinstance(index, int):
            if index >= 0 and index < len(self.slist):
                #print(self.slist[index])
                return self.slist[index]
            return "out of index"
        else:
            return "input error"

    def update_list(self,listt):
        if isinstance(listt, list):
            self.slist.extend(listt)
            return self.slist
        return "input wrong"

    def del_key(self):
        if len(self.slist) >= 0:
            return self.slist.pop(-1)
        return "none num"

#if __name__ == '__main__':
mylist = ListInfo([1,2,3,4,5,6])
    #mylist.add_key(7)
print(mylist.del_key())
print(mylist.del_key())
