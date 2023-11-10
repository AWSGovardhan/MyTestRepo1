# import Mod1 as m #Error
from Mod1 import Prod
from Mod1 import QDiv

# print("Multiplication Result is ::",m.Multiply(5,2)) #Error
# print("Quotient of Division is :: ",m.QDivide(5,2)) #Error

# print("Multiplication Result is ::",m.Prod.Multiply(5,2))#Error
# print("Quotient of Division is :: ",m.QDiv.QDivide(5,2))#Error


print("Multiplication Result is ::",Prod.Multiply(5,2))
print("Quotient of Division is :: ",QDiv.QDivide(5,2))