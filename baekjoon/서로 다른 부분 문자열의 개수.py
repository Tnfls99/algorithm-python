input = input()
string = set()

for i in range(len(input)):
    for k in range(i, len(input)):
        string.add(input[i:k+1])

print(len(string))
