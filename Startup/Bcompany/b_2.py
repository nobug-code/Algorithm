def max_inversions(prices):
    # Initialize result
    invcount = 0

    for i in range(1, len(prices) - 1):
        small = 0
        for j in range(i + 1,  len(prices)):
            if prices[i] > prices[j]:
                small += 1

        big = 0;
        for j in range(i - 1, -1, -1):
            if prices[i] < prices[j]:
                big += 1

        invcount += big * small

    return invcount

# 문제 설면
# 3게를 순서대로 놓을 수 있는 것의 갯수를 구하는 것.
prices = [15, 10, 1, 7, 8]
print(max_inversions(prices))