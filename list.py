# リスト型について
# リストには複数の値を入れることができるよ
# 値の間にカンマをつけて区切るのが条件
# リスト型を使うときは[] を使うこと
# リスト型の中には整数の中に文字を混ぜてもOK(ただし""で文字を囲うこと!)

# list_age = [1, 2, "apple", 4]
# print(list_age[0])
# print(list_age[1])
# print(list_age[2])

# list_base = ["高木慎", "木暮和夫", "木暮海斗", "塩津宏輝"]
# print(list_base[0], list_base[3])

# list_base = ["高木慎", "木暮和夫", "木暮海斗", "塩津宏輝", [1, 2, 3]]
# print(list_base[4][2])
# list_base[2] = "山田太郎"
# print(list_base[2])
# print(list_base)

# list_base[4][0] = "西村ひろゆき"
# print(list_base)

# list_base[4][1] = "山田健太郎"
# list_base[4][2] = "佐藤隆"
# print(list_base)
# print(list_base[-2])


list_base = ["高木慎", "木暮和夫", "木暮海斗", "塩津宏輝"]
print(list_base[0:3])
print(list_base[3:])

# appendはリストに要素を追加するときに使います
# appendは一番使う関数だよ
list_base.append("山田久志")
print(list_base)
list_base.clear()
print(list_base)

list_fruits = ["apple", "orange", "grape", "strawberry", "pineapple"]
print(list_fruits)

# list_fruits.remove("apple")

# print(list_fruits)

# print(list_fruits.count("apple"))

# list_fruits.append("apple")
# print(list_fruits)

# print(list_fruits.count("apple"))

# list_fruits.remove("apple")

# print(list_fruits)

# list_fruits.reverse()
# print(list_fruits)

list_fruits = ["apple", "orange", "grape", "strawberry", "pineapple"]
list_fruits.reverse()
print(list_fruits)


def win():
    list_base = ["高木", "木暮", "塩津", "武藤", "中本"]
    print("高木" in list_base)  # True

    list_base.append("城之内")
    print(list_base)

    list_base.clear()
    list_base.append("高木")
    print(list_base)
    return win


def add(a, b, c):
    x = a * b + c
    return x


x = add(7, 4, 5)
print(x)


def My_friends():
    list_friends = ["macaron", "kaede", "sora", "minayo"]
    print(list_friends)
    new_friend = input("Enter your friends:")
    list_friends.append(new_friend)
    print(list_friends)


My_friends()
