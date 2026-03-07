nums = [8, 6, 10, 2, 5]

def buyAndSell(prices):
    minNum = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        tempProfit = prices[i] - minNum
        profit = max(profit, tempProfit)
        minNum = min(minNum, prices[i])
    return profit

print(buyAndSell(nums))