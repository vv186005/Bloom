import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, string):
        for seed in range(self.hash_count):
            index = mmh3.hash(string, seed) % self.size
            self.bit_array[index] = 1

    def contains(self, string):
        for seed in range(self.hash_count):
            index = mmh3.hash(string, seed) % self.size
            if not self.bit_array[index]:
                return False
        return True

# Calculate the optimal size and hash functions for 1 million strings input
num_strings = 1000000
false_positive_rate = 0.01
size = int((num_strings * (1 / false_positive_rate) * 0.6931) / 8)  # Optimal size formula
hash_count = int((size / num_strings) * 0.6931)  # Optimal number of hash functions

# Create the Bloom Filter with the calculated size and hash functions
bloom_filter = BloomFilter(size, hash_count)

# Train the Bloom Filter with the strings
for i in range(num_strings):
    bloom_filter.add(str(i))

# Check if a string exists in the Bloom Filter
print(bloom_filter.contains("12345"))  # Example check
