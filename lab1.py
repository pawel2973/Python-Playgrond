# Hello World
############################################################################################

print("1#")
print("Hello world!")
print("\n2#")

# Printing
############################################################################################
ws = "  "  # white space
vl = "|"  # vertical line
hl = "--------"  # horizontal line

print("{0}{1}{0}{1}{0}".format(ws, vl))
print(hl)
print("{0}{1}{0}{1}{0}".format(ws, vl))
print(hl)
print("{0}{1}{0}{1}{0}".format(ws, vl))
print("\n3#")

# Printing #2
############################################################################################
pt1 = "  |  |  "  # pattern 1
pt2 = "--+--+--"  # pattern 2
pt3 = "========+========+========"  # pt3

for x in range(3):
    print("{0}H{0}H{0}".format(pt1))
    print("{0}H{0}H{0}".format(pt2))
    print("{0}H{0}H{0}".format(pt1))
    print("{0}H{0}H{0}".format(pt2))
    print("{0}H{0}H{0}".format(pt1))
    if x == 0 or x == 1:
        print(pt3)
print("\n4#")

# Fizz, Buzz, FizzBuzz!
# Find the sum of all the multiples of 3 or 5 below 1001.
############################################################################################
suma = 0

for i in range(1, 1001):  # 1 .. 1000
    if (i % 3 == 0) or (i % 5 == 0):
        print(i, end=" ")
        suma += i
print("\nSum of all the multiples of 3 or 5 below 1001: ", str(suma))
print("\n5#")


# Collatz Sequence
############################################################################################
def collatz_seq(n):
    print("collatz_seq(", n, ")")
    suma_n = 0
    while True:
        if (n % 2) != 0:
            n = int(3 * n + 1)
            suma_n += 1
        elif (n % 2) == 0:
            n = int(n / 2)
            suma_n += 1
        if n == 1:  # always ends with 1
            print(n)
            suma_n += 1
            break
        print(n, end=" -> ")
    print("Chain length: ", suma_n, "\n")


# Collatz Sequence
############################################################################################
collatz_seq(13)
collatz_seq(999)  # under 1,000
collatz_seq(999999)  # under 1,000,000
print("6#")


# Fahrenheit-to-Celsius converter
############################################################################################
farenheit = input("Temperature F?: ")
farenheit = float(farenheit)
celcius = round((farenheit - 32)*(5/9), 2)
print("It is", celcius, "degrees Celsius.")

