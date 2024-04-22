'''
Andrew Kozempel
CMPSC 413
Lab 5
Fall 2023
'''

from queue import PriorityQueue

# node class for tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # comparisons based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

# Time Complexity: O(n)
# - n is length of text
# iterate over text once
def get_frequencies(text):

    # dict to hold frequencies of characters
    freq_map = {}

    # get count of each char and store
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1

    return freq_map

# Time Complexity: O(n + k*log(k))
# - n is the length of the text
# - k is the number of unique characters in the text
# building the frequency map takes O(n)
# creating the tree involves inserting and removing each of the k characters,
# which takes O(log(k)) for each operation
def make_hufftree(text):

    # get frequencies
    freq_map = get_frequencies(text)
    
    # priority queue to hold nodes
    q = PriorityQueue()  

    # insert each character into the priority queue
    for char, freq in freq_map.items():
        q.put(Node(char, freq))

    # build the tree
    # go until one node/the root remains
    while q.qsize() > 1:  
        left = q.get()  # least frequency
        right = q.get()  # second least frequency

        # merge nodes
        merged = Node(None, left.freq + right.freq)  
        merged.left = left
        merged.right = right
        
        # put merged node back into the queue
        q.put(merged)
    
    # return root node of tree
    return q.get()

# Time Complexity: O(k)
# - k is number of unique characters in text
# traverses each node of the tree once
def get_huffcodes(root, current_code="", code_map={}):
    
    # base case
    if root is None:
        return

    # if leaf node, assign code for char
    if root.char is not None:  
        code_map[root.char] = current_code
    
    # traverse left and right subtree
    get_huffcodes(root.left, current_code + "0", code_map)
    get_huffcodes(root.right, current_code + "1", code_map)

    return code_map

# Time Complexity: O(n)
# - n is the length of the text
# iterate over the text once
def encode(text, huffman_code):

    # convert each character to huffman code
    encoded_text = []

    for char in text:
        encoded_char = huffman_code[char]
        encoded_text.append(encoded_char)

    return ''.join(encoded_text)

# Time Complexity: O(n)
# - n is the length of the encoded text
# iterates over the encoded text once
def decode(encoded_text, root):
    
    # init decoded text
    decoded_text = ""

    # start at root
    current_node = root

    # iterate over each bit in encoded text
    for bit in encoded_text:

        # go left or right based on bit
        if bit == "0":
            current_node = current_node.left
        else: 
            current_node = current_node.right

        # if leaf/char node
        if current_node.char:

            # append char to decoded text and 
            # reset back to root for next char
            decoded_text += current_node.char
            current_node = root

    return decoded_text

### EXAMPLES

# sample text
text = "ABAAABCBCCCDEFFFEE"

# get huffman tree root
root = make_hufftree(text)

# get huffman codes
huffman_codes = get_huffcodes(root)

print("\nHuffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")

# original
print("\nOriginal Text:", text)

# encode
encoded_text = encode(text, huffman_codes)
print("Encoded Text:", encoded_text)

# decode
decoded_text = decode(encoded_text, root)
print("Decoded Text:", decoded_text)