#!usr/bin/python3
#login to root first
import os

uname = input("enter username ---> ")
if type(uname)==str:
	upass="hello"+uname
	os.system("useradd -p $(openssl passwd -1 "+upass+") "+uname)
	print("user created ! ")
else:
	print("user name is invalid")
