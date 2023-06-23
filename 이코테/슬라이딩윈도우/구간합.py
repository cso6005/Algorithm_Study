numbers = [3, -1, 8, -2, 0, 9, -3]
n = len(numbers)
k = 3
window = sum(numbers[:k])
answer = window
for i in range(3, n):
    window += numbers[i] - numbers[i - k]
    answer = max(answer, window)

print(answer)