import os
import random
import string

def generate_random_text():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

def main():
    data_directory = '/serverdata'
    file_path = os.path.join(data_directory, 'random.txt')



    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = file.read()
            print(existing_data)

    new_data = generate_random_text()
    print(new_data)

    with open(file_path, 'w') as file:
        file.write(new_data)

if __name__ == "__main__":
    main()
