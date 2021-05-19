# Valid Parentheses


def isValid(s: str) -> bool:
		# if s empty
		if not s:
			return True

		# data structure: stack
		stack = []

		# database
		left = ['(','{','[']
		right = [')','}',']']

		# enumerate string
		for char in s:
			# store the relevant right part
			if char in left:
				stack.append(right[left.index(char)])

			# empty or doesn't find
			else:
				if not stack or stack.pop() != char:
					return False

		# empty: True | not empty: False        
		return False if stack else True


print(isValid("()[]{}[]"))
print(isValid("([]{()})"))
print(isValid("((]"))
