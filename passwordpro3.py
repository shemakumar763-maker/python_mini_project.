def check_password(password):
    if len(password) >=25:
        print("strong password")
    else:
        print("weak password")
check_password("mysecretpassword")
       