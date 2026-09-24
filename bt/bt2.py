def generate_strings(n):
    result = []

    def backtrack(current):
        # Base case: string reached length N
        if len(current) == n:
            result.append(current)
            return

        # Choose A
        backtrack(current + "A")

        # Choose B
        backtrack(current + "B")

    backtrack("")
    return result


n = 3
print(generate_strings(n))