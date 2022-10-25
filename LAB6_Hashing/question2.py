class Hashtable:
    def __init__(self, n: int):
        self.N = n
        self.ht = [None] * n
        self.full = False
        assert self.full == False, "Hash Table full"
        return

    def insert(self, n: int):
        h = n % (self.N)
        if (self.ht[h] == None):
            self.ht[h] = n
        else:
            tmp = h
            i = 0
            while (self.ht[h] != None):
                i += 1
                h = (n + (i**2)) % self.N
                if (h == tmp):
                    self.full = True
            self.ht[h] = n
        return

    def check(self, n: int):
        h = n % (self.N)
        if (self.ht[h] == None):
            print("Element Not Found", n)
        else:
            tmp = h
            if (self.ht[h] == n):
                print("Element Found", n)
                return
            i = 1
            h = (n + (i**2)) % self.N
            while (h < self.N):
                if (h == tmp):
                    print("Element Not Found", n)
                    break
                elif (self.ht[h] == n):
                    print("Element Found", n)
                    break
                i += 1
                h = (n + (i**2)) % self.N
            if(h >= self.N):
                print("Element Not Found", n)
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

# b trying Seconday clustering
hash = Hashtable(10)
hash.insert(10)
hash.insert(100)
hash.insert(1000)
hash.insert(10000)
hash.check(1000)
hash.check(10000)
hash.printHash()