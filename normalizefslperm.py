import sys
import os

def normalize_perm(input_file_path, output_file_path):
    input_file = open(input_file_path, 'r')
    output_file = open(output_file_path, 'w')
    for line in input_file:
        numbers = line.split()
        for str_number in numbers:
            number = int(float(str_number))
            output_file.write(str(number)+" ")
        output_file.write("\n")
    input_file.close()
    output_file.close()
    
if __name__ == "__main__":
    argc = len(sys.argv)
    help_message = "Usage: " + sys.argv[0] + "<Fsl permutation file>"
    if(argc < 2):
        print(help_message)
    elif(argc == 2):
        normalize_perm(sys.argv[1], os.path.dirname(sys.argv[1])+"/perm_normalized.txt")
    os.remove(sys.argv[1])
    os.rename(os.path.dirname(sys.argv[1])+"/perm_normalized.txt", sys.argv[1])

