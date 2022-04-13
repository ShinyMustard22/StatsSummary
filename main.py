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

    numbers.sort()

    print("Mean:", statistics.mean(numbers))
    print("Median:", statistics.median(numbers))
    print("Mode:", statistics.mode(numbers))
    print("Range:", numbers[-1] - numbers[0])

    print("Population variance:", statistics.pvariance(numbers))
    print("Sample variance:", statistics.variance(numbers))

    print("Sample standard deviation:", statistics.pstdev(numbers))
    print("Population standard deviation:", statistics.stdev(numbers))


if __name__ == "__main__":
    main()
