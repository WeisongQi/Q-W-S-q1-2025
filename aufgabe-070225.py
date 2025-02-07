# Überlegt euch ein eigenes Projekt,
# in welchem ihr die Themen login, signup Themen
# mit Verschlüsselung in einem eigenen Projekt anwendet


import hashlib
from cryptography.fernet import Fernet

users_list = []

# 创建和初始化一个 Fernet 加密实例
# 创建一个 32 字节的随机密钥
key = Fernet.generate_key()
# 使用生成的密钥创建一个 Fernet 加密器实例
cipher = Fernet(key)
# 对称加密（使用 AES-128-CBC）
# 消息认证（使用 HMAC-SHA256）
# 内置的时间戳支持（可以设置令牌的有效期）


# 加密函数
def encrypt_value(value):
    return cipher.encrypt(value.encode()).decode()


# 解密函数
def decrypt_value(value):
    return cipher.decrypt(value.encode()).decode()


# 哈希加密函数
def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()


def login(musername, mpassword):
    print(f"My Username: {musername} Password: {mpassword}")
    user = None
    hashed_password = hash_password(mpassword)
    for u in users_list:
        if u["username"] == musername and u["password"] == hashed_password:
            user = u
            break

    if user:
        print("Login successful!")
    else:
        print("Invalid username or password.")
    return user


def signup(musername, mpassword, credit_card):
    for u in users_list:
        if u["username"] == musername:
            print("User exists already, please Login")
            return

    new_user_id = len(users_list) + 1
    hashed_password = hash_password(mpassword)
    encrypted_credit_card = encrypt_value(credit_card)
    users_list.append(
        {
            "id": new_user_id,
            "username": musername,
            "password": hashed_password,
            "credit_card": encrypted_credit_card,
        }
    )


def save_product(musername):
    user = None
    for u in users_list:
        if u["username"] == musername:
            user = u
            break

    if user:
        print(f"Hallo {musername}, you can buy something:")
        product_list = input("I will buy: ")
        encrypted_product_list = encrypt_value(product_list)
        user["product"] = encrypted_product_list
    else:
        print("User not found. Please login first.")


def buy_product(musername):
    user = None
    for u in users_list:
        if u["username"] == musername:
            user = u
            break

    if "product" in user:
        decrypted_product = decrypt_value(user["product"])
        print(f"You have bought: {decrypted_product}")
    else:
        print("No products found.")


def main():
    while True:
        print("1. Sign up")
        print("2. Search product")
        print("3. Buy product")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            musername = input("Enter your username: ")
            mpassword = input("Enter your password: ")
            credit_card = input("Enter your credit card: ")
            signup(musername, mpassword, credit_card)
        elif choice == "2":
            musername = input("Enter your username: ")
            mpassword = input("Enter your password: ")
            user = login(musername, mpassword)
            if user:
                save_product(musername)
        elif choice == "3":
            musername = input("Enter your username: ")
            mpassword = input("Enter your password: ")
            user = login(musername, mpassword)
            if user:
                buy_product(musername)
        elif choice == "4":
            break
        elif choice == "5":
            print(users_list)
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
