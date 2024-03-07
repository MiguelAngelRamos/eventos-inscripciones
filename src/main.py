from registration_management import create_registration, validate_email

def print_menu():
    print("\n1. Comenzar asignación de correos")
    print("2. Listar todos los participantes")
    print("3. Salir")

def assign_email(registration):
    print(f"\n Asignando un correo para: {registration['name']} ({registration['role']})")
    while True:
        email = input("Introduce el electrónico: ")
        if validate_email(email):
            registration['email'] = email
            print(f"Registro actualizado: {registration}")
            break
        else:
            print("El correo electronico es invalido. ")

def list_participants(participants):
    for registration in participants:
        print(registration)

def main():
    participants = [
        create_registration("Catalina", "Estudiante"),
        create_registration("Sofia", "Docente"),
        create_registration("Elon", "CEO Tesla"),
        create_registration("Richard", "Fundador GNU")
    ]
    
    while True:
        print_menu()
        option = input("Seleccione una opción: ")

        if option == "1":
            for registration in participants:
                assign_email(registration)
        elif option == "2":
            list_participants(participants)
        elif option == "3":
            print("Saliendo del sistema")
            break
        else: 
            print("Opcion válida, Intente de nuevamente")


if __name__ == "__main__":
    main()