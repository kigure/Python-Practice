# 辞書型について
y = {"a": "x", "y": "c"}
print(y["a"])

car = {"brand": "Toyota", "model": "Yarisu", "price": "10000$", "year": "2016"}
print(car["brand"])
print(car.get("mode", "Does not exist"))
print(car.values())  # 値一覧
print(car.items())  # キーと値の一覧

# dictionaryのメソッドを紹介
# 辞書の名前.update({"":""})で、keyとvalueを追加できる
# リストはappendで辞書はupdate....ややこしい
# updateで追加と更新ができる

car.update({"mileage": "10000km"})
print(car.items())

# キーの中身のvalueを更新するとき
# 下のやり方でもできるし、updateを使って更新することもできる

car["year"] = "2014"
print(car["year"])

car.update({"year": "2009"})
print(car["year"])

# 辞書の削除の仕方について

car.clear()
print(car)

# 変数そのものを消したいときは....

# del car
# print(car)

# # for文ってよくわかんないな....
# for k, v in car.items():
#     print("key = {}, value = {}".format(k, v))

# num = 0
# for num in range(5):
#     print(num)

# apple = 200
# money = 100


# # while 文ってなんだ....?

# # while 条件式:
# #     処理A
# # 処理B

# number = 1

# while number < 10:
#     number += 1   # ここまでが繰り返される条件と処理
# print(number)
# print("終了")      # 条件の結果がFalseになった場合に出力される処理


Me = {"name": "kigure", "from": "Tokyo",
      "gender": "male", "favorite_food": "meat"}
print(Me.get("name"))
Me.update({"hobby": "videos_game"})
print(Me.get("age", "Does not exist"))
