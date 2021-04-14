#Frequent Words Problem

#Find the most frequent k-mers in a string.

#Input: A String Text and an integer k.
#Output: All most frequent k-mers in Text.

def maxValue(freqMap):
    first_key = next(iter(freqMap))
    max_number = freqMap[first_key]
    for i in freqMap.keys():
        if freqMap[i] > max_number:
            max_number = i
    return max_number


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


def frequentWord(text, k):
    freqPatterns = []
    freqMap = frequencyMap(text, k)
    maxCount = maxValue(freqMap)

    for pattern in freqMap.keys():
        if freqMap[pattern] == maxCount:
            freqPatterns.append(pattern)
    return freqPatterns

if __name__ == '__main__':
    print(frequentWord("ACGTTTCACGTTTTACGG",3))