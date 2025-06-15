"""
MiniBank – Oddiy Banking Simulyatori

Foydalanuvchi yangi hisob ochishi, balansga pul qo‘shishi, pul yechishi
va balansni ko‘rishi mumkin.

Cheklovlar:
- Faqat bitta foydalanuvchi hisobini qo‘llab-quvvatlaydi
- List, dict, class ishlatilmagan
- Ma'lumotlar vaqtinchalik, dastur yopilganda yo'qoladi

"""


from typing import Union

# Global o'zgaruvchilar
name: Union[str, None] = None
balance: Union[float, None] = None

def open_account() -> None:
    global name, balance
    name = input("name = ")
    balance = 0.0

def check_account() -> bool:
    return name is not None and balance is not None

def deposit() -> None:
    global balance
    amount_str = input("Qo'shiladigan summani kiriting: ")
    if not amount_str.replace('.', '', 1).isdigit():
        print("Xatolik: Iltimos, musbat son kiriting.")
        return

    amount = float(amount_str)
    if amount <= 0:
        print("Xatolik: Summani musbat son sifatida kiriting.")
        return

    balance += amount
    print(f"{amount} so'm qo'shildi.")

def withdraw() -> None:
    global balance
    amount_str = input("Yechiladigan summani kiriting: ")
    if not amount_str.replace('.', '', 1).isdigit():
        print("Xatolik: Iltimos, musbat son kiriting.")
        return

    amount = float(amount_str)
    if amount <= 0:
        print("Xatolik: Summani musbat son sifatida kiriting.")
        return
    if amount > balance:
        print("Xatolik: Yetarli mablag' mavjud emas.")
        return

    balance -= amount
    print(f"{amount} so'm yechildi.")

def check_balance() -> None:
    print(f"Hozirgi balans: {balance} so'm")

def main() -> None:
    while True:
        print("\n=== ATM Menyusi ===")
        print("0 - Account yaratish")
        print("1 - Balansni ko'rish")
        print("2 - Pul qo'shish (deposit)")
        print("3 - Pul yechish (withdraw)")
        print("4 - Chiqish")

        tanlov = input("Amalni tanlang (0-4): ")

        if tanlov == "0":
            open_account()
        elif tanlov == "1":
            if check_account():
                check_balance()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "2":
            if check_account():
                deposit()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "3":
            if check_account():
                withdraw()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "4":
            print("Dasturdan chiqildi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov! Iltimos, qaytadan urinib ko'ring.")

# Dastur ishga tushiriladi
main()
