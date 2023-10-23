def find_index(N, numbers, X):
    if X in numbers:
        return numbers.index(X) + 1
    return -1

if __name__ == "__main__":
    N = int(input("Enter a positive integer (N): "))
    numbers = []
    
    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    X = int(input("Enter an integer (X): "))
    result = find_index(N, numbers, X)
    print(result)
