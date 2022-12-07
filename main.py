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
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    # [0, 5, 2, 3, 4],
]

# sudoku =[
#     [0, 3, 5, 2, 0, 9, 7, 8, 1],
#     [6, 8, 2, 5, 0, 1, 4, 9, 3],
#     [1, 9, 7, 8, 3, 4, 5, 0, 2],
# ]
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
        return True
    if num_to_insert > len(sudoku_copy[row]):
        return False
    # if the index is equal to the length of the row, the end of the row has been reached...
    '''This causes issues when trying to check a row and change its contents'''
    if index >= len(sudoku_copy[row]):
        # Check each row for duplicates at the same index position
        # row_checker(sudoku_copy, row + 1)
        # Move to the next row
        parse_sudoku_row(sudoku_copy, row + 1)
        return
    if sudoku_copy[row][index] != 0:
        # if the element is not equal to zero, go to the next element
        parse_sudoku_row(sudoku_copy, row, index + 1)
        return
    if num_to_insert in sudoku_copy[row]:  # and sudoku_copy[row][index] == 0:
        # if the number to insert is already in the row, increase the number to insert by 1 and check again
        return parse_sudoku_row(sudoku_copy, row, index, num_to_insert + 1)
    else:
        # if the number is not in the row, add the number to the row at the index
        sudoku_copy[row][index] = num_to_insert
        # check the next number
        parse_sudoku_row(sudoku_copy, row, index + 1)

    if row + 1 == len(sudoku_copy):
        row_checker(sudoku_copy, row)


def row_checker(sudoku_copy, stop_at_row):
    # If only one row was passed, return as there is nothing to check
    # In the range of 1 to the number of rows passed, iterate through the rows
    for row in range(0, stop_at_row):
        check_all_rows_against_one(sudoku_copy, row, stop_at_row)

    # return if all are matching
    return


def check_all_rows_against_one(sudoku_copy, main_row, stop_at_row):
    # need function to check row 1 to row 2, then check against row 3 until the end
    # Then once all rows have been checked against 1, check every row (besides 1) to row 2
    # Then check row 3 to all rows besides 1 & 2
    # If there is an element mismatch, correct it, and re-check each row starting back at 1...

    # go through each element in each row and compare them to each other
    for second_row in range(main_row + 1, stop_at_row + 1):
        for index in range(0, len(sudoku_copy[main_row])):
            # if the element is same at the same index or the element is 0...
            if sudoku_copy[main_row][index] == sudoku_copy[second_row][index] or sudoku_copy[second_row][index] == 0:
                bad_num = sudoku_copy[second_row][index]
                # set the bad element to 0
                sudoku_copy[second_row][index] = 0
                if bad_num >= 0:
                    # run the parse function again, increase the number to check by 1
                    # if the while expression returns false, continue to run the loop until true
                    while sudoku_row_algo(sudoku_copy[second_row], bad_num, index) == False:
                        # if the bad element is at the end of the list, reset the index to the beginning of the list
                        if index == len(sudoku_copy[second_row]) - 1:
                            sudoku_copy[second_row][0] = 0
                            bad_num = 0
                        else:
                            # if not at the end of the list then set the next number to 0 and increase bad_num
                            sudoku_copy[second_row][index + 1] = 0
                if 0 in sudoku_copy[second_row]:
                    sudoku_row_algo(sudoku_copy[second_row], 0, sudoku_copy[second_row].index(0), 0)


# Use this function to rerun the row and get the correct number, this should help avoid any issues with list getting
# filled when they should not and infinite recursion
def sudoku_row_algo(row_to_change, num_to_check, index, pass_thru=1):
    num_to_check += 1

    if pass_thru == len(row_to_change):
        return False

    if num_to_check >= len(row_to_change) + 1:
        num_to_check = 1

    if num_to_check in row_to_change:
        return sudoku_row_algo(row_to_change, num_to_check, index, pass_thru + 1)

    else:
        row_to_change[index] = num_to_check
        return True


