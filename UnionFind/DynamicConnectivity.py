
# this was my first solution ,and it is the least efficient way to deal with the problem of dynamic connectivity
class UF:

    def __init__(self, N: int):
        self.N = N
        self.result = []

    def unionA(self, l: list):

        for i in range(len(l)):
            p, q = l[i].split()

            for j in self.result:
                if p in j or q in j:
                    j.update({p, q})
                    break
            else:
                self.result.append({p, q})

        print(self.result)



def main():
    temp = []
    with open('/Data Structures and algorithms/DynamicConnectivity/text.txt') as f:
        N = int(f.readline())
        for i in range(N):
            temp.append(f.readline().strip())

    uf = UF(N)
    UF.unionA(uf, temp)

if __name__ == '__main__':
     main()