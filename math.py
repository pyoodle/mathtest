# A simple math equation solver example -

def doMath(equation):
  splitEquation = equation.split('*')
  equationOutside = splitEquation[0]
  equationInside = splitEquation[1]
  equationInsideNumbers = equationInside.split('+')
  number = 0
  
  for equationNumber in equationInsideNumbers:
    number += int(equationOutside)*int(equationNumber)
  
  print(number)

# Example -
# * is ( & )
doMath('3*3+5+3*')
