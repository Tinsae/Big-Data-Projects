def encode_decode(key, string, enc=True):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        if enc:
            encdec_c = chr(ord(string[i]) + ord(key_c) % 256)
        else:
            encdec_c = chr(ord(string[i]) - ord(key_c) % 256)

        encoded_chars.append(encdec_c)
    encoded_string = "".join(encoded_chars)
    return encoded_string



import base64
while(True):
    print("Enter 1 to encode")
    print("Enter 2 to decode")
    print("Enter 3 to exit ")
    choice = int(input())
    if(choice == 1):
        ref_id = input("Enter Reference ID: ")
        # allows @, _, numbers and english letters
        rem = ref_id.replace("@", "")
        rem = rem.replace("_", "")
        # invalid if it contains non alphanumeric characters
        # or if length is not 12
        if len(ref_id) != 12 or not rem.isalnum() :
            print("Invalid Reference ID", len(ref_id))
        else:
            encoded = encode_decode("jumbo!!", ref_id, enc=True)
            print("Here is the encoded string => ", encoded)
            print()
            
    elif(choice == 2):
        ref_id = input("Enter Encrypted String: ")
        decoded = encode_decode("jumbo!!", ref_id, enc=False)
        print("Here is the decoded string => ", decoded)
        print()
    elif(choice == 3):
        break;
    else:
        print("invalid input\n")
        