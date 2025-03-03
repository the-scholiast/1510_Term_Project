# Future import files below
from beta import make_character, proper_name


def game():
    character = make_character(proper_name())
    print(character)


def main():
    game()


if __name__ == "__main__":
    main()