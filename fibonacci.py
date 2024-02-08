# Write a program to generate the Fibonacci sequence up to 100

def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while True:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_fibonacci > limit:
            break
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence

limit = 100

fibonacci_sequence = generate_fibonacci(limit)
print("Fibonacci sequence up to", limit, ":", fibonacci_sequence)