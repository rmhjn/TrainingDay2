#Write a function in Python to parse a string such that it accepts a parameter- an encoded string. This encoded string will contain a first name, last name, and an id. You can separate the values in the string by any number of zeros. The id will not contain any zeros. The function should return a Python dictionary with the first name, last name, and id values. For example, if the input would be "John000Doe000123". Then the function should return: { "first_name": "John", "last_name": "Doe", "id": "123" }
def parse_encoded_string(encoded_string):
    parts = encoded_string.split('0')  # Split the string by zeros
    parts = [part for part in parts if part]  # Remove empty parts

    if len(parts) >= 3:
        first_name = parts[0]
        last_name = parts[1]
        id_value = parts[2]
        result = {
            "first_name": first_name,
            "last_name": last_name,
            "id": id_value
        }
        return result
    else:
        return None

# Example usage:
encoded_string = "John000Doe000123"
parsed_data = parse_encoded_string(encoded_string)
if parsed_data:
    print(parsed_data)
else:
    print("Invalid input string.")
