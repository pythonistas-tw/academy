from models import DBUse

test1 = DBUse()
test1.f_create(account="maomao@gmail.com", password="123321")
test1.f_create(account="hahaha@gmail.com", password="abcd")

user = test1.f_read(uid=2)
test1.f_update(user, account="amy111@gmail.com")

ul = test1.f_read()
for i in ul:
    test1.f_delete(i)

test1.f_read()
