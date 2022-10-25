class StringHash:
    def __init__(self, a, n):
        self.A = a
        self.N = n
        self.st = [""] * n
        return

    def insert(self, st):
        hash = self.polynomial_hash(st)
        print("polynomial_hash of %s is %d"%(st,hash))
        self.st[hash] = st
        return

    def polynomial_hash(self, s):
        hash = 0
        i = self.N
        for c in s:
            hash = (hash + (ord(c) * (self.A**i))) % self.N
            i -= 1
        return hash

    def printTable(self):
        print(self.st)
        return

table = StringHash(2,17)
table.insert("fist")
table.insert("sift")
table.insert("shift")
table.insert("fast")
table.insert("faster")
table.insert("shaft")
table.printTable()

table = StringHash(2,37)
table.insert("fist")
table.insert("sift")
table.insert("shift")
table.insert("fast")
table.insert("faster")
table.insert("shaft")
table.printTable()