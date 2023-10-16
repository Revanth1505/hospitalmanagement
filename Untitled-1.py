def max_sum_contiguous(arr):
    max_sum = float("-inf")
    positive_set = set()
    current_sum = 0

    for x in arr:
        if x > 0:
            positive_set.add(x)
        elif abs(x) in positive_set:
            current_sum += abs(x)
        
        max_sum = max(max_sum, current_sum)

    return max_sum

# Input
n = int(input())
arr = list(map(int, input().split()))

# Calculate and print the maximum sum
result = max_sum_contiguous(arr)
print(result)
