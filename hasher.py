import hashlib
    
#Main function that takes input added to the word-list.txt file and hashes file with SHA-512    
def main():
    words_to_add = str(input("Please enter a phrase to hash with SHA-512: "))
    f = open('word-list.txt','w')
    words_to_add = words_to_add.encode('UTF-8')
    f.write('{}'.format(words_to_add))
    hasher = hashlib.sha512()
    hasher.update(words_to_add)
    f.write('\n{}\n'.format(hasher.digest()))
        
    f.close()
                
main()
