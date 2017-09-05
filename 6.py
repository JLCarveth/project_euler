import time

class Problem():
    def solve(self, n):
        sumOfSq = 0
        sqOfSum = 0
        
        for i in range(1,n + 1):
            sumOfSq += i ** 2
            sqOfSum += i

        sqOfSum = sqOfSum ** 2

        return sqOfSum - sumOfSq
        


if __name__ == "__main__":
    p = Problem()

    start = time.time()
    
    solution = p.solve(100)

    elapsed = time.time() - start

    print("Result:",solution)
    print("Time Elapsed: ", round(elapsed,2) ,"s")
    
