import hash

password = "pass"

h = hash.hash_password(password)

b = hash.check_password(password, h)

if b == 0:
    print("same")
else:
    print("not same")

b = hash.check_password("wrong", h)

if b == 0:
    print("same")
else:
    print("not same")

