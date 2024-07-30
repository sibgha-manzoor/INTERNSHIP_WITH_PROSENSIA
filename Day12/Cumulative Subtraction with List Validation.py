def subtract_sequence(numbers):
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements in the list must be numeric values.")
    
    result = numbers[0]
    
    for num in numbers[1:]:
        result -= num
    
    return result

print(subtract_sequence([10, 2, 3, 4]))
print(subtract_sequence([10]))
print(subtract_sequence([10, 'a', 3]))