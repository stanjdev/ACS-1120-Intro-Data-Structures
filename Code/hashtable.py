#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        all_values = []
        for bucket in self.buckets:
        # TODO: Collect all values in each bucket
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        count = 0
        for bucket in self.buckets:
        # TODO: Count number of key-value entries in each bucket
            for key, value in bucket.items():
                count += 1
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        # TODO: Check if key-value entry exists in bucket
        if not self.buckets[index].is_empty():
            for pair in self.buckets[index].items():
                if pair[0] == key:
                    return True
        return False
        
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket_list = self.buckets[index].items()
        if len(bucket_list) < 1:
            raise KeyError('Key not found: {}'.format(key))
        # TODO: Check if key-value entry exists in bucket
        for pair in bucket_list:
        # TODO: If found, return value associated with given key
            if pair[0] == key:
                return pair[1]
        # TODO: Otherwise, raise error to tell user get failed
            else: 
                raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        # TODO: Check if key-value entry exists in bucket
        bucket_list = self.buckets[index].items()
        if len(bucket_list) < 1:
            self.buckets[index].append((key, value))
            return 
        for pair in bucket_list:
        # TODO: If found, update value associated with given key
            if pair[0] == key:
                print('found! now updating')
                temp = list(pair)
                temp[1] = value
                pair = tuple(temp)
        # TODO: Otherwise, insert given key-value entry into bucket
            else:
                self.buckets[index].append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        # TODO: Check if key-value entry exists in bucket
        bucket_list = self.buckets[index].items()
        if len(bucket_list) < 1:
            raise KeyError('Key not found: {}'.format(key))
        for pair in bucket_list:
        # TODO: If found, delete entry associated with given key
            if pair[0] == key:
                self.buckets[index].delete(pair)
        # TODO: Otherwise, raise error to tell user delete failed
            else:
                raise KeyError('Key not found: {}'.format(key))
        # Hint: raise KeyError('Key not found: {}'.format(key))

if __name__ == '__main__':
    ht = HashTable()
    print('hash table: {}'.format(ht))
