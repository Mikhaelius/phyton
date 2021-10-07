#simple calc

def operateCalc():
  first = ''
  second = ''
  operator  = ""

  while first == '':
    try:
      first = int(input("Enter first Number."))
    except ValueError:
      first = ''

  while second == '':
    try:
      second = int(input("Enter first Number."))
    except ValueError:
      second = ''

  while operator == "":
    operator = input("Enter a valid operator (+-*/).")
    if operator != "+" and operator != "-" and operator != "*" and operator !="/":
      operator = ""
  #print(first)
  return first ,second ,operator

def calculate():
  data = operateCalc()
  first, second, operator = data

  if operator == '+':
    print(first + second)

  if operator == '-':
    print(first - second)

  if operator == '*':
    print(first * second)

  if operator == '/':
    print(first / second)
  
  calculate()
calculate()