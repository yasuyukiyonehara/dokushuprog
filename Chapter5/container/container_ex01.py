colors = ["purple","orenge","green"]

guess = input("何色でしょう？（入力してください）：")

if guess in colors:
    print("当たり！")
else:
    print("ハズレ！残念！")