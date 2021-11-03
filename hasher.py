import hashlib
    
#Main function that takes input added to the word-list.txt file and hashes file with SHA-512    
def main():
    words_to_add = int(input("How many words would you like to add to the word-lists: "))
    f = open('word-list.txt','w')
    for i in range(words_to_add):
        add_word = str(input("Add a word: ")).encode('UTF-8')
        f.write('{}'.format(add_word))
        hasher = hashlib.sha512()
        hasher.update(add_word)
        f.write('\n{}\n'.format(hasher.digest()))
        
    f.close()
                
main()
