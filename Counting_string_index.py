def custom_count(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


# Example usage
input_string = "hello world"
result = custom_count(input_string)

for char, count in result.items():
    if count > 1:
        print(f"'{char}' appears {count} times.")
