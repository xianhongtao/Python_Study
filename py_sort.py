dict = []
input_str = input()
input_dict = input_str.split()
for i in input_dict:
    dict.append(int(i))
dict.sort(reverse=True)
for i in dict:
    print(i, end=' ')
print()
