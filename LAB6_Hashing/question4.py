class Hashtable:
    def __init__(self, n: int):
        self.N = n
        self.ht = [0] * n
        self.full = False
        assert self.full == False, "Hash Table full"
        return

    def insert(self, n: int):
        h = n % (self.N)
        self.ht[h] = 1
        return

    def check(self, n: int):
        h = n % (self.N)
        if (self.ht[h] == 0):
            print("Element Not Found", n)
        else:
            print("Element Found", n)
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
