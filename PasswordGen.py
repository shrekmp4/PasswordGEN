from password_strength import PasswordPolicy
import secrets

def check_password_strength(password):
    # Definir la política de contraseña
    policy = PasswordPolicy.from_names(
        length=8,  # Mínimo de 8 caracteres
        uppercase=1,  # Al menos 1 mayúscula
        numbers=1,  # Al menos 1 número
        special=1,  # Al menos 1 carácter especial
        nonletters=1,  # Al menos 1 carácter no alfabético
    )

    # Evaluar la contraseña según la política
    result = policy.test(password)

    return result

def generate_random_password():
    # Generar una contraseña aleatoria de 12 caracteres
    random_password = ''.join(secrets.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?") for _ in range(12))
    return random_password

if __name__ == "__main__":
    print("Bienvenido al Evaluador de Seguridad de Contraseñas")

    while True:
        password = input("Ingresa tu contraseña: ")

        # Evaluar la seguridad de la contraseña
        result = check_password_strength(password)

        if result:
            print("La contraseña es segura.")
        else:
            print("La contraseña no cumple con los criterios de seguridad:")
            for rule in policy.test(password, verbose=True):
                print(rule)

        # Preguntar si desea generar una nueva contraseña
        response = input("¿Quieres generar una nueva contraseña? (s/n): ").lower()

        if response != 's':
            break

        # Generar una nueva contraseña aleatoria
        new_password = generate_random_password()
        print(f"Contraseña generada: {new_password}")
