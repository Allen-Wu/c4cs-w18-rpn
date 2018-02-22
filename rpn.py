#!/usr/bin/env python3

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(token)
		except ValueError:
			if value == '+':
				arg1 = stack.pop()
				arg2 = stack.pop()
				return int(arg1) + int(arg2)
			if value == '^'
				arg1 = stack.pop()
				arg2 = stack.pop()
				result = 1
				for x in range(1, arg2)
					result = result * arg1
				return result
def main():
	while True:
		print(calculate(input("rpn calc> ")))

if __name__ == '__main__':
    main()