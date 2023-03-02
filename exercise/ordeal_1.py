num = 10
print(type(num))

num_str = str(num)
num_list = [num_str, "20", "30"]
num_list.append("40")

print(num_list)

num_tuple = tuple(num_list)

val = input()
num_tuple += (val,)

num_set = {"40", "50", "60"}

print('num_tuple = {}'.format(num_tuple))
print('num_set = {}'.format(num_set))

set = set(num_tuple)

print(set | num_set)
