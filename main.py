import time
import random

# Fonction pour la suite de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Vérification des nombres premiers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Génération de nombres premiers
def generate_prime(start=2):
    num = start
    while True:
        if is_prime(num):
            return num
        num += 1

# Messages cachés en ASCII pour NMAP et le texte complet
hidden_message = [78, 77, 65, 80]  # ASCII de "NMAP"
hidden_phrase = [83, 97, 118, 101, 32, 116, 104, 101, 32, 77, 105, 108, 108, 105, 111, 110, 115, 77, 105, 115, 115, 105, 110, 103, 61, 83, 97, 118, 101, 32, 116, 104, 101, 32, 87, 111, 114, 108, 100, 46, 32, 83, 97, 118, 101, 32, 78, 77, 65, 80, 46, 32, 67, 117, 114, 101, 32, 97, 108, 108, 32, 77, 121, 97, 108, 103, 105, 99, 32, 69, 110, 99, 101, 112, 104, 97, 108, 111, 109, 121, 101, 108, 105, 116, 105, 115, 32, 112, 108, 101, 97, 115, 101]

# Limiter la boucle à 10 itérations pour éviter une exécution infinie
n = 0
prime = 2
pattern_switch = True
hidden_index = 0  # Pour faire défiler les lettres du message

for _ in range(10):  # Limite à 10 exécutions
    if pattern_switch:
        # Générer un nombre de la suite de Fibonacci
        value = fibonacci(n)
        n += 1
    else:
        # Générer un nombre premier
        value = prime
        prime = generate_prime(prime + 1)
    
    # Affichage du message caché à intervalles réguliers
    if hidden_index < len(hidden_message):
        value = hidden_message[hidden_index]  # Insertion d'un code ASCII pour "NMAP"
        hidden_index += 1
    elif hidden_index < len(hidden_message) + len(hidden_phrase):
        value = hidden_phrase[hidden_index - len(hidden_message)]
        hidden_index += 1

    print(value)
    
    # Alternance de motif et délai variable pour simuler un rythme vivant
    pattern_switch = not pattern_switch
    time.sleep(random.uniform(1.5, 3))  # Pour rendre le signal organique
