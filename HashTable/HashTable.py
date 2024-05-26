import csv
from collections import defaultdict

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = defaultdict(list)

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashed_key = self._hash(key)
        key_exists = False
        bucket = self.table[hashed_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))
        print(f"Inserted key: {key} with value: {value} at hash: {hashed_key}")

    def search_by_key(self, key):
        hashed_key = self._hash(key)
        bucket = self.table[hashed_key]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def search_by_value(self, value):
        for bucket in self.table.values():
            for k, v in bucket:
                if v == value:
                    return k
        return None

    def load_from_csv(self, filepath):
        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) == 2:
                    key, value = row
                    self.insert(key, value)

    def display(self):
        for i, bucket in self.table.items():
            if bucket:
                print(f"Hash {i}: {bucket}")

def main():
    hash_table = HashTable()

    while True:
        print("\nMenu:")
        print("1. Insertar manualmente")
        print("2. Buscar por clave")
        print("3. Buscar por valor")
        print("4. Cargar desde CSV")
        print("5. Mostrar tabla")
        print("6. Salir")

        choice = input("Elija una opción: ")

        if choice == '1':
            key = input("Ingrese la clave: ")
            value = input("Ingrese el valor: ")
            hash_table.insert(key, value)
        elif choice == '2':
            key = input("Ingrese la clave para buscar: ")
            result = hash_table.search_by_key(key)
            if result:
                print(f"Valor encontrado: {result}")
            else:
                print("Clave no encontrada.")
        elif choice == '3':
            value = input("Ingrese el valor para buscar: ")
            result = hash_table.search_by_value(value)
            if result:
                print(f"Clave encontrada: {result}")
            else:
                print("Valor no encontrado.")
        elif choice == '4':
            filepath = input("Ingrese la ruta del archivo CSV: ")
            hash_table.load_from_csv(filepath)
        elif choice == '5':
            hash_table.display()
        elif choice == '6':
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()