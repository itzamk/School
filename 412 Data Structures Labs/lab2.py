import array

class Vector:
    def __init__(self):

        # Initialize an empty array with type 'd' (double precision floats)
        self._data = array.array('d', [])

        # Initialize the size to 0
        self._size = 0

        # Set the initial capacity to 2
        self._capacity = 2

        # Extend the array to the initial capacity with default values
        self._data.extend([0.0, 0.0])

    # Prints vector
    def __str__(self):

        # Initialize result string
        result = "["

        # Add elements to result
        for i in range(self._size):
            result += str(self._data[i])

            # If not the last element, add a comma and space
            if i != self._size - 1:  
                result += ", "

        # Finish result and return
        result += "]"
        return result

    # Return the number of items in the vector
    def length(self):
        return self._size
    
    # Check if the item is contained in the vector
    def contains(self, item):
        return item in self._data

    # Return the item at the given index
    def getitem(self, ndx):

        # If index is valid, return item
        if 0 <= ndx < self._size:
            return self._data[ndx]
        
        # Print error
        else:
            print("Index out of range")

    # Set the item at the given index
    def setitem(self, ndx, item):
        
        # If index is valid
        if 0 <= ndx < self._size:

            # Set if index is valid
            self._data[ndx] = item

        # Print error        
        else:
            print("Index out of range")
        
    # Append an item to the end of the vector
    def append(self, item):
        
        # Resize the array if the capacity is reached
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        # Add at end 
        self._data[self._size] = item

        # Increase size by 1
        self._size += 1

    # Insert an item at the given index
    def insert(self, ndx, item):
        
        # Resize the array if the capacity is reached
        if self._size == self._capacity:
            self.resize(2 * self._capacity)

        # Shift items to the right, make room
        for i in range(self._size, ndx, -1):
            self._data[i] = self._data[i - 1]

        # Insert at index
        self._data[ndx] = item

        # Increase size by 1
        self._size += 1

    # Remove and return the item at the given index
    def remove(self, ndx):
        
        # If valid index
        if 0 <= ndx < self._size:

            # Store value to be returned
            removed_item = self._data[ndx]

            # Shift items left, fill gap
            for i in range(ndx, self._size - 1):
                self._data[i] = self._data[i + 1]

            # Decrease size by 1
            self._size -= 1
            
            # Return item
            return removed_item
        
        # Print error
        else:
            print("Index out of range")

    # Return the index of the first occurrence of the item
    def indexOf(self, item):
        
        # Loop until item is found
        for i in range(self._size):

            # If found, return index
            if self._data[i] == item:
                return i
        
        # Print if not found
        print("Item not found in the vector")

    # Append the entire contents of another vector to this vector
    def extend(self, otherVector):
        
        # Loop through second vector
        for i in range(otherVector.length()):

            # Append each element to first vector
            self.append(otherVector.getitem(i))

    # Return a new vector that contains a subsequence of items
    def subVector(self, from_ndx, to_ndx):
        
        # If valid indices
        if 0 <= from_ndx <= to_ndx < self._size:

            # Create new vector (subvector)
            new_vector = Vector()

            # Loop through elements between 2 indices
            for i in range(from_ndx, to_ndx + 1):

                # Add elements to new subvector
                new_vector.append(self._data[i])

            # Return the subvector
            return new_vector
        
        # Print error
        else:
            print("Index out of range")

    # Resize the array to a new capacity
    def resize(self, new_capacity):

        # Create and initialize new array with new capacity
        new_data = array.array('d', [0.0] * new_capacity)

        # Loop through current array
        for i in range(self._size):

            # Add elements from current array to new
            new_data[i] = self._data[i]

        # Copy new data to current array
        self._data = new_data

        # Set new capacity
        self._capacity = new_capacity

# Initialize the Vector
# Expected Output: []
test = Vector()
print("\nAfter initialization:", test)  

# Testing length()
# Expected Output: 0
print("\nVector:", test)
print("Length of vector:", test.length())  

# Testing contains()
# Expected Output: False
print("\nVector:", test)
print("Contains 1.0:", test.contains(1.0))

# Testing append()
# Expected Output: [1.0]
print("\nBefore appending 1.0:", test)
test.append(1.0) 
print("After appending 1.0:", test)
print("Length of vector:", test.length())
print("Contains 1.0:", test.contains(1.0))

# Testing getitem()
# Expected Output: 1.0
print("\nVector:", test)
print("Item at index 0:", test.getitem(0))

# Testing setitem()
# Expected Output: [1.0, 2.0]
print("\nBefore setting item at index 0 to 2.0:", test)
test.setitem(0, 2.0)
print("After setting item at index 0 to 2.0:", test)

# Testing insert()
# Expected Output: [1.0, 1.5, 2.0]
print("\nBefore inserting 1.5 at index 1:", test)
test.insert(1, 1.5)
print("After inserting 1.5 at index 1:", test)

# Testing remove()
# Expected Output: 1.5
# Expected Output: [1.0, 2.0]
print("\nBefore removing item at index 1:", test)  
removed = test.remove(1)
print(f"Removed item at index 1: {removed}")
print("After removing item at index 1:", test)  

# Testing indexOf()
# # Expected Output: 1
print("\nVector:", test)
index = test.indexOf(2.0)
print(f"Index of 2.0: {index}")

# Testing extend()
# Expected Output: [1.0, 2.0, 3.0, 4.0]
test2 = Vector()
test2.append(3.0)
test2.append(4.0)
print("\nVector to be added:", test2)
print("Before extending with another vector:", test)
test.extend(test2)
print("After extending with another vector:", test)

# Testing subVector()
# Expected Output: [2.0, 3.0, 4.0]
print("\nVector:", test)
sub_test = test.subVector(1, 3)
print("Subvector from index 1 to 3:", sub_test)