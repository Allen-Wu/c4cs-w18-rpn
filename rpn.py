#!/usr/bin/env python3

def calculate(arg):
	stack = list()
	for token in arg.split():
		value = token
		if value == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			return int(arg1) + int(arg2)
		if value == '^':
			arg1 = int(stack.pop())
			arg2 = int(stack.pop())
			result = 1
			for x in xrange(arg1):
				result = result * arg2
			return result
		value = int(token)
		stack.append(token)

def main():
	while True:
		print(calculate(input("rpn calc> ")))

if __name__ == '__main__':
    main()