def bingo_turn(N: int, K: int, grid: list[list[int]], called_numbers: list[int]) -> int:
    pass

#bingo_turn()
grid, called_numbers = [], []

#N
N = int(input())

print()

#
for __ in range(N):
    low=[]
    for _ in range(N): low.append(int(input()))
    grid.append(low)

print()

#K
K = int(input())

print()

#
for _ in range(K): called_numbers.append(int(input()))

#K
print(f"\nN: {N}\nGrid: {grid}\nK: {K}\nCalled numbers: {called_numbers}")


bingo_turn(N, K, grid, called_numbers)