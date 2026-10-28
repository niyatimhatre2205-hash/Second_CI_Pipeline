def most_frequent(numbers):
    if not numbers:
        return None

    return max(numbers, key=numbers.count)