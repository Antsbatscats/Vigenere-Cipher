import random
import string

# First one needs to create a base array so that an alphapbet can be converted into numbers simply
Alphabet_base = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".","/","?",",","|","¬","`","!","£","$","%","^","&","*","(",")","-","_","=","+","#","~","<",">",":",";","@","[","]","{","}","1","2","3","4","5","6","7","8","9","0"]

# key generator 
def get_random_string(length):
    global result_str
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    
# Now for the encryptor
def encryption(msge): 
    lst = [*msge] # breaks the given message into characters and whitespaces 
    alpha_position = [] # holds the final position fo each of the inputed message charcters
    length = len(lst) # gets the full charcter length of the inputed message

    get_random_string(length) # creates a random string based on the length of the inputed message

    key = str(result_str)  # sets the given variable key to the newly created key in a string formatBREAKDE
    key_lst = [*key] # breaks the key into a ist of characters
    key_position = [] # sets a variable known as key_position to hold the index values of the key's characters

    cipher_position = [] # holds the values of the cipher's index values
    cipher_text_individual = [] # holds each of the actual characters in the cipher

    for x in range(0,length): # repeats this action for the number of characters in the message
        num_location = Alphabet_base.index(lst[x]) # gets the index value of the messages's charcters's values within the given alphabet
        alpha_position.append(num_location) # this is then put into a list to be held 
        print(alpha_position)
        

    for x in range(0,length): # repeats this action for the number of characters in the message
        num_key_location = Alphabet_base.index(key_lst[x]) # gets the index value of the key's charcters's values within the given alphabet
        key_position.append(num_key_location) # this is put into a list to be held
        print(key_position)
        

    for x in range(0,length): # repeats this action for the number of characters in the message
        new_num_cipher = (alpha_position[x] + key_position[x]) % len(Alphabet_base) # the given index of the plain text charcter is add to the index of the corresponding key character, this is then placed against the length of the alphabet. If it is longer than it - then number is dvided by 26 and the reminder is used. 
        cipher_position.append(new_num_cipher) # these new index values are placed into a new list
        print(cipher_position)
       
     
    for x in range(0,length): # repeats this action for the number of characters in the message
        cipher_character = Alphabet_base[cipher_position[x]] # the cipher indexes made are then converted into there alphabet equivelents
        cipher_text_individual.append(cipher_character) # these are then held within a new list
        print(cipher_text_individual)
    
    cipher = ''.join(cipher_text_individual) # the list is then joined together into a single string
    print(f'key: {key}') # the key s printed
    print(f'plain text message: {msge}') # the original msg is printed
    print(f'encrypted message: {cipher}') # the encrypted msg is printed
        
def decryption(msgd,key): # the msg and key variables must be inputed into the defined function decryption 
    cipher = [*msgd] # the cipher is split into its characters and assigned into a list
    key_lst = [*key] # the key is split into its characters and assigned into a list
    length = len(cipher) # the length of the cipher is assigned to 'length'

    cipher_position = [] # a variable called cipher_position holds the indexes of the cipher. 
    
    key_position = [] # a variable called key_position holds the indexes of the key

    true_alpha_position = [] # this is the list that holds the true indexes of the original msg

    msg_true = [] # the list that holds the characters found in the list

    for x in range(0,length): # repeats this action for the number of characters in the message
        num_cipher_location = Alphabet_base.index(cipher[x]) # gets the index value of the cipher's charcters's values within the given alphabet
        cipher_position.append(num_cipher_location) # this is put into a list to be held
        print(cipher_position)

    for x in range(0,length): # repeats this action for the number of characters in the message
        num_key_location = Alphabet_base.index(key_lst[x]) # gets the index value of the key's charcters's values within the given alphabet
        key_position.append(num_key_location) # this is put into a list to be held
        print(key_position)
    
    for x in range(0,length): # repeats this action for the number of characters in the message
        true_alpha = ((cipher_position[x] - key_position[x]) + len(Alphabet_base)) % len(Alphabet_base) # the index of the key is taken away form the index of the cipher - to reverse the original addition. Then the adition length of the alphabet is added to remove the warpping that occured during the originall modding. Finally the whole thing is moddded to bring thr true index of the plain text character back.
        true_alpha_position.append(true_alpha) # this is then added to a list to be heldbr
        print(true_alpha_position)
    
    for x in range (0,length): # repeats this action for the number of characters in the message
        true_text = Alphabet_base[true_alpha_position[x]] # the original indexes of the plain text characters are then referenced aginst the original alphabet to show the actual character
        msg_true.append(true_text) # these characters are then stored in a list
        print(msg_true)
    
    plain_text = ''.join(msg_true) # the original msg is put together using the .join() function

    print(f'key: {key}') # the key is printed
    print(f'encyrpted message: {msgd}') # the encrypted msg is printed
    print(f'plain text message: {plain_text}') # the plain text msg is printed

while True: 
    cmd = str(input("""What would you Like to do: 
                        1) enter 'EN' to encrypt a message
                        2) enter 'DE' to dectrypt a message
                        3) enter 'RN' to create a random of string of your chosen length
                        4) enter 'BREAK' to kill the system
                        
                        cm>_<: """))
    if cmd == 'EN':
        msge = str(input("Enter a msg to be encrypted: "))
        encryption(msge)

    elif cmd == 'DE':
        msgd = str(input("Enter a msg to be decrypted: "))
        key = str(input("Enter the key the msg was encoded with: "))
        decryption(msgd,key)
    
    elif cmd == 'RN': 
        length_u = int(input("Enter the length of the random string: "))
        get_random_string(length_u)
        print(result_str)
    
    elif cmd == 'BREAK':
        print("System shutdown initiated")
        break
    
    else: 
        print("That is an unkown command!")