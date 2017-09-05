class Problem():
    def solve(self):
        '''
        By considering the terms in the Fibonacci sequence whose values
        do not exceed four million, find the sum of the even-valued terms.
        '''

        fib1 = 1
        fib2 = 1
        result = 0

        _sum = 0

        while result < 4000000:
            if result % 2 == 0:
                _sum += result

            result = fib1 + fib2

            fib2 = fib1
            fib1 = result

        return _sum

if __name__ == "__main__":
    p = Problem()
    solution = p.solve()
    
    print(solution)     # 4,613,732 is the sum.
        
