def calculatrice(historique):
    expression = input("Entrez l'expression mathématique : ")
    if expression.lower() == 'historique':
        if historique:
            print("Historique des calculs :")
            for i, calcul in enumerate(historique, 1):
                print(f"{i}. {calcul}")
        else:
            print("Historique vide")
        return None, historique
    
    expression = expression.replace(',', '.')

    pile_nombre = []
    pile_operateur = []
    priorite = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    i = 0
    while i < len(expression):
        if expression[i] == '(':
            pile_operateur.append(expression[i])
        elif expression[i] == ')':
            while pile_operateur and pile_operateur[-1] != '(':
                operator = pile_operateur.pop()
                b = pile_nombre.pop()
                a = pile_nombre.pop()
                if operator == '+':
                    pile_nombre.append(a + b)
                elif operator == '-':
                    pile_nombre.append(a - b)
                elif operator == '*':
                    pile_nombre.append(a * b)
                elif operator == '/':
                    if b == 0:
                        print("Division par zéro impossible")
                        return None, historique
                    pile_nombre.append(a / b)
                elif operator == '^':
                    pile_nombre.append(a ** b)
            pile_operateur.pop()
        elif expression[i] in '+-*/^':
            while pile_operateur and pile_operateur[-1] != '(' and priorite[pile_operateur[-1]] >= priorite[expression[i]]:
                operator = pile_operateur.pop()
                b = pile_nombre.pop()
                a = pile_nombre.pop()
                if operator == '+':
                    pile_nombre.append(a + b)
                elif operator == '-':
                    pile_nombre.append(a - b)
                elif operator == '*':
                    pile_nombre.append(a * b)
                elif operator == '/':
                    if b == 0:
                        print("Division par zéro impossible")
                        return None, historique
                    pile_nombre.append(a / b)
                elif operator == '^':
                    pile_nombre.append(a ** b)
            pile_operateur.append(expression[i])
        else:
            start = i
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                i += 1
            try:
                pile_nombre.append(float(expression[start:i]))
            except ValueError:
                print("Saisie invalide")
                return None, historique
            continue
        i += 1

    while pile_operateur:
        operator = pile_operateur.pop()
        b = pile_nombre.pop()
        a = pile_nombre.pop()
        if operator == '+':
            pile_nombre.append(a + b)
        elif operator == '-':
            pile_nombre.append(a - b)
        elif operator == '*':
            pile_nombre.append(a * b)
        elif operator == '/':
            if b == 0:
                print("Division par zéro impossible")
                return None, historique
            pile_nombre.append(a / b)
        elif operator == '^':
            pile_nombre.append(a ** b)

    resultat = pile_nombre[0]
    historique.append(expression + " = " + str(resultat))
    return resultat, historique


def effacer_historique(historique):
    historique.clear()
    print("Historique effacé")


historique = []

while True:
    resultat, historique = calculatrice(historique)
    if resultat is not None:
        print("Résultat :", resultat)

    action = input("Voulez-vous regarder l'historique? (O/N) : ").upper()
    if action == 'O':
        if historique:
            print("Historique des calculs :")
            for i, calcul in enumerate(historique, 1):
                print(f"{i}. {calcul}")
    elif action == 'N':
        effacer_historique(historique)

    continuer = input("Voulez-vous continuer? (O/N) : ").upper()
    if continuer != 'O':
        break
   