def read(n: int, book: [int], target: int) -> str:
	d = {}
	for i in range(n):
		if book[i] not in d:
			d[book[i]] = 1
		else:
			d[book[i]] += 1

		if target - book[i] == 0:
			return "No"

		if (target - book[i]) in d:
			return "YES"
	else:
		return "NO"

print(read(2,[1,2],1))