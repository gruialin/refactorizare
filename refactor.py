# Această funcție calculează prețul final al unui produs pe baza tipului și taxei aferente.
def calc_price(product_type, price):
    taxes = {
        "food": 0.09,
        "electronics": 0.19,
        "books": 0.05
    }

    if product_type not in taxes:
        print("Unknown product type")
        return

    tax = price * taxes[product_type]
    final = price + tax
    print("Final price:", final)
# Funcția gestionează comenzi (start, stop, restart) folosind un dicționar de acțiuni.
def handle_command(cmd):
    actions = {
        "start": lambda: print("Starting..."),
        "stop": lambda: print("Stopping..."),
        "restart": lambda: print("Restarting...")
    }

    action = actions.get(cmd, lambda: print("Unknown command"))
    action()
# Exemplu de utilizare a funcțiilor
calc_price("electronics", 1000) # Ar trebui să afișeze prețul final cu taxă                     
# Funcția filtrează numerele pare și le sortează crescător.
def filter_and_sort(numbers):
    return sorted([n for n in numbers if n % 2 == 0])
print(filter_and_sort([5, 3, 8, 6, 2, 1, 4])) # Ar trebui să afișeze [2, 4, 6, 8]
handle_command("start") # Ar trebui să afișeze "Starting..."    # Funcția verifică dacă un cuvânt este palindrom într-o manieră pythonică.
def is_palindrome(word):
    if word.lower() == word.lower()[::-1]:
        print("Este palindrom")
    else:
        print("Nu este palindrom")
is_palindrome("Radar") # Ar trebui să afișeze "Este palindrom"
is_palindrome("Hello") # Ar trebui să afișeze "Nu este palindrom"
handle_command("stop") # Ar trebui să afișeze "Stopping..." 
# Funcția elimină duplicatele dintr-o listă folosind un set.
def remove_duplicates(numbers):
    result = list(set(numbers))
    print(result)
remove_duplicates([1, 2, 2, 3, 4, 4, 5]) # Ar trebui să afișeze o listă fără duplicate
handle_command("restart") # Ar trebui să afișeze "Restarting..."        
# Funcția calculează suma cifrelor unui număr folosind sum() și list comprehensions.
def sum_of_digits(number):
    total = sum(int(digit) for digit in str(number))
    print("Suma cifrelor este:", total)
sum_of_digits(12345) # Ar trebui să afișeze 15  
calc_price("food", 200) # Ar trebui să afișeze prețul final cu taxă 
calc_price("books", 150) # Ar trebui să afișeze prețul final cu taxă 
calc_price("clothes", 300) # Ar trebui să afișeze "Unknown product type"    
