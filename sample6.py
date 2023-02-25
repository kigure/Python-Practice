# 文字列型
fruit = "apple"
print(fruit)
print(type(fruit))
print(10 * fruit)

fruits = """apple
banana
strawberry
"""
print(fruits)

# count

msg = "ABCDEABC"
print(msg.count("ABCDEABC"))


# startswith, endwith
print(msg.startswith("ABC"))
print(msg.endswith("AE"))

msg = "abcABC"
msg_u = msg.upper()  # 大文字
msg_l = msg.lower()  # 小文字
msg_s = msg.swapcase()  # 大文字小文字の入れ替え
print(msg_u, msg_l, msg_s)

msg = "tomato of tomato"
msg_r = msg.replace("tomato", "banana")
print(msg_r)

msg = "hello world"
print(msg.capitalize())

# 文字列の取り出し,format,islower,isupper

msg = "hello, my name is taro"
print(msg[7:])


print("hello {}".format("taro"))
name = "jiro"
print(f"hello {name}")  # 3.6以上
print(f"{name=}")


# islowerはslowerはすべての文字が小文字だったらtrue isupperはすべての文字が大文字だったらtrue
msg = "appleF"
print(msg.islower())
msg = "apple"
print(msg.isupper())

msg = "ABCDEABC"
print(msg.find("ABC"))
