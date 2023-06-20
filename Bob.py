import os
import numpy as np

os.chdir(r"c:\Users\teent\OneDrive\Desktop\code") # Change the current working directory if needed

def read_encoded_file(filename):
    encoded_list = []
    with open(filename, 'r') as file:
        for line in file:
            element = int(line.strip())
            encoded_list.append(element)
    return encoded_list

def process_groups(encoded_list):
    error_indices = []
    matrix1 = np.array([[1, 0, 1, 0, 1, 0, 1],
                        [0, 1, 1, 0, 0, 1, 1],
                        [0, 0, 0, 1, 1, 1, 1]])
    for i in range(0, len(encoded_list), 7):
        group = encoded_list[i:i+7]
        matrix2 = np.zeros((7, 1))
        matrix2[:7, 0] = group
        result = np.matmul(matrix1, matrix2)
        result %= 2
        #print("result: ",result)
        if(result[0][0] + 2*result[1][0]+ 4*result[2][0]-1!=-1):
            error_indices.append(int(i+result[0][0] + 2*result[1][0]+ 4*result[2][0]-1))

    return error_indices

def is_not_power_of_two(n):
    return not ((n & (n - 1) == 0) and n != 0)

encoded_filename = "encoded.txt"
BobsInput = read_encoded_file(encoded_filename)

error_indices = process_groups(BobsInput)

for j in error_indices:
    BobsInput[j] = 1 - BobsInput[j]

reconciled_list = []
for i, element in enumerate(BobsInput):
    if (i%7==4 or i%7==2 or i%7==5 or i%7==6):
        reconciled_list.append(element)

reconciled_filename = "reconciled_message.txt"
with open(reconciled_filename, 'w') as file:
    for element in reconciled_list:
        file.write(str(element) + "\n")
#print(reconciled_list)
print("Reconciled Message stored in", reconciled_filename)
print("Bit Error Rate: ",len(error_indices)/len(reconciled_list))
