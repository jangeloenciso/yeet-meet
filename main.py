from chrome import *
import getpass

MAIL_ADDRESS =  input("Email: ")
PASSWORD = getpass.getpass()
meet_link = input("Meet link: ")
start(meet_link, MAIL_ADDRESS, PASSWORD)