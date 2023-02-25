# 自動販売機
# 投入した金額がジュースの値段以下の場合にtrue それ以外はfalse
# trueの場合はジュースが出て、falseはジュースは出ずに足りない金額を告知
# ジュースの値段より多く金額が投入された場合は、ジュースが出てかつ money - JUICE の値が出力

JUICE = 150
money = input("いくら入れますか?:")
money = int(money)

if money > JUICE:
    print("ジュースゲット")
    print(str(money - JUICE) + "円のお釣りです")
elif money == JUICE:
    print("ジュースゲットお釣りなし")
else:
    print("ジュースは出ません")
    print(str(JUICE - money) + "円足りません")
