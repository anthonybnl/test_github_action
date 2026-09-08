def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def main():
    import argparse

    parser = argparse.ArgumentParser("mon_module")
    parser.add_argument("a", help="le nombre 'a', pour l'addition", type=int)
    parser.add_argument("b", help="le nombre 'b', pour l'addition", type=int)
    args = parser.parse_args()
    a = args.a
    b = args.b

    result = addition(a, b)

    print(f"l'addition de {a} et {b} donne :")
    print(result)


if __name__ == "__main__":
    main()
