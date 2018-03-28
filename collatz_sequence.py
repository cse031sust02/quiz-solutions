'''
The Collatz Sequence
src : https://automatetheboringstuff.com/chapter3/
'''

# [START collatz]
def collatz(number):
	number = int(number)

	if number%2 == 0:
		result = number//2
	else: 
		result = 3 * number + 1

	print(result)
	return result
# [END collatz]

input = input('please input a integer : ')
output = collatz(input)

while output != 1:
	output = collatz(output)