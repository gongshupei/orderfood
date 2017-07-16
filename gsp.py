# add comments
#coding=utf-8
def translatefile(inputstring):
    gbk = inputstring.decode("UTF-8")
    return gbk.encode("GBK")

print translatefile("欢迎点餐")
dialogue = translatefile("菜单：   套餐： 1 牛肉饭套餐（牛肉饭1碗，紫菜蛋花汤1碗，土豆泥1份) 18元； 2 猪肉贩套餐（猪肉饭1碗，紫菜蛋花汤1碗，土豆泥1份) 15元；  主食： 3 牛肉饭 15元； 4猪肉饭 12元；  小菜： 5土豆泥 2元；  6咸菜1 元   饮料： 7紫菜蛋花汤 2元； 8可乐 3元")
print dialogue

bills = 0

lists = "菜单如上"

continueOrderFlag = True

x=1.0

# 2**3
# x**y


print x/3
while continueOrderFlag == True :
    print continueOrderFlag
    selection = raw_input(translatefile("输入一个您想要的食物的序号"))
    selection1 = raw_input(translatefile("您想要几份"))
    
    if int(selection) == 1:
        lists = "牛肉饭套餐*" + str(int(selection)) + ";" + lists
        print "==============================="
        print "Lists= " + translatefile(lists)
        print "=============================="
        pay = 18
    if int(selection) == 2:
        lists = ("猪肉饭套餐*" + selection1 + ";" + lists)
        pay = 15
    if int(selection) == 3: 
        lists = ("牛肉饭*" + selection1 + ";" + lists)
        pay = 15
    if int(selection) == 4:
        lists = ("猪肉饭" + selection1 + ";" + lists)
        pay = 12
    if int(selection) == 5:
        lists = ("土豆泥；" + selection1 + ";" + lists)
        pay = 2
    if int(selection) == 6:
        lists = ("咸菜；" + selection1 + ";" + lists)
        pay = 1
    if int(selection) == 7:
        lists = ("紫菜蛋花汤；" + selection1 + ";" + lists)
        pay = 2
    if int(selection) == 8:
        lists = ("可乐；" + selection1 + ";" + lists)
        pay = 3
    bill = pay * int(selection1)
    choose = raw_input(translatefile("您还想要继续点餐吗？ t：是 f：不是"))
    if choose == "t\r":
        continueOrderFlag = True
        bills = bill + bills
    if choose == "f\r":
        continueOrderFlag = False
        bills = bill + bills




    

print translatefile(str(bills)+"元")
print translatefile(lists)
print translatefile("谢谢惠顾")


    
    




