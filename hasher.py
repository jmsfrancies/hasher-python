import hashlib

def hash_username_and_password(user_name,password):
    hasher_1 = hashlib.sha1()
    hasher_2 = hashlib.sha1()
    hasher_1.update(user_name)
    hasher_2.update(password)
    hasher_1.digest()
    hasher_2.digest()
    print("hashed username: {0}\nhashed password: {1}".format(hasher_1.hexdigest(),hasher_2.hexdigest()))
    
    
def main():
    user_name = str(input("Please enter your preferred username: "))
    password = str(input("Please enter your password (Must be between eight to fifteen characters): "))
    if len(password) >= 8 and len(password) <= 15:
        hash_username_and_password(user_name.encode('utf-8'),password.encode('utf-8'))
        print("%s \n%s"%(user_name,password))
    else:
        print("Please enter a different password that fulfills the condition of eight to fifteen characters:")
main()
