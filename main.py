import statistics


def main():
    numbers = []

    num = input("Enter the first number: ")

    while num.isdigit():
        numbers.append(int(num))
        num = input("Enter next number (enter non-numerical data to end): ")

    if len(numbers) < 2:
        print("Sorry, you need at least 2 data values.")
        return

    print("Mean:", round(statistics.mean(numbers), 2))
    print("Median:", round(statistics.median(numbers), 2))
    print("Mode:", round(statistics.mode(numbers), 2))
    print("Range:", round(max(numbers) - min(numbers), 2))

    print("Population variance:", round(statistics.pvariance(numbers), 2))
    print("Sample variance:", round(statistics.variance(numbers), 2))

    print("Population standard deviation:", round(statistics.pstdev(numbers), 2))
    print("Sample standard deviation:", round(statistics.stdev(numbers), 2))


if __name__ == "__main__":
    main()
