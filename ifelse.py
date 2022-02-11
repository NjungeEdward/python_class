#login program 
username=str(input("Enter username:"))
password=int(input("Enter password:"))

logins=["Edward",2022]
if username in logins and password in logins:
  print("login successful")
else:
  print("login unsuccessfull")
