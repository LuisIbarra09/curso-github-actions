import os

def main():
    username = os.getenv("USERNAME")
    print(f"¡Hola, {username} Bienvenido a Github Actions!")


if __name__ == "__main__":
    main()