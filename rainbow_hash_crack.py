import hashlib

print("         ____       _       _                     _   _           _     ")
print("        |  _ \ __ _(_)_ __ | |__   _____      __ | | | | __ _ ___| |__  ")
print(" _____  | |_) / _` | | '_ \| '_ \ / _ \ \ /\ / / | |_| |/ _` / __| '_ \ ")
print("|_____| |  _ < (_| | | | | | |_) | (_) \ V  V /  |  _  | (_| \__ \ | | |")
print("  ____  |_| \_\__,_|_|_| |_|_.__/ \___/ \_/\_/   |_| |_|\__,_|___/_| |_|")
print(" / ___|_ __ __ _  ___| | __                                             ")
print("| |   | '__/ _` |/ __| |/ /  _____                                      ")
print("| |___| | | (_| | (__|   <  |_____|                                     ")
print(" \____|_|  \__,_|\___|_|\_\                                             ")

hash = input("Introduce el hash a buscar en el diccionario: ").strip()
dict_path = input("Introduce la ruta del archivo del diccionario de contrasenyas: ").strip()
f = open(dict_path, "r", encoding='latin-1')
try:
    for line in f:
        password = line.strip()
        hash_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
        if hash == hash_md5:
            print("El hash " + hash + " pertenece al password " + password)
            break
except FileNotFoundError:
    print("No se pudo abrir el archivo. Verifica la ruta.")