def sudoku_algo_fill(_sudoku, row, index=0, num_to_insert=1, base_case=[6]):

    if index == 5:
        sudoku_algo_fill(_sudoku, row + 1)
        return

    if row == len(_sudoku):
        return
    if num_to_insert == sorted(base_case)[0]:
        check_rows_above(_sudoku, row, index, num_to_insert, base_case)


    if _sudoku[row][index] == 0 and num_to_insert not in _sudoku[row]:
        _sudoku[row][index] = num_to_insert
        if row > 0 and check_rows_above(_sudoku, row, index, num_to_insert, base_case):
            _sudoku[row][index] = 0
            sudoku_algo_fill(_sudoku, row, index, 1 if num_to_insert + 1 == 6 else num_to_insert + 1, [num_to_insert])
            return
        else:
            sudoku_algo_fill(_sudoku, row, index + 1)
        return
    elif _sudoku[row][index] == 0:
        sudoku_algo_fill(_sudoku, row, index, num_to_insert + 1, base_case)
        return
    else:
        sudoku_algo_fill(_sudoku, row, index + 1)
        return


def check_rows_above(_sudoku, row, index, num_to_insert, orig_base_case):
    # check all available rows to the row above it
    current_row_to_check = _sudoku[row]
    while row > 0:
        # if the number to be inserted is >= the highest number allowed, reset the curr and prev index to 0
        if num_to_insert >= len(_sudoku[row]) + 1 or current_row_to_check[index] == 0:
            prev_index = _sudoku[row][index - 1]
            _sudoku[row][index - 1] = current_row_to_check[index] = 0
            while True:
                if current_row_to_check[index] == 0:
                    orig_base_case.append(prev_index)
                    sudoku_algo_fill(_sudoku, row, index - 1, prev_index + 1, orig_base_case)
                # then try to fill the prev index first
                else:
                    sudoku_algo_fill(_sudoku, row, index - 1, prev_index + 1, [prev_index - 1] if prev_index == 5 else [prev_index])
                if prev_index != current_row_to_check[index]:
                    break

        if current_row_to_check[index] == _sudoku[row - 1][index]:
            return True
        row -= 1
    return False


# _sudoku, row, index=0, num_to_insert=1, base_case=6
sudoku_algo_fill(sudoku, 0)
# sudoku_c = copy.deepcopy(sudoku)
# parse_sudoku_row(sudoku_c)
# print(sudoku)

for _row in sudoku:
    print(f'''{_row}''')

# if num_to_insert > len(sudoku_copy[row]):
#     return False
# # if the index is equal to the length of the row, the end of the row has been reached...
# '''This causes issues when trying to check a row and change its contents'''
# if index == len(sudoku_copy[row]):
#     # Check each row for duplicates at the same index position
#     # row_checker(sudoku_copy, row + 1)
#     # Move to the next row
#     pass
#     # parse_sudoku_row(sudoku_copy, row + 1)
#     # return
# if sudoku_copy[row][index] != 0:
#     # if the element is not equal to zero, go to the next element
#     parse_sudoku_row(sudoku_copy, row, index + 1)
#     return
# if num_to_insert in sudoku_copy[row]:  # and sudoku_copy[row][index] == 0:
#     # if the number to insert is already in the row, increase the number to insert by 1 and check again
#     return parse_sudoku_row(sudoku_copy, row, index, num_to_insert + 1)
# else:
#     # if the number is not in the row, add the number to the row at the index
#     sudoku_copy[row][index] = num_to_insert
#     # check the next number
#     if index == len(sudoku_copy[row]) - 1:
#         # Check each row for duplicates at the same index position
#         if not row_checker(sudoku_copy, row + 1):
#             parse_sudoku_row(sudoku_copy, row + 1)
#     parse_sudoku_row(sudoku_copy, row, index + 1)


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
