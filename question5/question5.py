OUT_FILE_NAME1 = 'output_question_5_1'
OUT_FILE_NAME2 = 'output_question_5_2'


def coloring(L, color_num):
    """
    Place the colored beads while trying to minimize penalty.
    :param L: the length of the matrix
    :param color_num: a dictionary with numbers corresponding
        to the specified colored beads
    :return: the matrix of colored beads with minimize penalty.
    """
    matrix = [['-' for _ in range(L)] for _ in range(L)]  # an empty matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            keys_list = []
            for key in color_num.keys():
                keys_list.append(key)
            for key in keys_list:
                if color_num[key] == 0:
                    del color_num[key]  # delete the color without beads
            # sort the elements according to the value
            sorted_dict = sorted(color_num.items(),
                                 key=lambda x: x[1], reverse=True)
            options = [x[0] for x in sorted_dict]
            # choose a color with minimize penalty
            color = select_color(matrix, i, j, options)
            matrix[i][j] = color  # place the bead with chosen color
            # update the number of bead
            color_num[color] = color_num.get(color) - 1
    return matrix


def select_color(matrix, x, y, options):
    """
    choose a color with minimize penalty
    :param matrix: a 2D-list with placed beads
    :param x: x coordinate of the current point
    :param y: y coordinate of the current point
    :param options: the sorted dictionary with numbers corresponding
        to the specified colored beads
    :return: the color with minimize penalty
    """
    penalty = []
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    for option in options:
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # increment the penalty if the neighbour bead has the same color
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) \
                    and option == matrix[nx][ny]:
                count += 1
        penalty.append(count)
    # find the color with minimum penalty
    min_index = 0
    for i in range(len(options)):
        if penalty[i] < penalty[min_index]:
            min_index = i
    return options[min_index]


def write_to_file(matrix, file_name):
    """
    Write the matrix to the file
    :param matrix: a 2D-list containing colored beads
    :param file_name: the name of the file
    :return: None
    """
    file = open(file_name, 'w')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            file.write(matrix[i][j] + ' ')
        file.write('\n')
    file.close()


if __name__ == "__main__":
    color_num_1 = {'R': 12, 'B': 13}
    L1 = 5
    color_num_2 = {'R': 139, 'B': 1451, 'G': 977, 'W': 1072, 'Y': 457}
    L2 = 64
    matrix1 = coloring(L1, color_num_1)
    matrix2 = coloring(L2, color_num_2)
    write_to_file(matrix1, OUT_FILE_NAME1)
    write_to_file(matrix2, OUT_FILE_NAME2)
