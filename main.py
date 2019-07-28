

introductionStr = "同意請輸入1 不同意請輸入2 輸入後請輸入enter  所有人結束後請輸入3"

yesN = 0
noN = 0
ck=1
inputNumber = 0

while ck==1:
    inputNumber = int(input(introductionStr))
    if inputNumber == 1:
        yesN= yesN + 1
    elif inputNumber == 2:
        noN = noN + 1
    elif inputNumber == 3:
        ck = 0
    else :
        print("打錯了啦幹重打")

print("yes = " +  str(yesN) )
print("no = " +  str(noN) )






