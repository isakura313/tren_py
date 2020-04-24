unc_users = ['pavel', 'petr', 'semen']
ban_users = set(unc_users)
# print(mnog)
name = input(" Введите ваше имя")
if name in ban_users:
    exit()
else:
    print("ну привет")

