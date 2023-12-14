import os

def main():
    username = os.getenv("USERNAME")
    print(f"¡Hola, {username} Bienvenido")


if __name__ == "__main__":
    main()