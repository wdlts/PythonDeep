a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

if (a+b)>c or (a+c)>b or (b+c)>a:
    print("Triangle exists")
else:
    print("Triangle DOES NOT exist")

if (a!=b and b!=c):
    print("Triangle is scalenous")
elif(a==b and b==c):
    print("Triangle is equiangular")
elif(a==b or a==c or b==c):
    print("Triangle is isosceles")