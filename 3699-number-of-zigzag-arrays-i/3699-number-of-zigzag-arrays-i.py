class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        up = [0] * m
        down = [0] * m

        for x in range(m):
            up[x] = x
            down[x] = m - 1 - x

        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            prefix = 0
            for x in range(m):
                new_up[x] = prefix
                prefix = (prefix + down[x]) % MOD

            suffix = 0
            for x in range(m - 1, -1, -1):
                new_down[x] = suffix
                suffix = (suffix + up[x]) % MOD

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD