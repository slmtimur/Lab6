posl = input("Введите последовательность скобочек: ")
sums = [0]
ind = 0
for i in range(len(posl)):
    if posl[i] == "(":
        sums.append(sums[-1] + 1)
    else:
        sums.append(sums[-1] - 1)
    
    if sums[-1] < 0:
        print("Это неправильная последовательность, ", i)
        quit()

if sums[-1] == 0:
    print("Это правильная последовательность")
else:
    for i in range(len(sums) - 1, 0, -1):
        if sums[i - 1] == 0:
            print("Это неправильная последовательность, ", i - 1)
            quit()