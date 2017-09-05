import time

class Problem:
    def solve(self, step):
        check_list = [11,13,14,15,16,17,18,19,20]

        for num in range(step, 999999999, step):    # Adding the step increment
                                                    # saves many cycles!
            if all(num % n == 0 for n in check_list):
                return num
        return None

if __name__ == "__main__":
    p = Problem()

    start = time.time()
    solution = p.solve(20)
    
    print("Result: ", solution)

    elapsed = time.time() - start
    
    print("Time: ", round(elapsed, 2), "s")
