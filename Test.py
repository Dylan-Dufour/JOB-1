def dessiner_rectangle(width, height):
    if width < 1 or height < 1:
        print("La largeur et la hauteur doivent être des entiers positifs.")
        return

    # Dessiner le haut du rectangle
    print(' ' + '-' * (width - 2) + ' ')

    # Dessiner les côtés du rectangle
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    # Dessiner le bas du rectangle, si la hauteur est supérieure à 1
    if height > 1:
        print(' ' + '-' * (width - 2) + ' ')

# Exemple d'utilisation
width = int(input("Entrez la largeur du rectangle : "))
height = int(input("Entrez la hauteur du rectangle : "))
dessiner_rectangle(width, height)
