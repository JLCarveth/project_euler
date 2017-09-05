class Problem:
    def solve(self):
        '''
        What is the largest prime factor of the number 600851475143 ?
        '''
        num = 600851475143
        i = 2

        while i * i < num:
            while num % i == 0:
                num = num / i
            i += 1
        return num

if __name__ == "__main__":
    p = Problem()

    solution = p.solve()

    print(solution)     # 6857
    
