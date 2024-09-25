import time
import matplotlib.pyplot as plt

# HashTableC implementation (Separate Chaining)
class HashTableC:
    def __init__(self, initial_size=100000):
        self.size = initial_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def hash_function(self, key):
        hash_value = sum(ord(letter) for letter in key)
        return hash_value % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        chain = self.table[index]

        for i, (k, v) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return

        chain.append((key, value))
        self.count += 1

    def search(self, key):
        index = self.hash_function(key)
        chain = self.table[index]

        for k, v in chain:
            if k == key:
                return v

        return None

# HashTableDH implementation (Double Hashing)
class HashTableDH:
    def __init__(self, initial_size=100000):
        self.size = initial_size
        self.table = [None] * self.size
        self.keys = [None] * self.size
        self.count = 0

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def hash_function2(self, key):
        return 1 + (sum(ord(char) for char in key) % (self.size - 1))

    def insert(self, key, value):
        index = self.hash_function(key)
        step_size = self.hash_function2(key)

        while self.table[index] is not None and self.keys[index] != key:
            index = (index + step_size) % self.size

        if self.table[index] is None:
            self.count += 1

        self.table[index] = value
        self.keys[index] = key

    def search(self, key):
        index = self.hash_function(key)
        step_size = self.hash_function2(key)

        while self.table[index] is not None:
            if self.keys[index] == key:
                return self.table[index]
            index = (index + step_size) % self.size

        return None

# HashTableLP implementation (Linear Probing)
class HashTableLP:
    def __init__(self, initial_size=100000):
        self.size = initial_size
        self.table = [None] * self.size
        self.keys = [None] * self.size
        self.count = 0

    def hash_function(self, key):
        hash_value = sum(ord(letter) for letter in key)
        return hash_value % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        while self.table[index] is not None and self.keys[index] != key:
            index = (index + 1) % self.size

        if self.table[index] is None:
            self.count += 1

        self.table[index] = value
        self.keys[index] = key

    def search(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.keys[index] == key:
                return self.table[index]
            index = (index + 1) % self.size

        return None

def read_names_from_file(file_path):
    names = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                names.append(line.strip())
    except Exception as e:
        print(f"Error reading file: {e}")
    return names

def search_names(hash_table, names):
    search_times = []
    for name in names:
        start_time = time.time()
        hash_table.search(name)
        end_time = time.time()
        search_times.append(end_time - start_time)
    return search_times

def insert_names(hash_table, names):
    insert_times = []
    for name in names:
        start_time = time.time()
        hash_table.insert(name, 0)  # Assuming value is not important for this test
        end_time = time.time()
        insert_times.append(end_time - start_time)
    return insert_times

def calculate_load_factor(hash_table):
    return hash_table.count / hash_table.size

def main():
    names = read_names_from_file("english_words.txt")
    sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    chaining_insert_times = []
    chaining_search_times = []
    chaining_load_factors = []

    double_hashing_insert_times = []
    double_hashing_search_times = []
    double_hashing_load_factors = []

    linear_probing_insert_times = []
    linear_probing_search_times = []
    linear_probing_load_factors = []

    for size in sizes:
        names_subset = names[:size]

        hash_table_c = HashTableC()
        hash_table_dh = HashTableDH()
        hash_table_lp = HashTableLP()

        chaining_insert_times.append(sum(insert_names(hash_table_c, names_subset)))
        chaining_search_times.append(sum(search_names(hash_table_c, names_subset)))
        chaining_load_factors.append(calculate_load_factor(hash_table_c))

        double_hashing_insert_times.append(sum(insert_names(hash_table_dh, names_subset)))
        double_hashing_search_times.append(sum(search_names(hash_table_dh, names_subset)))
        double_hashing_load_factors.append(calculate_load_factor(hash_table_dh))

        linear_probing_insert_times.append(sum(insert_names(hash_table_lp, names_subset)))
        linear_probing_search_times.append(sum(search_names(hash_table_lp, names_subset)))
        linear_probing_load_factors.append(calculate_load_factor(hash_table_lp))

    # Plotting results
    plt.figure(figsize=(21, 7))

    # Insert times
    plt.subplot(1, 3, 1)
    plt.plot(chaining_load_factors, chaining_insert_times, label="Chaining Insert Times", marker='o')
    plt.plot(double_hashing_load_factors, double_hashing_insert_times, label="Double Hashing Insert Times", marker='o')
    plt.plot(linear_probing_load_factors, linear_probing_insert_times, label="Linear Probing Insert Times", marker='o')
    plt.xlabel("Load Factor")
    plt.ylabel("Insert Time (seconds)")
    plt.title("Insert Time vs. Load Factor")
    plt.legend()

    # Search times
    plt.subplot(1, 3, 2)
    plt.plot(chaining_load_factors, chaining_search_times, label="Chaining Search Times", marker='o')
    plt.plot(double_hashing_load_factors, double_hashing_search_times, label="Double Hashing Search Times", marker='o')
    plt.plot(linear_probing_load_factors, linear_probing_search_times, label="Linear Probing Search Times", marker='o')
    plt.xlabel("Load Factor")
    plt.ylabel("Search Time (seconds)")
    plt.title("Search Time vs. Load Factor")
    plt.legend()

    plt.tight_layout()
    plt.show()

main()
