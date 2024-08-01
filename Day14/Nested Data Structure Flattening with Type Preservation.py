def flatten_and_depth(nested_list):
    def flatten_helper(lst, current_depth):
        flattened = []
        max_depth = current_depth
        for element in lst:
            if isinstance(element, list):
                sublist, sub_depth = flatten_helper(element, current_depth + 1)
                flattened.extend(sublist)
                max_depth = max(max_depth, sub_depth)
            else:
                flattened.append(element)
        return flattened, max_depth

    flat_list, depth = flatten_helper(nested_list, 1)
    return flat_list, depth

nested_list = [1, [2, [3, [4, 5]], 6], 7]
flattened_list, depth = flatten_and_depth(nested_list)
print(f"Flattened List: {flattened_list}")
print(f"Depth: {depth}")