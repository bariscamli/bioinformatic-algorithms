# Pattern Matching Problem

# Find all ocurences of a pattern in a string.

# Input: String pattern and Genome
# Output: All starting positions in Genome where Patter appears as a substring

def patternMatch(pattern, genome):
    n = len(genome)
    k = len(pattern)
    startingPositions = []

    for i in range(n - k):
        if pattern == genome[i:i + k]:
            startingPositions.append(i)
    return startingPositions


if __name__ == '__main__':
    print(patternMatch("TTT", "ACGTTTCACGTTTTACGG"))
