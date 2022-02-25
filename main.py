from chrome import *
from firefox import *
import getpass

MAIL_ADDRESS =  input("Email: ")
PASSWORD = getpass.getpass()
meet_link = input("Meet link: ")
chrome(meet_link, MAIL_ADDRESS, PASSWORD)
