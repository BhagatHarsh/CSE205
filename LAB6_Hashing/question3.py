
class Hashtable:
    def __init__(self, n: int, p: int):
        self.N = n
        self.ht = [None] * n
        self.full = False
        self.P = p
        assert self.full == False, "Hash Table full"
        return

    def insert(self, n: int):
        i = 0
        h = ((n % self.N) + i * (1 + (n % self.P))) % self.N
        if (self.ht[h] == None):
            self.ht[h] = n
        else:
            tmp = h
            while (self.ht[h] != None):
                i += 1
                h = ((n % self.N) + i * (1 + (n % self.P))) % self.N
                if (h == tmp):
                    self.full = True
            self.ht[h] = n
        return

    def check(self, n: int):
        i = 0
        h = ((n % self.N) + i * (1 + (n % self.P))) % self.N
        if (self.ht[h] == None):
            print("Element Not Found", n)
        else:
            tmp = h
            if (self.ht[h] == n):
                print("Element Found", n)
                return
            while (h < self.N):
                i += 1
                h = ((n % self.N) + i * (1 + (n % self.P))) % self.N
                if (h == tmp):
                    print("Element Not Found", n)
                    break
                elif (self.ht[h] == n):
                    print("Element Found", n)
                    break
            if (h >= self.N):
                print("Element Not Found", n)
        return

    def printHash(self):
        print(self.ht)


hash = Hashtable(17, 11)
hash.insert(133)
hash.insert(88)
hash.insert(92)
hash.insert(221)
hash.insert(174)
hash.check(100)
hash.check(133)
hash.check(174)
hash.printHash()
