import sys

def generate_files(num_subjects_group_1, num_subjects_group_2, mat_output_filename, con_output_filename, grp_output_filename):
    strings_mat_file_group_1 = []
    strings_mat_file_group_2 = []
    for i in range(num_subjects_group_1):
        strings_mat_file_group_1.append("1 0\n")
    for i in range(num_subjects_group_2):
        strings_mat_file_group_2.append("0 1\n")
    string_contrast = "1 -1\n"
    mat_output_file = open(mat_output_filename, "w")
    for string in strings_mat_file_group_1:
        mat_output_file.write(string)
    for string in strings_mat_file_group_2:
        mat_output_file.write(string)
    mat_output_file.close()
    con_output_file = open(con_output_filename, "w")
    con_output_file.write(string_contrast)
    con_output_file.close()
    grp_output_file = open(grp_output_filename, "w")
    num_maps = num_subjects_group_1 + num_subjects_group_2
    for i in range(0, num_maps):
        grp_output_file.write(str(1)+"\n")
    grp_output_file.close()

if __name__ == "__main__":
    argc = len(sys.argv)
    help_message = "Usage: " + sys.argv[0] + "<num subjects in group1> <num subjects in group2>"
    if(argc < 3):
        print(help_message)
    elif(argc == 3):
        generate_files(int(sys.argv[1]), int(sys.argv[2]), "design_matrix.txt", "contrast_matrix.txt", "groups.txt")
