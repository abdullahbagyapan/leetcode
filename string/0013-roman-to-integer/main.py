class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        n = len(s)

        for i in range(n):
            current = values[s[i]]
            if i + 1 < n and current < values[s[i + 1]]:
                total -= current
            else:
                total += current

        return total


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
        ("MMMCMXCIX", 3999),
    ]

    for idx, (s, expected) in enumerate(test_cases, start=1):
        result = sol.romanToInt(s)
        assert result == expected, f"Test {idx} failed: got {result}, expected {expected}"
        print(f"Test {idx} passed: {s} -> {result}")