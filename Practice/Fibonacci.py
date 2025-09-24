length = int(input("Enter how many numbers in the series you want to display: "))

fibo = [0, 1]

i = 2
while(i < length):
    next = int(fibo[i-1]) + int(fibo[i-2])
    fibo.append(next)
    i = i + 1

print(fibo)