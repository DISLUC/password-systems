print("SECURED LOGIN")
#saves the typed-in username and password
username = input("Username > ")
password = input("Password> ")
#make it any name you want
if username == "Luc" and password == "password":
  print("Welcome Luc!")
elif username == "Suzanne" and password == "su74nne":
  print("hey there Suzanne!")
#when the above name or password dont match it will execute the else command
else:
  print("go away!")