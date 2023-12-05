import datetime

def salutation():
    heure = datetime.datetime.now().hour
    if 6 <= heure < 18:
        return "Bonjour"
    elif 18 <= heure < 21:
        return "Bonsoir"
    else:
        return "Bonne nuit"

def au_revoir():
    heure = datetime.datetime.now().hour
    if 6 <= heure < 20:
        return "Au revoir"
    else:
        return "Bonne nuit"

def est_palindrome(mot):
    mot = mot.lower()
    return mot == mot[::-1]

def application_console():
    print(salutation())
    
    while True:
        entree_utilisateur = input("Saisissez un mot (ou 'exit' pour quitter) : ")
        
        if entree_utilisateur.lower() == 'exit':
            break
        
        if est_palindrome(entree_utilisateur):
            print("Bien dit !")
        else:
            print("Ce n'est pas un palindrome.")

    print(au_revoir())

if __name__ == "__main__":
    application_console()
