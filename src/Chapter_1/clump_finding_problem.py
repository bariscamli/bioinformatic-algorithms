# Clump Finding Problem

# Find patterns forming clumps in a string.

# Input: A string Genome, and integers k, L, and t.
# Output: All distinct k-mers forming (L, t)-clumps in Genome.

def frequencyMap(text, k):
    freqMap = {}
    n = len(text)
    for i in range(n - k):
        pattern = text[i:i + k]
        if pattern not in freqMap.keys():
            freqMap[pattern] = 1
        else:
            freqMap[pattern] = freqMap[pattern] + 1
    return freqMap

def findClumps(genome, k, L, t):
    patterns = set()
    n = len(genome)

    for i in range(0, n - L):
        window = genome[i:i + L]
        freqMap = frequencyMap(window, k)
        for pattern in freqMap.keys():
            if freqMap[pattern] >= t:
                patterns.add(pattern)
    return patterns

if __name__ == '__main__':
    print(findClumps("ACGTTTCACGTTTTACGG", 3, 12, 2))