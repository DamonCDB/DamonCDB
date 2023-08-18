import hashlib

def to_md5():
    file1 = input("Introduce la ruta del archivo del diccionario de contraseñas: ")
    file2 = input("Introduce la ruta del archivo donde quieres guardar los hashes: ")
    f = open(file1, "r", encoding='latin-1')
    h = open(file2, "a")
    for line in f:
        string_to_hash = line
        hash_md5 = hashlib.md5(str(string_to_hash).encode('utf-8'))
        h.write(hash_md5.hexdigest() + "\n")

def check_md5(hash):
    file1 = input("Introduce la ruta del archivo de los hashes del diccionario: ")
    file2 = input("Introduce la ruta del archivo del diccionario de contraseñas: ")
    h = open(file1, 'r', encoding='latin-1')
    p = open(file2, 'r', encoding='latin-1')
    lineas1 = h.readlines()
    lineas2 = p.readlines()
    i = 0
    
    for line in lineas1:
        if hash in line:
            print("El hash " + hash + " pertenece al password " + lineas2[i])
        else:
            i = i + 1

# to_md5()
# check_md5('hash_a_buscar')