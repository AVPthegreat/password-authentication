import getpass
data = {"code.infinity":"12345","infinity.code":"789"}
username = input('ENTER YOUR USERNAME ')
password = getpass.getpass('ENTER YOU PASSWORD ')
for i in data.keys():
  if username == i:
    while password != data.get(i):
      password=getpass.getpass('WRONG PASSWORD..!!!, ENTER YOUR PASSWORD AGAIN')
    break
print("USER ID VERIFIED")