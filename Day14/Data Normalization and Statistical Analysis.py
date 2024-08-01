def normalize_and_stats(numbers):
    if not numbers:
        raise ValueError("The input list is empty.")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements in the list must be numeric.")
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    if min_val == max_val:
        normalized = [0.5] * len(numbers)
    else:
        normalized = [(x - min_val) / (max_val - min_val) for x in numbers]

    mean = sum(normalized) / len(normalized)

    sorted_normalized = sorted(normalized)
    n = len(sorted_normalized)
    median = (sorted_normalized[n // 2] if n % 2 == 1 else
              (sorted_normalized[n // 2 - 1] + sorted_normalized[n // 2]) / 2)
    
    variance = sum((x - mean) ** 2 for x in normalized) / len(normalized)
    
    return mean, median, variance

numbers = [10, 20, 30, 40, 50]
mean, median, variance = normalize_and_stats(numbers)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")