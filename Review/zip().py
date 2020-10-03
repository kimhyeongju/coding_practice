# zip()
dates = ['월','화','수','목','금','토','일']
food = ['갈비탕','순대국','칼국수','삼겹살']
price = [5000,4000,3000,6000]

menu =zip(dates,food,price)

for d,f,p in menu:
    print(f"{d}요일 메뉴: {f}, {p}원",'\n')


# dict(zip())
menu_dic = dict(zip(dates,food))
print(menu_dic,'\n')