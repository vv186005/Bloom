import math
import mmh3
import csv

class BloomFilter:
    '''
    Python implementation of Bloom filters
    '''

    def __init__(self, capacity, error_rate):
        '''
        Initializes a Bloom filter with a given capacity and error rate
        '''
        self.capacity = capacity # maximum number of elements that can be stored
        self.error_rate = error_rate # desired maximum false positive rate
        self.num_bits = self.get_num_bits(capacity, error_rate) # number of bits needed
        self.num_hashes = self.get_num_hashes(self.num_bits, capacity) # number of hash functions needed
        self.bit_array = [0] * self.num_bits # bit array to store the elements
        
    def add(self, element):
        for i in range(self.num_hashes):
            # generates a hash value for the element and sets the corresponding bit to 1
            hash_val = mmh3.hash(element, i) % self.num_bits
            self.bit_array[hash_val] = 1
        
    def __contains__(self, element):
        for i in range(self.num_hashes):
            # generates a hash value for the element and checks if the corresponding bit is 1
            hash_val = mmh3.hash(element, i) % self.num_bits
            if self.bit_array[hash_val] == 0:
                # if any of the bits is 0, the element is definitely not present
                return False
        # if all the bits are 1, the element may or may not be present
        return True
    
    def get_num_bits(self, capacity, error_rate):
        '''
        Calculates the number of bits needed for a given capacity and error rate
        '''
        num_bits = - (capacity * math.log(error_rate)) / (math.log(2) ** 2)
        return int(num_bits)
    
    def get_num_hashes(self, num_bits, capacity):
        '''
        Calculates the number of hash functions needed for a given number of bits and capacity
        '''
        num_hashes = (num_bits / capacity) * math.log(2)
        return int(num_hashes)
    # create a new bloom filter with a capacity of 1000 items and a false positive rate of 0.1

#bloom_filter = BloomFilter(1000, 0.1)
bloom_filter = BloomFilter(2763, 0.1)

# add some items to the bloom filter
# bloom_filter.add("apple")
# bloom_filter.add("banana")
# bloom_filter.add("orange")
# bloom_filter.add("vinitha")

with open("C:/Users/vvijayk3/OneDrive - azureford/Datastage/bloom_names2.csv", mode='r') as file:
    csv_reader = csv.reader(file)

    # Skip the header row if it exists
    next(csv_reader)

    # Loop through each row and print the first column value
    for row in csv_reader:
        if row:  # Check if the row is not empty
            first_column_value = row[0] 
            #for i in range(num_strings):
            bloom_filter.add(first_column_value)

# check if an item is in the bloom filter
# print("apple" in bloom_filter) # True
# print("pear" in bloom_filter) # False
# print("vinita" in bloom_filter)
            
print(bloom_filter.contains("ABELOS"))  # Example check
