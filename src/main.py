from registration_management import create_registration, validate_email

def print_menu():
    print("\n1. Comenzar asignación de correos")
    print("2. Listar todos los participantes")
    print("3. Salir")

def main():
    participants = [
        create_registration("Catalina", "Estudiante"),
        create_registration("Sofia", "Docente"),
        create_registration("Elon", "CEO Tesla"),
        create_registration("Richard", "Fundador GNU")
    ]
    print(participants)

main()