def round_float(value, strategy):
    if strategy == "up":
        return int(value) + (1 if value > int(value) else 0)
    elif strategy == "down":
        return int(value)
    elif strategy == "nearest":
        return int(value + 0.5) if value >= 0 else int(value - 0.5)
    else:
        raise ValueError("Invalid rounding strategy. Choose 'up', 'down', or 'nearest'.")

rounded_up = round_float(3.7, "up")      
rounded_down = round_float(3.7, "down") 
rounded_nearest = round_float(3.7, "nearest") 

print(rounded_up)  
print(rounded_down)  
print(rounded_nearest)  