
# Write team member names here: 


'''
Base class file for building a Direct mapped Cache.
Credit: R. Martin (W&M), A. Jog (W&M), Ramulator (CMU)
'''

import numpy as np
from math import log
import random


class Cache:
    '''
    keep ways = 1 to build a direct mapped cache.
    '''
    def __init__(self, cSize, ways=1, bSize=4):

        if(ways != 1):
            print("Ways not equal to 1. Not a Direct mapped cache")
            exit(0)
        
        self.cacheSize = cSize  # Bytes
        self.ways = ways        # Default: 1 way (i.e., directly mapped)
        self.blockSize = bSize  # Default: 4 bytes (i.e., 1 word block)
        self.sets = cSize // bSize // ways

        self.blockBits = 0
        self.setBits = 0

        if (self.blockSize != 1):
            self.blockBits = int(log(self.blockSize, 2))

        if (self.sets != 1):
            self.setBits = int(log(self.sets, 2))

        self.cache = np.zeros((self.sets, self.ways, self.blockSize), dtype=int)
        self.cache = self.cache - 1

        self.metaCache = np.zeros((self.sets, self.ways), dtype=int)
        self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0
        self.hitlatency = 1 # cycle
        self.misspenalty = 10 # cycle

    def reset(self):
        self.cache = np.zeros((self.sets, self.ways, self.blockSize), dtype=int)
        self.cache = self.cache - 1

        self.metaCache = np.zeros((self.sets, self.ways), dtype=int)
        self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0
        
    '''
    Warning: DO NOT EDIT ANYTHING ABOVE THIS LINE
    '''


    '''
    Returns the set number of an address based on the policy discussed in the class
    Do NOT change the function definition and arguments
    '''

    def find_set(self, address):
        # Mask and shift address to get the set index
        return (address >> self.blockBits) & (self.sets - 1)

    '''
    Returns the tag of an address based on the policy discussed in the class
    Do NOT change the function definition and arguments
    '''
    
    def find_tag(self, address):
        # Get the tag from the address by shifting right to remove set and block bits
        return address >> (self.blockBits + self.setBits)

    '''
    Search through cache for address
    return True if found
    otherwise False
    Do NOT change the function definition and arguments
    '''

    def find(self, address):
        set_index = self.find_set(address)
        tag = self.find_tag(address)

        # Check if the tag matches in the cache's metadata for the given set index
        if self.metaCache[set_index][0] == tag:
            self.hit += 1
            return True
        else:
            self.miss += 1
            return False
    
    '''
    Load data into the cache. 
    Something might need to be evicted from the cache and send back to memory
    Do NOT change the function definition and arguments
    '''
   
    def load(self, address):
        set_index = self.find_set(address)
        tag = self.find_tag(address)

        # Evict the current block in the set (since this is a direct-mapped cache)
        self.metaCache[set_index][0] = tag

        # Fill the cache block with random data as a placeholder (real cache would pull from memory)
        self.cache[set_index][0] = random.randint(0, 255)

