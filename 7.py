from math import sqrt
from time import time

class Problem:
    def solve(self, n, prime):
        a = [True] * (n)
        primes = []

        for i in range(2, round(sqrt(n))):
            if a[i] == True:
                for j in range(i ** 2, n, i):
                    a[j] = False

        for k in range(1,len(a)):
            if (a[k] == True):
                primes.append(k)

        return primes[prime]


if __name__ == "__main__":
    p = Problem()

    start = time()
    solution = p.solve(1000000, 10001)
    elapsed = time() - start

    print("Result: ", solution)
    print("Elapsed: ", round(elapsed, 2), "s")


    
