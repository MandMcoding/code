# 258
class Solution:
	def addDigits(self, num: int) -> int:
		target = num
		while(target <= 9):
			print(target)
			target = target % 10
			print(target)
			temp = target // 10
			print(temp)
			target = target + temp
			print(target)
		return target
sol = Solution()
sol.addDigits(38)

solution = Solution()
num = 38  # Replace with your input
result = solution.addDigits(num)
print(f"The result of addDigits({num}) is: {result}")
