import os
import numpy as np

os.chdir(r"c:\Users\teent\OneDrive\Desktop\code") # Change the current working directory if needed

def read_elements_from_file(filename):
    elements = []
    with open(filename, 'r') as file:
        for line in file:
            element = line.strip()  # Remove leading/trailing whitespace, if any
            elements.append(element)
            if len(elements) == 100000:
                break  # Stop reading after 100,000 elements
    return elements
def read_binary_string_from_file(filename):
    with open(filename, 'r') as file:
        binary_string = file.readline().strip()
        integer_list = [int(char) for char in binary_string]
        return integer_list
def create_matrix(element1, element2):
    # Create a 1x2 matrix from the two elements
    matrix = np.array([[int(element1), int(element2)]])
    return matrix

def multiply_matrices(matrix1, matrix2):
    # Multiply two matrices
    result = np.matmul(matrix1, matrix2)
    result %= 2  # Perform modulo 2 operation on each entry
    return result

def process_elements(elements_list):
    matrix2 = np.array([[1, 1, 0, 1],
                        [1, 0, 1, 1],
                        [1, 0, 0, 0],
                        [0, 1, 1, 1],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],])

    encoded_msg = []
    for i in range(0, len(elements_list), 4):
        element1 = elements_list[i]
        if i + 3 < len(elements_list):
            element2 = elements_list[i + 1]
            element3 = elements_list[i + 2]
            element4 = elements_list[i + 3]
            matrix1 = np.zeros((4, 1), dtype=int)  # Declare a 4x1 matrix filled with zeros

# Initialize the matrix with even numbers
            matrix1[0][0] = element1
            matrix1[1][0] = element2
            matrix1[2][0] = element3
            matrix1[3][0] = element4
            #print(matrix1)
            #print(matrix2)
            result = multiply_matrices(matrix2, matrix1)
            #print(result)
            encoded_msg.extend(result.flatten().tolist())

    return encoded_msg

filename = "input.txt"
elements_list = read_binary_string_from_file(filename)

encoded_msg = process_elements(elements_list)
print("Encoded Message:", encoded_msg)

output_filename = "encoded.txt"
with open(output_filename, 'w') as file:
    for element in encoded_msg:
        file.write(str(element))

print("Encoded message saved to", output_filename)
#directory = os.getcwd()
#print(directory)
#print("Elements", elements_list)
#print("Elements read:", len(elements_list))
#print("First 10 elements:", elements_list[:10])
