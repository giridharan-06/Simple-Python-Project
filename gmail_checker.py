def mail_address(address):
    dot=address.find('.')
    at=address.find('@')
    if dot==-1:
        print("Invalid Gmail")
    else:
        print("Valid")

while(True):
    print("Enter the Corret Gmail Address")
    x=input("Enter the gmail address: ")
