import os

def main():
    name = os.getenv("NAME")
    language = os.getenv("LANGUAGE")

    print(f"Hola {name}, veo que tu lenguaje favorito es {language}")


if __name__ == "__main__":
    main()