class Solution:
    def RomantoInteger(self, s:str) -> int:
        int_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
                     "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5,
                     "IV": 4, "I": 1}
        prev = inf
        #current = 0
        total = 0

        for letter in s:
            current = int_dict[letter]

            if prev < current:
                current -= prev
                total -= prev

            else:
                prev = current

            total += current


        return total
