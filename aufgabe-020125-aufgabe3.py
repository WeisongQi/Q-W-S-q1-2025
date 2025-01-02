a = int(input("Bitte geben Sie eine Zahl ein: "))
b = int(input("Bitte geben Sie eine weitere Zahl ein: "))
count_ungerade = 0
sum_ungerade = 0

if a > b:
    a, b = b, a

for i in range(a, b + 1):
    if i % 2 != 0:
        count_ungerade += 1
        sum_ungerade += i

print("Anzahl der ungeraden Zahlen:", count_ungerade)
print("Summe der ungeraden Zahlen:", sum_ungerade)
