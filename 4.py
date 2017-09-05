class Problem:
    def solve(self):
        '''
        Find the largest palindrome made from the product of
        two 3-digit numbers.
        '''
        largest = 0
        
        for i in range(999, 100, -1):
            for j in range(999, 100, -1):
                result = i * j

                if str(result) == str(result)[::-1]:
                    if result > largest:
                        largest = result
            

        return largest

if __name__ == "__main__":
    p = Problem()

    solution = p.solve()

    print(solution)     # 906609
        
