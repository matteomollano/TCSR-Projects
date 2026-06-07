import random
import string

def generate_strong_password(length=16, num_upper=2, num_lower=4, num_digits=4, num_special=2):
    total_required = num_upper + num_lower + num_digits + num_special
    
    if total_required > length:
        return f"Sum of character counts ({total_required}) is larger than the expected password length ({length})"
    
    password_list = []
    
    for _ in range(num_upper):
        uppercase_letter = random.choice(string.ascii_uppercase)
        password_list.append(uppercase_letter)
       
    for _ in range(num_lower):
        lowercase_letter = random.choice(string.ascii_lowercase)
        password_list.append(lowercase_letter)
        
    for _ in range(num_digits):
        digit = random.choice(string.digits)
        password_list.append(digit)
    
    for _ in range(num_special):
        special_char = random.choice("#$%&()*+;<=>?@^{}~") # (string.punctuation)
        password_list.append(special_char)
    
    num_remaining_chars = length - len(password_list)
    
    all_chars = string.ascii_letters + string.digits + "#$%&()*+;<=>?@^{}~"
    for _ in range(num_remaining_chars):
        char = random.choice(all_chars)
        password_list.append(char)
    
    random.shuffle(password_list)
    
    return "".join(password_list)

if __name__ == "__main__":
    password = generate_strong_password()
    print(password)
    