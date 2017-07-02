import sys

def generate_files(num_subjects, mat_output_filename, con_output_filename, grp_output_filename):
    matrix = []
    #Allocating matrix
    num_maps = num_subjects*2
    num_cols = num_subjects+1
    for i in range(num_maps):
        matrix.append(list())
    for i in range(num_maps):
        for j in range(num_cols):
            matrix[i].append(0)
    #Filling first column
    for i in range(0,num_maps, 2):
        matrix[i][0] = 1
    for i in range(1,num_maps, 2):
        matrix[i][0] = -1
    #Filling other columns
    for j in range(1, num_cols):
        n_subj = j - 1
        for i in range(0, num_maps):
            if(float(i)/2 == n_subj or float(i)/2 - 0.5 == n_subj):
                matrix[i][j] = 1
    mat_output_file = open(mat_output_filename, "w")
    for i in range(num_maps):
        row_string = ""
        for j in range(num_cols):
            row_string += str(matrix[i][j])
            if j != num_cols-1:
                row_string += " "
            else:
                row_string += "\n"
        mat_output_file.write(row_string)
    mat_output_file.close()

    grp_output_file = open(grp_output_filename, "w")
    counter = 1
    for i in range(0, num_maps, 2):
        grp_output_file.write(str(counter)+"\n")
        grp_output_file.write(str(counter)+"\n")
        counter += 1
    grp_output_file.close()

    con_output_file = open(con_output_filename, "w")
    string_con_output = "1"
    for i in range(1, num_subjects+1):
        string_con_output += " 0"
    string_con_output += "\n"
    con_output_file.write(string_con_output)
    con_output_file.close()
    
if __name__ == "__main__":
    argc = len(sys.argv)
    help_message = "Usage: " + sys.argv[0] + "<num subjects>"
    if(argc < 2):
        print(help_message)
    elif(argc == 2):
        generate_files(int(sys.argv[1]), "design_matrix.txt", "contrast_matrix.txt", "groups.txt")
