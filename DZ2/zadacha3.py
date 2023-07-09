# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions
def findgcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = input("Input num a/b: ").split("/")
num2 = input("Input num c/d: ").split("/")

a = int(num1[0])
b = int(num1[1])
c = int(num2[0])
d = int(num2[1])

resultsum = ""
resultmultuply = ""
# sum
if (b == d):
    if ((a + c) == b):
        resultsum = 1
    else:
        resultsum = (str((a + c)/findgcd(((a*d)+(b*c)),(b*d))) + "/" + str(b/findgcd(((a*d)+(b*c)),(b*d))))
else:
    resultsum = (str(int(((a * d) + (b * c))/findgcd(((a*d)+(b*c)),(b*d)))) + "/" + str(int((b * d)/findgcd(((a*d)+(b*c)),(b*d)))))

print("NO FRACTIONS, sum: " + resultsum)

# multiply
if ((b * d) % (a * c) == 0):
    resultmultuply = (str(int(((a * c) / (a * c))/findgcd(((a*c)),(b*d)))) + "/" + str(int(((b * d) / (a * c))/findgcd(((a*c)),(b*d)))))
else:
    resultmultuply = (str(int((a * c)/findgcd(((a*c)),(b*d)))) + "/" + str(int((b * d)/findgcd(((a*c)),(b*d)))))

print("NO FRACTIONS, multiply: " + resultmultuply)

f1 = fractions.Fraction(int(num1[0]), int(num1[1]))
f2 = fractions.Fraction(int(num2[0]), int(num2[1]))

print("USING FRACTIONS: num1+num2 = " + str(f1 + f2), "num1*num2 = " + str(f1 * f2))





