# hashtable/hashtable.py

from linkedlist import HashTableEntry, LinkedList

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [LinkedList()] * self.capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        self.load_factor = [i.head for i in self.storage if i.head is not None]
        return len(self.load_factor) / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        input, key: string
        """
        fnv1_prime = 16777619
        hash = 2166136261
        for i in key:
            # ^ : bitwise exclusive or operator
            hash = hash ^ ord(i)
            hash = hash * fnv1_prime

        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        input, key: string
        """
        hash = 5381
        for i in key:
            # << : bitwise shift left operator
            #      shifts hash left 5 spaces.
            hash = ((hash << 5) + hash) + ord(i)

        # 32-bit 8 Fs
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index].find(key) is not None:
            self.storage[index].insert_or_overwrite_value(key, value)

        else:
            self.storage[index].insert_at_head(HashTableEntry(key, value))


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        
        if self.storage[index].find(key) is not None:
            return self.storage[index].delete(key)

        else:
            raise Exception("No entry found with that key.")


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index].find(key) is not None:
            return self.storage[index].find(key).value

        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        old_storage = self.storage
        self.storage = [LinkedList()] * new_capacity
        for ll in old_storage:
            if ll.head is not None:
                cur = ll.head
                while cur is not None:
                    self.put(cur.key, cur.value)
                    cur = cur.next

        self.capacity = new_capacity




if __name__ == "__main__":
    # ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("storage")
    # print(ht.storage)

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")

    ht = HashTable(0x10000)

    ht.put("key-0", "val-0")
    print(ht.get("key-0"))
    ht.put("key-1", "val-1")
    print(ht.get("key-1"))
    ht.put("key-2", "val-2")
    print(ht.get("key-2"))

    ht.delete("key-2")
    print(ht.get("key-2"))
    ht.delete("key-1")
    ht.delete("key-0")