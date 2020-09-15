class list_fun:
    def __init__(self):
        self.l = []

    def add(self,n):
        self.l.append(n)

    def search(self,f):
        if f in self.l:
            print("found!!")
        else:
            print("not found")

    def sorts(self):
        self.l.sort()

    def reversing(self):
        self.l = self.l[::-1]

    def display(self):
        print(self.l)

l1 = list_fun()
l1.add(5)
l1.add(9)
l1.add(8)
l1.add(9)
l1.add(2)
l1.add(6)

l1.search(6)
l1.sorts()
l1.display()
l1.reversing()
l1.display()
