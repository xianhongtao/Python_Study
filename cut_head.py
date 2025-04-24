print ("请输入一个整数：")
input_number = int(input())
print ("请输入要消除的数位：")
cut_head = int(input())
var1 = input_number
var2 = 0
lenth = 0
while var1 != 0:
    lenth += 1
    var1 = var1 // 10
var2 = 10 ** (lenth - cut_head)
print(input_number % var2)