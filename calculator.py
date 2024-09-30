operation  = str(input('enter operation:'))

# the operations #
add = "+"
sub = "-"
mult = "*"
div = "/"
expo = "**"

num_1 = int(input('enter first number'))
num_2 = int(input('enter second number'))


if operation == add:
 print(num_1+num_2)

elif operation == sub:
  print(num_1-num_2)

elif operation == mult:
  print(num_1 * num_2)

elif operation == div:
 print(num_1 / num_2)

elif operation == expo:
  print(num_1 ** num_2)