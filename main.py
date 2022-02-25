from chrome import *
from firefox import *
import getpass

MAIL_ADDRESS =  input("Email: ")
PASSWORD = getpass.getpass()
meet_link = input("Meet link: ")
browser = int(input("[1] Chrome \n [2] Firefox"))

if browser == 1:
    chrome(meet_link, MAIL_ADDRESS, PASSWORD)
else:
    firefox(meet_link, MAIL_ADDRESS, PASSWORD)