import random
import string
import re

def generate_unique_id():
    id_chars = string.ascii_letters + string.digits
    # print(id_chars)  abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQpSTUVWXYZ0123456789
    return ''.join(random.choice(id_chars) for _ in range(8))

# margaritaramirez017@correo.cl
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$"
    # re.match('^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$', 'margaritaramirez017@correo.cl')
    return re.match(pattern, email) is not None

def create_registration(name, role):
    return {'name': name, 'role': role, 'unique_id':generate_unique_id(), 'email': ''}
