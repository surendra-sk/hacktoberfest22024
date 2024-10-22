# Function to create the LPS array for the pattern
def computeLPSArray(pattern):
    length = 0  # length of the previous longest prefix suffix
    lps = [0] * len(pattern)  # lps array
    i = 1

    # Build the lps array for the pattern
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

# KMP Algorithm to find the pattern in the text
def KMPSearch(text, pattern):
    n = len(text)
    m = len(pattern)

    # Preprocess the pattern to create the lps array
    lps = computeLPSArray(pattern)

    i = 0  # index for text
    j = 0  # index for pattern
    positions = []  # Store the positions where pattern is found

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:  # Found the pattern
            positions.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions

# Driver code to test the KMP algorithm
if __name__ == "__main__":
    text = "ababcabcabababd"
    pattern = "ababd"
    
    result = KMPSearch(text, pattern)
    
    if result:
        print(f"Pattern found at positions: {result}")
    else:
        print("Pattern not found in the text.")
