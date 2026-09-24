def chiffrer_cesar(texte: str, decalage: int) -> str:
    resultat = ""

    for lettre in texte:
        if lettre.islower():
            position = ord(lettre) - ord('a')
            position_decalee = position + decalage
            position_finale = position_decalee % 26
            nouvelle_lettre = chr(position_finale + ord('a'))
            resultat += nouvelle_lettre
        elif lettre.isupper():
            position = ord(lettre) - ord('A')
            position_decalee = position + decalage
            position_finale = position_decalee % 26
            nouvelle_lettre = chr(position_finale + ord('A'))
            resultat += nouvelle_lettre
        else:
            resultat += lettre

    return resultat

def dechiffrer_cesar(texte: str, decalage: int) -> str:
    return chiffrer_cesar(texte, -decalage)

def bruteforce_cesar(texte_chiffre: str) -> None:
    for decalage_test in range(1,26):
        resultat = dechiffrer_cesar(texte_chiffre, decalage_test)
        print(f"Decalage {decalage_test}: {resultat}")
    return resultat

def chiffrer_xor(texte: str, cle: str) -> bytes:
    # TODO: implémenter
    pass

def dechiffrer_xor(donnees: bytes, cle: str) -> str:
    # TODO: implémenter
    pass

def afficher_menu() -> None:
    print("\n=== Outil de chiffrement ===")
    print("1. Chiffrer avec César")
    print("2. Déchiffrer avec César")
    print("3. Attaque par force brute (César)")
    print("4. Chiffrer avec XOR")
    print("5. Déchiffrer avec XOR")
    print("6. Quitter")

def main() -> None:

    while True:
        afficher_menu()
        choix = int(input())
        if choix == 1:
            msg =  input("Quel message vous voulez chiffrer?: ")
            decalage = int(input("De combien veux tu faire le decalage: "))
            print(chiffrer_cesar(msg, decalage))
        if choix == 2:
            msg = input("Quel message vous voulez dechiffrer?: ")
            decalage = int(input("De combien veux tu faire le decalage: "))
            print(dechiffrer_cesar(msg, decalage))
        if choix == 3:
            msg = input("Quel message vous voulez trouver?: ")
            bruteforce_cesar(msg)
        if choix == 4:
            pass
        if choix == 5:
            pass
        if choix == 6:
            return

if __name__ == "__main__":
    main()