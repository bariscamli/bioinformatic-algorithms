# Reverse Complement Problem:

# Find the reverse complement of a DNA string.

# Input: A DNA string Pattern
# Output: Pattern, the reverse complement of Pattern.

def complement(text):
    result = ""
    matchMap = {"A": "T", "a": "t",
                "T": "A", "t": "a",
                "C": "G", "c": "g",
                "G": "C", "g": "c"}

    for letter in text:
        if letter in matchMap.keys():
            result += matchMap[letter]
        else:
            # For unknown letters
            result += "?"
    return result


def reverseComplement(text):
    return complement(text)[::-1]

if __name__ == '__main__':
    print(reverseComplement("ATGATCAAG"))