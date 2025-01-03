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


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci(10):
    print(num)


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
# with open("test.txt", "w") as f:
#     f.write("Hello World")
#     print("Datei wurde geschrieben")
# print("Datei wurde geschlossen")

# # 读取文件内容
# with open("test.txt", "r") as f:
#     content = f.read()
#     print(content)

# # 读取一行
# with open("test.txt", "r") as f:
#     line = f.readline()
#     print(line)

# # 读取所有行
# with open("test.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)

# # 写入多行
# with open("test.txt", "w") as f:
#     f.writelines(["Hello World\n", "This is a test\n"])

# # 移动文件指针
# with open("test.txt", "r") as f:
#     f.seek(6)
#     print(f.read())  # 从第6个字节开始读取

squares = [x * x for x in range(10)]
print(
    squares
)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]even_numbers = [x for x in range(10) if x % 2 == 0]
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # 输出: [0, 2, 4, 6, 8]
pairs = [(x, y) for x in range(3) for y in range(3)]
print(
    pairs
)  # 输出: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 创建 Git 命令词典
git_commands = {
    "init": "创建一个新的 Git 仓库",
    "clone": "克隆一个现有的仓库",
    "status": "显示工作目录的状态",
    "add": "将文件添加到暂存区",
    "commit": "提交暂存区的文件",
    "push": "将本地提交推送到远程仓库",
    "pull": "从远程仓库拉取更新并合并",
    "branch": "列出、创建或删除分支",
    "checkout": "切换到指定的分支或提交",
    "merge": "合并指定的分支到当前分支",
    "log": "显示提交日志",
    "diff": "显示提交之间的差异",
    "reset": "重置当前分支到指定状态",
    "rm": "从工作目录和暂存区中删除文件",
    "stash": "暂存当前工作目录的修改",
    "rebase": "将当前分支的更改应用到另一个分支上",
}


# 查询 Git 命令描述的函数
def query_git_command(command):
    return git_commands.get(command, "未知的 Git 命令")


# 示例查询
if __name__ == "__main__":
    command = input("请输入要查询的 Git 命令: ")
    description = query_git_command(command)
    print(f"{command}: {description}")
