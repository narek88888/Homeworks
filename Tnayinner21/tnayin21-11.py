# 21-11. Function Exercise:
# Write a function that checks if a given string is a valid email address.


def email_chechker(mail):

    letters = "qwertyuiopasdfghjklzxcvbnm"

    for i in letters:
        if i in mail and "@" in mail[i :] and "."+ i in mail["@" :] :
            print("Yes")
        else:
            print("No")

print(email_chechker("nar@mail.ru"))