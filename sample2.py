# if文
apple_price = 200
money = 1000

count = input("りんごを何個買いますか？:")
count = int(count)
total_price = apple_price * count
needed_money = total_price - money
if money > total_price:
    print("購入できました")
    print(("残金は"), money - total_price, ("円です"))
elif money == total_price:
    print("購入できましたが、残金は無しです")
else:
    print(("りんごは買えませんでした。必要な金額は"), str(needed_money), ("円です"))

# format文
print(f"{money=}")
