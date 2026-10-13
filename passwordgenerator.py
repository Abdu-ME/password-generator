import secrets
import string

def generate_password(Length=12):
    if Length < 3:
        raise ValueError("Password must be atleast 3 characters")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(punctuation),
    ]
    all_chars = lower + upper + digits + punctuation
    for _ in range(Length-3):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)

def main():
    try:
        length = int(input("How long do u want ur password to be\n"))
        print(f"Your password\n{generate_password(length)}")
    except ValueError as e:
        print(f"Invalid input\n{e}")
if __name__ == "__main__":
    main()