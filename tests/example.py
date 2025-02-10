import re

def extract_number(text):
    # Use regex to find the number inside the brackets
    match = re.search(r'\(.*?(\d+).*?\)', text)
    if match:
        return match.group(1)
    return None

# Example usage
text = "Wache (GHc 15)"
number = extract_number(text)
print(number)  # Output: 15
