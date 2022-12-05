import copy
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
# sudoku = [
#     [0, 0, 0, 2, 6, 0, 7, 0, 1],
#     [6, 8, 0, 0, 7, 0, 0, 9, 0],
#     [1, 9, 0, 0, 0, 4, 5, 0, 0],
#     [8, 2, 0, 1, 0, 0, 0, 4, 0],
#     [0, 0, 4, 6, 0, 2, 9, 0, 0],
#     [0, 5, 0, 0, 0, 3, 0, 2, 8],
#     [0, 0, 9, 3, 0, 0, 0, 7, 4],
#     [0, 4, 0, 0, 5, 0, 0, 3, 6],
#     [7, 0, 3, 0, 1, 8, 0, 0, 0]
# ]
sudoku = [
    [0, 3, 4, 5, 0],
    [0, 2, 3, 4, 5],
    [0, 5, 2, 3, 4],
]

# sudoku =[
#     [4, 3, 5, 2, 6, 9, 7, 8, 1],
#     [6, 8, 2, 5, 7, 1, 4, 9, 3],
#     [1, 9, 7, 8, 3, 4, 5, 6, 2],
# ]
"""
Needed:
Recursion/Backtracking

Recursion is calling the function from within the function itself
Backtracking is a form of recursion where the function makes a choice
"""




def parse_sudoku_row(sudoku_copy, row=0, index=0, num_to_insert=1):

    # if the row that was passed is equal to the length of the sudoku board, end the function
    if row == len(sudoku_copy):
        return
    # if the index is equal to the length of the row, the end of the row has been reached...
    print(f'index: {index}')
    if index == len(sudoku_copy[row]):
        print(f'len(sudoku_copy[row]: {len(sudoku_copy[row])}')
        # Check each row for duplicates at the same index position
        if row_checker(sudoku_copy, row + 1):
            sudoku_copy[row] = sudoku[row]
            parse_sudoku_row(sudoku_copy, row, 0, num_to_insert + 1)
        #Move to the next row
        parse_sudoku_row(sudoku_copy, row + 1)
        return
    if sudoku_copy[row][index] != 0:
        parse_sudoku_row(sudoku_copy, row, index + 1)
        return
    if num_to_insert in sudoku_copy[row] and sudoku_copy[row][index] == 0:
        parse_sudoku_row(sudoku_copy, row, index, num_to_insert + 1)
    else:
        sudoku_copy[row][index] = num_to_insert
        parse_sudoku_row(sudoku_copy, row, index + 1)


def row_checker(sudoku_copy, stop_at_row):
    # If only one row was passed, return as there is nothing to check
    if stop_at_row == 1:
        return False
    # In the range of 1 to the number of rows passed, iterate through the rows
    for row in range(1, stop_at_row):
        #go through each element in each row and compare them to each other
        for index in range(0, len(sudoku_copy[row])):
            #If any element is equal in each list, return true
            if sudoku_copy[row - 1][index] == sudoku_copy[row][index]:
                print("yes")
                print(f'''sudoku[{row - 1}]: {sudoku_copy[row - 1]} 
sudoku[{row}]: {sudoku_copy[row]}''')
                return True
            else:
                print("Nah")
    #return false is all are matching
    return False


sudoku_copy = copy.deepcopy(sudoku)
parse_sudoku_row(sudoku_copy)
# print(sudoku)

for row in sudoku_copy:
    print(f'''{row}''')
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
# for row in sudoku:
# print(row)
# for row in sudoku:
#     starting_row = row.copy()
#     parse_sudoku_row(row)
#     print(f'''BEGINNING ROW:      {starting_row}
#     FINAL ROW:      {row}\n''')

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
