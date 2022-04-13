import statistics


def main():
    numbers = []

    num = input("Enter next number: ")

    while num.isdigit():
        numbers.append(int(num))
        num = input("Enter next number: ")

    if len(numbers) < 2:
        print("Sorry, you need at least 2 data values.")
        return

    print("Population standard deviation:", statistics.stdev(numbers))
    print("Sample standard deviation:", statistics.pstdev(numbers))


if __name__ == "__main__":
    main()
