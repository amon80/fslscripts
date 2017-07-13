import sys

def generate_files(num_subjects, mat_output_filename, con_output_filename, grp_output_filename, ftests_output_filename):
    num_maps = num_subjects*4
    num_ev = num_subjects+3

    matrix = []
    for i in range(num_maps):
        matrix.append(list())
    for i in range(num_maps):
        for j in range(num_ev):
            matrix[i].append(0)
    for j in range(num_subjects):
        for i in range(1, num_maps+1):
            if i > 4*j and i <= 4*(j+1):
                matrix[i-1][j] = 1
    for j in range(num_subjects, num_ev):
        k = j - num_subjects
        for i in range(num_maps):
            if i % 4 == k:
                matrix[i][j] = 1

    mat_output_file = open(mat_output_filename, "w")
    for i in range(num_maps):
        for j in range(num_ev):
            mat_output_file.write(str(matrix[i][j]))
            if j != num_ev - 1:
                mat_output_file.write(" ")
        mat_output_file.write("\n")

    grp_output_file = open(grp_output_filename, "w")
    counter = 1
    for i in range(0,num_maps,4):
        grp_output_file.write(str(counter)+"\n")
        grp_output_file.write(str(counter)+"\n")
        grp_output_file.write(str(counter)+"\n")
        grp_output_file.write(str(counter)+"\n")
        counter += 1
    grp_output_file.close()

    contrast_matrix = []
    for j in range(3):
        contrast_matrix.append(list())
        for i in range(num_subjects+3):
            contrast_matrix[j].append(0)
    for i in range(num_subjects, num_subjects+3):
        for j in range(3):
            if(i-num_subjects == j):
                contrast_matrix[j][i] = 1

    con_output_file = open(con_output_filename, "w")
    for j in range(3):
        for i in range(num_subjects+3):
            con_output_file.write(str(contrast_matrix[j][i]))
            if(i == num_subjects+2):
                con_output_file.write("\n")
            else:
                con_output_file.write(" ")
    con_output_file.close()

    ftest_output_file = open(ftests_output_filename, "w")
    ftest_output_file.write("1 1 1\n")
    ftest_output_file.close()
    
if __name__ == "__main__":
    argc = len(sys.argv)
    help_message = "Usage: " + sys.argv[0] + "<num subjects>"
    if(argc < 2):
        print(help_message)
    elif(argc == 2):
        generate_files(int(sys.argv[1]), "design_matrix.txt", "contrast_matrix.txt", "groups.txt", "ftests.txt",)
