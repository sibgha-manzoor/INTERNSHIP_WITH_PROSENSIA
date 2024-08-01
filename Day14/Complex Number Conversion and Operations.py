def complex_operations(complex_str1, complex_str2):
    complex_num1 = complex(complex_str1)
    complex_num2 = complex(complex_str2)
    
    addition = complex_num1 + complex_num2
    subtraction = complex_num1 - complex_num2
    multiplication = complex_num1 * complex_num2
    if complex_num2 != 0:
        division = complex_num1 / complex_num2  
    else:
        return "Zero Error"
    
    return (addition, subtraction, multiplication, division)

result = complex_operations("3+4j", "1-2j")
print(result)