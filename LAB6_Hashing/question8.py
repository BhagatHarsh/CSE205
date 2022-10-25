import random


class Server:
    def __init__(self, n: int):
        self.N = n
        self.ht = []
        for i in range(n):
            self.ht.append([])
        self.full = False
        self.drop = []
        assert self.full == False, "Hash Table full"
        return

    def insert(self, n: int):
        h = n % (self.N)
        if (h not in self.drop):
            self.ht[h].append(n)
        else:
            i = 1
            flag = 1
            tmp = h
            while (h in self.drop):
                try:
                    i += (n // (n%self.N)) 
                except:
                    i += 1
                h = (n + (i)) % self.N
                if (h == tmp):
                    flag = 0
                    break
            if (flag):
                self.ht[h].append(n)
            else:
                print("Couldn't hash", n)
        return

    # def check(self, n: int):
    #     h = n % (self.N)
    #     flag = 0
    #     if (h not in self.drop):
    #         for i in self.ht[h]:
    #             if(i == n):
    #                 flag = 1
    #                 break
    #     else:
    #         i = 1
    #         tmp = h
    #         while (h in self.drop):
    #             try:
    #                 i += (n // (n%self.N)) 
    #             except:
    #                 i += 1
    #             h = (n + (i)) % self.N
    #             for j in self.ht[h]:
    #                 if(j == n):
    #                     flag = 1
    #                     break
    #             else:
    #                 break
    #             if (h == tmp):
    #                 break
    #         for j in self.ht[h]:
    #                 if(j == n):
    #                     flag = 1
    #                     break
                
    #     if (flag):
    #         print("Element Found", n)
    #     else:
    #         print("Element not Found", n)
    #     return

    def printHash(self):
        for i in self.ht:
            print(i)
        print("\n")

    def resize(self, n: int):
        assert self.N - n > 0, "Negative Size"
        i = self.N - n
        while (i > 0):
            dp = random.randint(0, self.N - 1)
            if (dp not in self.drop):
                self.drop.append(dp)
                for j in self.ht[dp]:
                    self.insert(j)
                self.ht[dp] = []
                print(self.drop)
                i -= 1
        self.N = n
        return


server = Server(17)
for i in range(126):
    server.insert(i)
server.printHash()
server.resize(13)
server.printHash()
# for i in range(126):
#     server.check(i)
