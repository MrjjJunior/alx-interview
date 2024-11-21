#!/usr/bin/python3
''' rotating 2d matrix '''


def rotate_2d_matrix(matrix):
    ''' Rotate 90 degrees clockwise '''
    length = len(matrix)

    swap1 = matrix[sec_integer][integer], matrix[integer][sec_integer]
    swap2 = matrix[integer][sec_integer], matrix[sec_integer][integer]

    for integer in range(length):
        for sec_integer in range(integer, length):
            swap1 = swap2

    for integer in range(length):
        matrix[integer] = matrix[integer][::-1]
