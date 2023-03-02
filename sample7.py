# int str 変換
int_num = 12
print(type(int_num))
str_num = str(int_num)
print(str_num)
print(type(str_num))

float_num = -20.5
print(type(float_num))
str_float = str(float(float_num))
print(str_float)
print(type(str_float))

# floatとintは計算できる！

tall = 168.5
weight = 60
print(type(weight))
print(type(tall))

print(tall + weight)

anime = "悟空"
rival = "ベジータ"

print("ドラゴンボールの主人公は{}ライバルは{}です".format(anime, rival), type(anime))

nashimin = 74
Pi = 3.14

print(type(nashimin), type(Pi))

Pi = str(Pi)

print(type(Pi))

print(Pi + nashimin)
