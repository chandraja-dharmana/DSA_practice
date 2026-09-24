def generate_strings(n):
    result = []

    def backtrack(current):
        # Base case: string reached length N
        if len(current) == n:
            result.append(current)
            #print("result: ", result)
            return

        # Choose A
        backtrack(current + "A")
        #print("current A: ", current)

        # Choose B
        backtrack(current + "B")
        #print("current B: ", current)

    backtrack("")
    return result


n = 3
print(generate_strings(n))