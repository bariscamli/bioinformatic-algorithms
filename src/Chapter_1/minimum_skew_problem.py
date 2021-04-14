# Minimum Skew Problem

# Find a position in a genome where the skew diagram attains a minimum.

# Input: A DNA string Genome
# Output: All integers i minimizing SKEWi(Genome) among all values of i
def minSkew(genome):
    min_skew = len(genome)
    min_skew_index = []
    g_values = 0
    c_values = 0

    for i in range(len(genome)):
        current_gen = genome[i]
        if current_gen == "C" or current_gen == "c":
            c_values += 1
        elif current_gen == "G" or current_gen == "g":
            g_values += 1
        currentSkew = g_values - c_values

        if currentSkew < min_skew:
            min_skew = currentSkew
            del min_skew_index
            min_skew_index = []
            min_skew_index.append(i)
        elif currentSkew == min_skew:
            min_skew_index.append(i)
    return min_skew_index


if __name__ == '__main__':
    print(minSkew("CATGGGCATCGGCCATACGCCCGC"))

