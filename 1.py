class Problem:
    def solve(self):
        '''
        Find the sum of all multiples of 3 or 5 below 1000.
        '''

        s = 0
        
        for i in range(0, 1000):
            if (i % 3 == 0) or (i % 5 == 0):
                s += i
        
        return s

if __name__ == "__main__":
    p = Problem()
    solution = p.solve()

    print(solution)     # 233,168 is the sum.
