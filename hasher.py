# The start of a simple python program that hashes the user input for favorite color
# import the python string  module
import string        

# hasher table function that inherits the favorite_color_list
def hasher_table(favorite_color_list):
    # variable that will be used to store the hashed word
    favorite_color_to_password = ""
    # iterator that goes through each letter
    for i in favorite_color_list:
        # Basic algorithm that is the key to finding the proper character within the string module printable characters feature 
        i = int((i/4)*2)
        # variable j is equivalent to the location of the integer i within the string.printable list
        j = string.printable[i]
        # Incrementor for the favorite_color_to_password empty string
        favorite_color_to_password = favorite_color_to_password + j
    
    # printed value of favorite_color_to_password for the user to see.
    print(favorite_color_to_password)

# Main function that stores the required user input variable, favorite_color_list, and both function calls
def main():
    # User input required on favorite color
    favorite_color = str(input("What is your favorite color? "))
    # print the favorite color for testing purposes
    print(favorite_color)
    # empty list for the favorite color's letters
    favorite_color_list = []
    # for loop that goes through each individual letter
    for i in favorite_color:
        # the iterators value i is converted to an ordinal value and appended to the favorite color list.
        favorite_color_list.append(ord(i))
    
    
    # Print Favorite Color List
    print("Ordinal Values for your favorite color are: {0}".format(favorite_color_list))
    # hasher table function that inherits the favorite_color_list            
    hasher_table(favorite_color_list)
    
main()