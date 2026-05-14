from functools import lru_cache
from itertools import combinations


def huffman_dp(freqs):

    freqs = tuple(sorted(freqs))

    @lru_cache(None)
    def solve(state):

        if len(state) == 1:
            return 0

        best = float('inf')

        for i, j in combinations(range(len(state)), 2):

            a = state[i]
            b = state[j]

            new_state = list(state)

            new_state.pop(j)
            new_state.pop(i)

            new_state.append(a + b)

            new_state = tuple(sorted(new_state))

            cost = solve(new_state) + a + b

            best = min(best, cost)

        return best

    return solve(freqs)
