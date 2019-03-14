# Reverse Integer

class Solution:
	def reverse(self,x):
		temp = 0
		output = 0
		l = list(str(abs(x)))

		if x <0:
			output = -int(''.join(l[::-1]))
		else:
			output = int(''.join(l[::-1]))
		return output if -(2**31)-1 < output < 2**31 else 0