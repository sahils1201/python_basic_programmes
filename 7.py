#7.⁠ ⁠Write a python function that takes a list and returns a new list with distinct elements from first list
def remove_duplicates(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

# Example usage:
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
result_list = remove_duplicates(sample_list)
print(f"Original list: {sample_list}")
print(f"List with distinct elements: {result_list}")
