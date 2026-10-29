class Fibonacci:
    def __init__(self):
        self.memo = {}

    def fibonacci(self, n):
        if n in self.memo:
            return self.memo[n]

        if n == 0:
            return 0
        elif n == 1:
            
            return 1

        self.memo[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        return self.memo[n]

    def display_series(self, n):
        print("\nFibonacci Series:")
        for i in range(n + 1):
            print(self.fibonacci(i), end=" ")

    def display_nth(self, n):
        print(f"\n\nThe {n}th Fibonacci number is: {self.fibonacci(n)}")


def main():
    print("===== Fibonacci Number Calculator =====")

    try:
        n = int(input("Enter the value of n: "))

        if n < 0:
            print("Please enter a non-negative integer.")
            return

        fib = Fibonacci()
        fib.display_series(n)
        fib.display_nth(n)

    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()