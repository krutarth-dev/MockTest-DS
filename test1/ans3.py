def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean
data = [5, 12, 8, 21, 17, 10]
mean_value = calculate_mean(data)
print("Mean:", mean_value)
