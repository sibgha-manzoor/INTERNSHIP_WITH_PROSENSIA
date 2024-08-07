def get_value(dictionary, key):
    value = dictionary.get(key, 0)
    print(f"The value for key '{key}' is: {value}")

fruit = {
    'apple': 1,
    'banana': 9,
    'grapes': 5
}

get_value(fruit, 'banana') 
get_value(fruit, 'orange')