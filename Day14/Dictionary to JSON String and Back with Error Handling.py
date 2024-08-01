import json

def dict_to_json_and_back(input_dict):
    try:
        json_str = json.dumps(input_dict)
    except (TypeError, OverflowError) as e:
        return input_dict, f"Error converting to JSON: {str(e)}"
    
    try:
        result_dict = json.loads(json_str)
    except json.JSONDecodeError as e:
        return json_str, f"Error converting back to dict: {str(e)}"
    
    return result_dict

input_data = {"name": "Sara", "age": 20, "city": "Islamabad"}
result = dict_to_json_and_back(input_data)
print(result)