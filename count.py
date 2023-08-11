password = 'pbkdf2:sha256:600000$ur52OZ1pbmIhFuu2$ffc6d066f228350d66f8871f39c3df04be73e2f3da53e1393bf4d29de522a703'
#l_password = list(password)


password_str = ""
for char in password:
    if char != "$":
        password_str += char

print(password_str)