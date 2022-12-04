# sudoku_answer = [
#     [4, 3, 5, 2, 6, 9, 7, 8, 1],
#     [6, 8, 2, 5, 7, 1, 4, 9, 3],
#     [1, 9, 7, 8, 3, 4, 5, 6, 2],
#     [8, 2, 6, 1, 9, 5, 3, 4, 7],
#     [3, 7, 4, 6, 8, 2, 9, 1, 5],
#     [9, 5, 1, 7, 4, 3, 6, 2, 8],
#     [5, 1, 9, 3, 2, 6, 8, 7, 4],
#     [2, 4, 8, 9, 5, 7, 1, 3, 6],
#     [7, 6, 3, 4, 1, 8, 2, 5, 9]
# ]
sudoku = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

"""
Needed:
Recursion/Backtracking

Recursion is calling the function from within the function itself
Backtracking is a form of recursion where the function makes a choice
"""

"""
row is the current row of sudoku that is being checked
"""


def parse_sudoku_row(row, index=0, num_to_check=1):
    # Use this to check if the number that was entered is in the row
    # If it is, call the function again with the same index and num_to_check+1
    if num_to_check == 10 or index == 9:
        return
    if row[index] != 0:
        parse_sudoku_row(row, index + 1)
        return
    if num_to_check in row and row[index] == 0:
        parse_sudoku_row(row, index, num_to_check + 1)
    else:
        row[index] = num_to_check
        parse_sudoku_row(row, index + 1)



    # if is_number not in row and row[index] == 0:
    # possible_nums = range(1, 10)
    # print(row)
    # for index, is_number in enumerate(range(1, 10)):
    #     #if the number in the range is not in the row, set that index to the number
    #     if is_number not in row and row[index] == 0:
    #         row[index] = is_number
    #     else:
    #         parse_sudoku_row(row)
    # print(row)



for row in sudoku:
    starting_row = row.copy()
    parse_sudoku_row(row)
    print(f'''BEGINNING ROW:      {starting_row}
    FINAL ROW:      {row}\n''')

    # for num in sudoku[0]:
#     print(f"the number in the sudoku row is {num}")
#     if num == 0:
#         num = 1
#     for is_number in range(1,10):
#         if num == is_number:
#             print(f"YES the number is {is_number}")
#         else:
#             print("NO!")


# def permute(list, s):
#    if list == 1:
#       return s
#    else:
#       return [
#          y + x
#          for y in permute(1, s)
#          for x in permute(list - 1, s)
#       ]
#
#
#
# print(permute(3, ["a","b","c"]))
