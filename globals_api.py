#global Api variables
import random
base_url = "https://thinking-tester-contact-list.herokuapp.com"
get_contact = "https://thinking-tester-contact-list.herokuapp.com/contacts/"
get_contactlist = "https://thinking-tester-contact-list.herokuapp.com/contacts"
post_contact = "https://thinking-tester-contact-list.herokuapp.com/contacts"
put_contact = "https://thinking-tester-contact-list.herokuapp.com/contacts/"
patch_contact = "https://thinking-tester-contact-list.herokuapp.com/contacts/"
delete_contact = "https://thinking-tester-contact-list.herokuapp.com/contacts/"

post_user = "https://thinking-tester-contact-list.herokuapp.com/users"
delete_user = "https://thinking-tester-contact-list.herokuapp.com/users/me"

def generateEmail():
    randNum = random.randint(1, 10)
    randWord = "Test"
    for i in range(randNum):
        randWord += random.choice(["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    email = f"0{randWord}0{randNum}0{randWord}0{randNum}0@gmail.com"

    return email

firstName = "Test"
lastName = "Name"
password = "mypassword"