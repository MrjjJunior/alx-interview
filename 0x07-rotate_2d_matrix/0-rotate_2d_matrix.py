#!/usr/bin/python3
''' rotating 2d matrix '''


def rotate_2d_matrix(matrix):
    ''' Rotate 90 degrees clockwise '''
    length = len(matrix)

    for i in range(length):
        for s in range(i, length):
            matrix[s][i], matrix[i][s] = matrix[i][s], matrix[s][i]

    for integer in range(length):
        matrix[integer] = matrix[integer][::-1]
