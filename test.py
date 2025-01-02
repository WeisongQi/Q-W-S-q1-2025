# user1 = {"password": "1234", "email": "1234@qq.com"}
# user2 = {"password": "3456", "email": "234@qq.com"}

# user_list = [user1, user2]

# print(user_list[0]["password"])
# print(user_list[1]["email"])
# print(user_list[0].keys())
# print(user_list[0].values())
# print(user_list[0].items())

# for i in range(5):
#    print(i)

# list1 = [1, 2, 3, 4, 5]

# # sum = list1[0] + list1[1] + list1[2] + list1[3] + list1[4]

# print(sum(list1))

# garad_list1 = []
# ungerade_list1 = []

# for i in range(len(list1)):
#     if list1[i] % 2 == 0:
#         garad_list1.append(list1[i])
#     else:
#         ungerade_list1.append(list1[i])
#         print(f"{list1[i]} ist ungerade")
# print(garad_list1)
# print(ungerade_list1)


# max_value = max(list1)
# print(f"Der größte Wert in list1 ist: {max_value}")


# def ungerade(list1):
#     return [x for x in list1 if x % 2 != 0]


# print(ungerade(list1))

# thislist = [100, 50, 65, 82, 23]
# print(thislist)
# thislist.sort(reverse=False)
# print(thislist)


# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b


# # for num in fibonacci(10):
# #     print(num)


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Funktion wird ausgeführt")
#         # print("vorher")
#         return func(*args, **kwargs)
#         # print("nachher")

#     return wrapper


# @decorator
# def greet(name):
#     print(f"Hello {name}")


# greet("Max")

# context Managers
with open("test.txt", "w") as f:
    f.write("Hello World")
    print("Datei wurde geschrieben")
print("Datei wurde geschlossen")

# 读取文件内容
with open("test.txt", "r") as f:
    content = f.read()
    print(content)

# 读取一行
with open("test.txt", "r") as f:
    line = f.readline()
    print(line)

# 读取所有行
with open("test.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# 写入多行
with open("test.txt", "w") as f:
    f.writelines(["Hello World\n", "This is a test\n"])

# 移动文件指针
with open("test.txt", "r") as f:
    f.seek(6)
    print(f.read())  # 从第6个字节开始读取
