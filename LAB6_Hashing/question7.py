class Hashtable:
    def __init__(self, n: int):
        self.N = n
        self.ht = []
        for i in range(n):
            self.ht.append([])
        self.full = False
        assert self.full == False, "Hash Table full"
        return

    def insert(self, n: int):
        h = n % (self.N)
        self.ht[h].append(n)
        return

    def check(self, n: int):
        h = n % (self.N)
        flag = 0
        for i in self.ht[h]:
            if (i == n):
                flag = 1
                break
        if (flag):
            print("Element Found", n)
        else:
            print("Element not Found", n)
        return

    def printHash(self):
        print(self.ht)


hash = Hashtable(17)
hash.insert(133)
hash.insert(88)
hash.insert(92)
hash.insert(221)
hash.insert(174)
hash.check(100)
hash.check(133)
hash.check(174)
hash.printHash()

hash = Hashtable(37)
hash.insert(133)
hash.insert(88)
hash.insert(92)
hash.insert(221)
hash.insert(174)
hash.check(100)
hash.check(133)
hash.check(174)
hash.printHash()

# trying primary clustering
hash = Hashtable(10)
hash.insert(10)
hash.insert(100)
hash.insert(1000)
hash.insert(10000)
hash.check(1000)
hash.check(10000)
hash.printHash()
