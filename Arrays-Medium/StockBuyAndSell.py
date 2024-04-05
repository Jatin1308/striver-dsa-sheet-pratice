def bestTimeToBuyAndSellStock(prices: [int]) -> int:
	minSoFar = float("inf")
	maxProfit = float("-inf")

	for x in prices:
		minSoFar = min(x,minSoFar)
		maxProfit = max(maxProfit,abs(minSoFar-x))
	return maxProfit


print(bestTimeToBuyAndSellStock([3,1,4,8,7,2,5]))

