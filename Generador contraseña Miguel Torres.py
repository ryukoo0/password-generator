import random
import string
def generate_password (longitud= 10):
    caracteres= string.ascii_letters+string.digits+string.punctuation
    password= "".join(random.choice(caracteres)for _ in range(longitud))
    return password
new_password= generate_password ()
print(f"su contraseña es: {new_password}")

