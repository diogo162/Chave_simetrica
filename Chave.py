import random

def generate_key(num_tables, binary_lengths):
    tables = []
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,<>;:+-/\|?!@#$%¨&*()[]{}´`?éáíôÔÉÓÍÁçÇêÊÃãàÀ "

    random.shuffle(binary_lengths)

    for i in range(num_tables):
        key = {}
        binaries = generate_unique_binaries(len(characters), binary_lengths[0])
        assign_binaries_to_characters(key, characters, binaries)
        tables.append((i, key))  
        binary_lengths.pop(0)

    return tables


def generate_unique_binaries(num_binaries, binary_length):
    binaries = set()

    while len(binaries) < num_binaries:
        binary = "{:0{}b}".format(random.randint(0, 2**binary_length - 1), binary_length)
        binaries.add(binary)

    return binaries


def assign_binaries_to_characters(key, characters, binaries):
    characters = list(characters)

    for binary in binaries:
        char = random.choice(characters)
        characters.remove(char)
        key[char] = binary


def encrypt_message(message, keys):
    encrypted_message = ""
    num_tables = len(keys)
    table_id_length = num_tables

    for char in message:
        key_index = random.randint(0, num_tables - 1)
        key = keys[key_index][1]
        if char in key:
            table_id = "{:0{}b}".format(key_index, table_id_length)
            encrypted_message += f"[{table_id}] {key[char]} "  
        else:
            encrypted_message += char + " "  

    return encrypted_message


def decrypt_message(encrypted_message, keys):
    decrypted_message = ""
    binary_lengths = []

    for key in keys:
        binary_lengths += list(set(len(binary) for binary in key[1].values()))
    binary_lengths.sort(reverse=True)

    i = 0

    while i < len(encrypted_message):
        if encrypted_message[i] == '[':  
            end_bracket_index = encrypted_message.index(']', i)
            table_id = int(encrypted_message[i + 1:end_bracket_index], 2)
            key = keys[table_id][1]
            i = end_bracket_index + 2  
        else:
            found = False
            for binary_length in binary_lengths:
                binary_char = encrypted_message[i:i + binary_length]

                if binary_char in key.values():
                    char = next((k for k, v in key.items() if v == binary_char), None)
                    if char:
                        decrypted_message += char
                        i += binary_length + 1  
                        found = True
                        break

            if not found:
                break

    return decrypted_message


def get_user_input(prompt, data_type=str):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")


while True:
    num_tables = get_user_input("Enter the number of tables to generate: ", int)

    table_id_length = num_tables

    binary_lengths = []
    min_length = 8
    max_length = 18

    unique_values = set()
    while len(unique_values) < num_tables:
        binary_length = random.randint(min_length, max_length)
        unique_values.add(binary_length)

    binary_lengths = list(unique_values)

    keys = generate_key(num_tables, binary_lengths.copy())

    show_table = get_user_input("Do you want to display the tables of characters? (Y/N): ", str)
    if show_table.lower() == 'y':
        for i, (table_id, key) in enumerate(keys):
            print(f"Table {table_id + 1} (ID: {table_id}, ID Length: {table_id_length}):")
            print("Character\tBinary")
            for char in key.keys():
                print(char + "\t\t" + key[char])
            print()

    message = input('Enter the message: ')

    encrypted_message = encrypt_message(message, keys)
    print("Encrypted message:", encrypted_message)

    decrypt_option = get_user_input("Do you want to decrypt the message? (Y/N): ", str)
    if decrypt_option.lower() == 'y':
        decrypted_message = decrypt_message(encrypted_message, keys)
        print("Decrypted message:", decrypted_message)

    continue_option = get_user_input("Do you want to continue decrypting? (Y/N): ", str)
    if continue_option.lower() != 'y':
        break
