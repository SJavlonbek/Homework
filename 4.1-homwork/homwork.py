class Solution:
    def convertToTitle(self, n: int) -> str:
        ustun_nomlari = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I", 
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O",
            16: "P",
            17: "Q",
            18: "R",
            19: "S",
            20: "T",
            21: "U",
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
            26: "Z"
        }

        if n in ustun_nomlari:
            return ustun_nomlari[n]
        else:
            ustun_nomi = ""
            while n > 0:
                z = (n - 1) % 26
                ustun_nomi = ustun_nomlari[z + 1] + ustun_nomi
                n = (n - 1) // 26
            return ustun_nomi

natija = Solution()
print(natija.convertToTitle(1))

print(natija.convertToTitle(2))

print(natija.convertToTitle(28))

print(natija.convertToTitle(701))


print(natija.convertToTitle(702))