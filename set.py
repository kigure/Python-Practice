# セット型
s = {"a", "b", "c", "d", "e", "f"}
t = {"g", "h", "i", "j", "k", "l"}

# 和集合....ようはセットに入ってるものを全て取り出している。被りがあった場合は二つじゃなくて、一個だけ取り出す。
u = s | t
print(u)

s = {"apple", "banana"}
t = {"apple", "banana", "lemon"}
u = {"cherry"}

# issubsetを使うとsの中にtの中身が被ってるか確認できる。入ってればTrue なければFalse
print(s.issubset(t))  # true
print(u.issubset(t))  # false

# isdisjointを使うと、重なってる要素があればFalseがかえってきて,重なってなければtrueが返ってくる
print(t.isdisjoint(s))
print(t.isdisjoint(u))
