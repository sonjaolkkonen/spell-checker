class DamerauLevenshtein:
    def __init__(self):
        """Class constructor which creates a new DamerauLevenshtein object.
        """

    def damerau_levenshtein_distance(self, word1, word2):
        """Method which gives the distance of two given strings

        Args:
            word1 (str): first given string
            word2 (str): second given string

        Returns:
            int: distance
        """
        #create a 2D table to store the distances
        d = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]


        #initialize the table
        for i in range(len(word1) + 1):
            d[i][0] = i
        for j in range(len(word2) +1):
            d[0][j] = j

        #populate the table
        for i in range(1, len(word1) +1):
            for j in range(1, len(word2) +1):
                cost = 1
                if word1[i-1] == word2[j-1]:
                    cost = 0

                d[i][j] = min(d[i-1][j] + 1, #deletion
                             d[i][j-1] + 1, #insertion
                             d[i-1][j-1] + cost) #substitution

                if i > 1 and j > 1 and word1[i-1] == word2[j-2] and word1[i-2] == word2[j-1]:
                    d[i][j] = min(d[i][j],
                                  d[i-2][j-2] + 1) #transposition

        return d[len(word1)][len(word2)]
