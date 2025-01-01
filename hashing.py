def custom_hash(input_string):
    
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string.")
    
    hash_value = 0
    prime = 47
    
    for i, char in enumerate(input_string):
        
        char_code = ord(char)
        hash_value = (hash_value * prime + char_code) ^ (i + 1)
        hash_value &= 0xFFFFFFFF
    
    return hash_value

input_data = "Hello, World!"
hashed_value = custom_hash(input_data)
print(f"The hash of '{input_data}' is: {hashed_value}")
