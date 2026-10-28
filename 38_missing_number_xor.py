def missing_number(numbers):
    n = len(numbers)
    result = n

    for i, num in enumerate(numbers):
        result ^= i ^ num

    return result