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
#
# ]
sudoku_answer = [
    [8, 3, 9, 6, 7, 5, 1, 2, 4],
    [5, 1, 2, 9, 8, 4, 7, 3, 6],
    [4, 7, 6, 1, 3, 2, 8, 5, 9],
    [6, 9, 4, 3, 1, 7, 5, 8, 2],
    [1, 8, 5, 2, 9, 6, 3, 4, 7],
    [3, 2, 7, 5, 4, 8, 6, 9, 1],
    [9, 5, 8, 7, 2, 1, 4, 6, 3],
    [2, 6, 1, 4, 5, 3, 9, 7, 8],
    [7, 4, 3, 8, 6, 9, 2, 1, 5]
]
sudoku = [
    [0, 3, 0, 6, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 7, 6, 0, 3, 0, 0, 5, 9],
    [0, 0, 0, 3, 0, 0, 5, 0, 0],
    [1, 8, 0, 0, 0, 0, 0, 4, 7],
    [0, 0, 7, 0, 0, 8, 0, 0, 0],
    [9, 5, 0, 0, 2, 0, 4, 6, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 9, 0, 1, 0]

]
# sudoku = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     # [0, 5, 2, 3, 4],
# ]

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


#
#
# def parse_sudoku_row(sudoku_copy, row=0, index=0, num_to_insert=1):
#     # if the row that was passed is equal to the length of the sudoku board, end the function
#     if row == len(sudoku_copy):
#         return True
#     if num_to_insert > len(sudoku_copy[row]):
#         return False
#     # if the index is equal to the length of the row, the end of the row has been reached...
#     '''This causes issues when trying to check a row and change its contents'''
#     if index >= len(sudoku_copy[row]):
#         # Check each row for duplicates at the same index position
#         # row_checker(sudoku_copy, row + 1)
#         # Move to the next row
#         parse_sudoku_row(sudoku_copy, row + 1)
#         return
#     if sudoku_copy[row][index] != 0:
#         # if the element is not equal to zero, go to the next element
#         parse_sudoku_row(sudoku_copy, row, index + 1)
#         return
#     if num_to_insert in sudoku_copy[row]:  # and sudoku_copy[row][index] == 0:
#         # if the number to insert is already in the row, increase the number to insert by 1 and check again
#         return parse_sudoku_row(sudoku_copy, row, index, num_to_insert + 1)
#     else:
#         # if the number is not in the row, add the number to the row at the index
#         sudoku_copy[row][index] = num_to_insert
#         # check the next number
#         parse_sudoku_row(sudoku_copy, row, index + 1)
#
#     if row + 1 == len(sudoku_copy):
#         row_checker(sudoku_copy, row)
#
#
# def row_checker(sudoku_copy, stop_at_row):
#     # If only one row was passed, return as there is nothing to check
#     # In the range of 1 to the number of rows passed, iterate through the rows
#     for row in range(0, stop_at_row):
#         check_all_rows_against_one(sudoku_copy, row, stop_at_row)
#
#     # return if all are matching
#     return
#
#
# def check_all_rows_against_one(sudoku_copy, main_row, stop_at_row):
#     # need function to check row 1 to row 2, then check against row 3 until the end
#     # Then once all rows have been checked against 1, check every row (besides 1) to row 2
#     # Then check row 3 to all rows besides 1 & 2
#     # If there is an element mismatch, correct it, and re-check each row starting back at 1...
#
#     # go through each element in each row and compare them to each other
#     for second_row in range(main_row + 1, stop_at_row + 1):
#         for index in range(0, len(sudoku_copy[main_row])):
#             # if the element is same at the same index or the element is 0...
#             if sudoku_copy[main_row][index] == sudoku_copy[second_row][index] or sudoku_copy[second_row][index] == 0:
#                 bad_num = sudoku_copy[second_row][index]
#                 # set the bad element to 0
#                 sudoku_copy[second_row][index] = 0
#                 if bad_num >= 0:
#                     # run the parse function again, increase the number to check by 1
#                     # if the while expression returns false, continue to run the loop until true
#                     while sudoku_row_algo(sudoku_copy[second_row], bad_num, index) == False:
#                         # if the bad element is at the end of the list, reset the index to the beginning of the list
#                         if index == len(sudoku_copy[second_row]) - 1:
#                             sudoku_copy[second_row][0] = 0
#                             bad_num = 0
#                         else:
#                             # if not at the end of the list then set the next number to 0 and increase bad_num
#                             sudoku_copy[second_row][index + 1] = 0
#                 if 0 in sudoku_copy[second_row]:
#                     sudoku_row_algo(sudoku_copy[second_row], 0, sudoku_copy[second_row].index(0), 0)
#
#
# # Use this function to rerun the row and get the correct number, this should help avoid any issues with list getting
# # filled when they should not and infinite recursion
# def sudoku_row_algo(row_to_change, num_to_check, index, pass_thru=1):
#     num_to_check += 1
#
#     if pass_thru == len(row_to_change):
#         return False
#
#     if num_to_check >= len(row_to_change) + 1:
#         num_to_check = 1
#
#     if num_to_check in row_to_change:
#         return sudoku_row_algo(row_to_change, num_to_check, index, pass_thru + 1)
#
#     else:
#         row_to_change[index] = num_to_check
#         return True
#
#
# def sudoku_algo_fill(_sudoku, row, index=0, num_to_insert=1, base_case=len(sudoku[0]) + 1, nums_tried=[]):
#     if index == len(_sudoku[0]):
#         sudoku_algo_fill(_sudoku, row + 1)
#         return
#     if row == len(_sudoku):
#         return
#     if num_to_insert == base_case:
#         check_rows_above(_sudoku, row, index, num_to_insert, base_case, nums_tried)
#         return
#     if num_to_insert in nums_tried:
#         sudoku_algo_fill(_sudoku, row, index, num_to_insert + 1 if num_to_insert != 5 else 1, base_case, nums_tried)
#         return
#
#     if _sudoku[row][index] == 0 and num_to_insert not in _sudoku[row]:
#         _sudoku[row][index] = num_to_insert
#         if row > 0 and check_rows_above(_sudoku, row, index, num_to_insert, base_case, nums_tried):
#             _sudoku[row][index] = 0
#             sudoku_algo_fill(_sudoku, row, index, 1 if num_to_insert + 1 == len(_sudoku[0]) + 1 else num_to_insert + 1,
#                              num_to_insert, nums_tried)
#             return
#         else:
#             # nums_tried = []
#             sudoku_algo_fill(_sudoku, row, index + 1, base_case=len(sudoku[0]) + 1, nums_tried=[])
#         return
#     elif _sudoku[row][index] == 0:
#         sudoku_algo_fill(_sudoku, row, index, num_to_insert + 1, base_case, nums_tried)
#         return
#     else:
#         sudoku_algo_fill(_sudoku, row, index + 1)
#         return
#
#
# def check_rows_above(_sudoku, row, index, num_to_insert, orig_base_case, nums_tried=[]):
#     # check all available rows to the row above it
#     current_row_to_check = _sudoku[row]
#     while row > 0:
#         # if the number to be inserted is >= the highest number allowed, reset the curr and prev index to 0
#         if num_to_insert >= len(_sudoku[row]) + 1 or current_row_to_check[index] == 0:
#             prev_index = _sudoku[row][index - 1]
#             _sudoku[row][index - 1] = current_row_to_check[index] = 0
#             num_to_insert = -1;
#             while True:
#                 if current_row_to_check[index] == 0:
#                     try:
#                         nums_tried.append(prev_index)
#                     except UnboundLocalError:
#                         nums_tried = [prev_index]
#                     if index - 1 > 0:
#                         sudoku_algo_fill(_sudoku, row, index - 1, prev_index + 1 if prev_index != 5 else 1, prev_index,
#                                          nums_tried)
#                     else:
#                         sudoku_algo_fill(_sudoku, row - 1, len(_sudoku[row]), prev_index + 1 if prev_index != 5 else 1,
#                                          prev_index,
#                                          nums_tried)
#                 # then try to fill the prev index first
#                 else:
#                     # nums_tried = []
#                     # if row ==3:
#                     break
#                     # print("h")
#                     sudoku_algo_fill(_sudoku, row, index - 1, prev_index + 1,
#                                      prev_index + 1 if prev_index == 5 else [prev_index])
#
#         if current_row_to_check[index] == _sudoku[row - 1][index]:
#             return True
#         row -= 1
#     return False


def check_rows_above(_sudoku, row, index, orig_ele=0):
    curr_row = _sudoku[row]
    # check all available rows to the row above it
    column_nums = []
    row_counter = 0
    while row_counter <= row - 1:
        column_nums.append(_sudoku[row_counter][index])
        row_counter += 1

    orig_num = []
    if orig_ele:
        # maybe get rid of the orig_ele in the current form
        orig_num.append(orig_ele)
        num_to_insert = orig_ele
    else:
        # set the # to check to 1 if it will increase past 5, else add one to it and keep moving
        num_to_insert = 1 if curr_row[index] + 1 == 6 else curr_row[index] + 1
    counter = 0
    # while the loop is true, it will continue to look for a number to fit into the sequence
    while True:
        # if the current number does not == 0, do not change it
        if curr_row[index] != 0:
            break
        # if every number was tried, then try changing the number before it
        if counter == 5:
            curr_row[index] = orig_num[-1]
            # find_next_num(curr_row, index, _sudoku)
            # save the number that was bad
            curr_bad_num = curr_row[index]
            # set the current number to 0
            curr_row[index] = 0
            if index > 0:
                # get the previous number before setting that index to 0
                prev_index = curr_row[index - 1]
                curr_row[index - 1] = 0
                # call this function again but going back one index
                ##Maybe call new function instead
                check_rows_above(_sudoku, row, index - 1, prev_index)
                orig_num.clear()
                orig_num.append(curr_bad_num)
            else:
                check_rows_above(_sudoku, row - 1, len(_sudoku[0]) - 1)
            print("nN")
            # counter = 0
            # break

        counter = 0

        # add the number that was tried in the above while loop to the list
        orig_num.append(curr_row[index])

        # skip over the number if it is in the list already
        while (num_to_insert in orig_num or num_to_insert in curr_row or num_to_insert in column_nums) and counter != 5:
            orig_num.append(num_to_insert)
            num_to_insert = 1 if num_to_insert + 1 == 6 else num_to_insert + 1
            counter += 1
        # if counter != 5 and num_to_insert != 0:
        if counter != 5:
            curr_row[index] = num_to_insert
            if curr_row[index] in curr_row:
                break

    print(f"_sudoku: {_sudoku}")
    print(f"orig_num: {orig_num}")


def column_numbers(_sudoku, row, index):
    column_nums = []
    row_counter = 0
    while row_counter < len(sudoku[0]):
        if row == row_counter or _sudoku[row_counter][index] == 0:
            row_counter += 1
            continue
        column_nums.append(_sudoku[row_counter][index])
        row_counter += 1
    return column_nums



def row_grid_start(row):
    try:
        if row % 3 == 2:
            return row - 2
        if row % 3 == 1:
            return row - 1
        return row
    except RecursionError:
        print(sudoku_c)

def index_grid_start(index):
    try:
        if index % 3 == 2:
            return index - 2
        if index % 3 == 1:
            return index - 1
        return index
    except RecursionError:
        print("h")



def find_grid(_sudoku, row, index):
    grid_nums = []
    row = row_grid_start(row)
    index = index_grid_start(index)

    orig_index = index
    row_counter = 0


    while row_counter < 3:
        index = orig_index
        index_counter = 0
        while index_counter < 3:
            grid_nums.append(_sudoku[row][index])
            index += 1
            index_counter += 1
        row += 1
        row_counter += 1
    return grid_nums


# def column_numbers(_sudoku, row, index):
#     row_counter = 0
#     column_nums = []
#     while row_counter <= row - 1:
#         if row == row_counter:
#             row_counter += 1
#             continue
#         column_nums.append(_sudoku[row_counter][index])
#         row_counter += 1
#
#
#     return column_nums


def element_permanent(row, index):
    if sudoku[row][index] == 0:
        return False
    return True


def try_again(_sudoku, row, index=0, add_num=0):
    curr_row = _sudoku[row]

    if index == len(_sudoku[row]):
        return True


    if element_permanent(row, index):
        return try_again(_sudoku, row, index + 1)


    three_by_three = find_grid(_sudoku, row, index)
    column_row = column_numbers(_sudoku, row, index)
    column_row.append(add_num)
    add_num = 1 if add_num + 1 > len(_sudoku[row]) else add_num + 1
    count = 0

    while True:

        #if the number that will be added to the list is not in one of these list and is  equal to 0, run this statement
        while (add_num in curr_row or add_num in column_row or add_num in three_by_three) and count < len(_sudoku[row]):
            add_num = 1 if add_num + 1 > len(_sudoku[row]) else add_num + 1
            count += 1
        if count < len(_sudoku[row]):
            curr_row[index] = add_num
            if try_again(_sudoku, row, index + 1):
                break
            else:
                curr_row[index] = 0
                add_num = 1 if add_num + 1 > len(_sudoku[row]) else add_num + 1
        else:
            if index == 0:
                # _sudoku[row-1][8] = 0
                ##Need to find a way to call the try_again function if the previous row gets completed

                x = call_prev_row(_sudoku, row - 1, row)
                if x:
                    if not 0 in curr_row:
                        return x
                    else:
                        return try_again(_sudoku, row, 0)
                # if call_prev_row(_sudoku, row - 1):
                    # print("J")
                    # try_again(_sudoku, row, 0)

            return False


    return True


def try_again_from_prev_row(_sudoku, row, index=0, add_num=0):
    if row == 9:
        return
    curr_row = _sudoku[row]

    if index == len(_sudoku[row]):
        return True


    if element_permanent(row, index):
        return try_again_from_prev_row(_sudoku, row, index + 1)

    three_by_three = find_grid(_sudoku, row, index)
    column_row = column_numbers(_sudoku, row, index)
    column_row.append(add_num)
    add_num = 1 if add_num + 1 > len(_sudoku[row]) else add_num + 1
    count = 0


    while True:

        #if the number that will be added to the list is not in one of these list and is  equal to 0, run this statement
        while (add_num in curr_row or add_num in column_row or add_num in three_by_three) and count < len(_sudoku[row]):
            add_num = 1 if add_num + 1 > len(_sudoku[row]) else add_num + 1
            count += 1
        if count < len(_sudoku[row]):
            curr_row[index] = add_num
            if try_again_from_prev_row(_sudoku, row, index + 1):
                break
            else:
                curr_row[index] = 0
                add_num = 1 if add_num + 1 > len(_sudoku[row]) else add_num + 1
        else:
            curr_row[index] = 0
            return False
            # if index == 0:
            #     return False
    return True


def copy_rows(_sudoku, orig_row):
    for row in range(0, len(_sudoku)):
        if _sudoku[row] != orig_row[row]:
            _sudoku[row] = orig_row[row]


def call_prev_row(_sudoku, row, original_row, index=8, count=0):
    row_count = 1
    x = False
    while not x:
        # make copy of the current row in case it needs to be reset
        while True:
            if element_permanent(row, index):
                index -= 1
                if index <= -1:  # means combo cannot be found
                    if call_prev_row(_sudoku, row - 1, original_row):  # check the previous row
                        # print(f"if call orig: {id(orig_row)}")
                        # print(f"if call sudoku: {id(_sudoku)}")
                        return True
            else:
                bad_num = _sudoku[row][index]
                _sudoku[row][index] = 0
                count += 1
                if count == 2:
                    break
                index -= 1

        # print(f"sud1oku: {id(_sudoku)}")
        orig_row = copy.deepcopy(_sudoku)
        # print(f"orig: {id(orig_row)}")
        # print(f"sudoku: {id(_sudoku)}")
        x = try_again_from_prev_row(_sudoku, row, index, bad_num)
        if not x:
            count -= 1
            index -= 1
        else:
            '''
            Change the original row count to +1 so that the calling row can b e checked too'''
            while row_count < original_row+1:
                if try_again_from_prev_row(_sudoku, row + row_count):
                    row_count += 1
                else:
                    # print(f"Inside Before assignment orig: {id(orig_row)}")
                    # print(f"Inside Before assignment sudoku: {id(_sudoku)}")
                    copy_rows(_sudoku, orig_row)
                    # print(f"Inside after assignment orig: {id(orig_row)}")
                    # print(f"Inside after assignment sudoku: {id(_sudoku)}")

                    count -= 1
                    index -= 1
                    x = False
                    break
    return True
    # if not x:
    #     y = call_prev_row(_sudoku, row, index-1, 1)
    #     return y


    # if not try_again_from_prev_row(_sudoku, row+1):
    #     _sudoku[row] = copy.deepcopy(sudoku[row])
    #     return call_prev_row(_sudoku, row - 1)
    #     # print("POK")
    #
    # return x

def call_prev_row_2point0(_sudoku, row, index=8, count=0):
    # use this if statement to reset rows that have been tried before
    # if reset_rows >0:
    #     _sudoku[row - reset_rows] = sudoku[row]
    #     call_prev_row(_sudoku, row - 1, 8, 0, reset_rows-1)
    #     return

    while True:
        if element_permanent(row, index):
            index -= 1
            if index == -1:
                return call_prev_row(_sudoku, row - 1)
        else:
            bad_num = _sudoku[row][index]
            _sudoku[row][index] = 0
            count += 1
            if count == 2:
                break
            index -= 1

    x = try_again(_sudoku, row, index, bad_num)
    if not x:
        y = call_prev_row(_sudoku, row, index - 1, 1)
        return y
    else:
        if not try_again_from_prev_row(_sudoku, row + 1):
            _sudoku[row] = copy.deepcopy(sudoku[row])
            return call_prev_row(_sudoku, row - 1)  # put return here
            # print("POK")

    return x



        # if add_num == 0:
        #     print()
        # if count == len(_sudoku[row]):
        #     return False
        # curr_row[index] = add_num
        # if try_again(_sudoku, row, index + 1):  # might use if statement here
        #     return True
        # else:
        #
        #     rev_index = 1
        #     while sudoku[row][index-rev_index] != 0 and index != 0:
        #         rev_index +=1
        #     bad_num = curr_row[index]
        #     curr_row[index] = 0
        #     if index == 0:
        #         if try_again(_sudoku, row, index, bad_num):
        #             return True
        #     if try_again(_sudoku, row, index - rev_index, bad_num):
        #         return True
        #     else:
        #         if index == 0:
        #             for i in range(0, len(_sudoku[row])):
        #                 _sudoku[row][i] = 0
        #             try_again(_sudoku, row, 0, len(_sudoku[row]))
        #         else:
        #             return False


# def try_again(_sudoku, row, index=0, add_num=0):
#     curr_row = _sudoku[row]
#
#     if index == len(_sudoku[row]):
#         return True
#
#     if sudoku[row][index] != 0:
#         return try_again(_sudoku, row, index+1, add_num)
#
#
#     add_num = 1 if add_num + 1 > len(_sudoku[row]) else add_num + 1
#     count = 0
#
#     column_row = column_numbers(_sudoku, row, index)
#
#     # if the number that will be added to the list is not in one of these list and is  equal to 0, run this statement
#     while (add_num in curr_row or add_num in column_row) and count < len(_sudoku[row]):  # and curr_row[index] == 0:
#         add_num = 1 if add_num + 1 > len(_sudoku[row]) else add_num + 1
#         count += 1
#
#     if add_num == 0:
#         print()
#     if count == len(_sudoku[row]):
#         return False
#     curr_row[index] = add_num
#     if try_again(_sudoku, row, index + 1):  # might use if statement here
#         return True
#     else:
#
#         rev_index = 1
#         while sudoku[row][index-rev_index] != 0 and index != 0:
#             rev_index +=1
#         bad_num = curr_row[index]
#         curr_row[index] = 0
#         if index == 0:
#             if try_again(_sudoku, row, index, bad_num):
#                 return True
#         if try_again(_sudoku, row, index - rev_index, bad_num):
#             return True
#         else:
#             if index == 0:
#                 for i in range(0, len(_sudoku[row])):
#                     _sudoku[row][i] = 0
#                 try_again(_sudoku, row, 0, len(_sudoku[row]))
#             else:
#                 return False
#     return



sudoku_c = copy.deepcopy(sudoku)

for _row in range(0, len(sudoku_c)):
    try_again(sudoku_c, _row)
    print(sudoku_c[_row])

print('\n\n')
for _row in range(0, len(sudoku_c)):
    print(sudoku_c[_row])


# for _row in range(0, len(sudoku_c)):
#     print(sudoku_c[_row] == sudoku_answer[_row])


#
# su1 = [
#     # [1, 2, 3, 4, 5],
#     # [2, 4, 1, 5, 3],
#     # [3, 5, 4, 1, 2],
#     # [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     #     # [1, 2, 3, 4, 5],
#     #     # [1, 2, 3, 4, 4],
#     #     # [1, 2, 3, 4, 1],
#     #     # [2, 1, 4, 5, 3],
#     #     # [3, 4, 5, 1, 2],
#     #     # [4, 5, 2, 3, 2],
# ]

# for row in su:
#     print(row)


# num_of_rows = len(su)
# for _row in range(0, num_of_rows):
#     for _index in range(0, len(su[_row])):
#         check_rows_above(su, _row, _index, [])
# def find_next_num(curr_row, index, _sudoku):
#     # check all available rows to the row above it
#
#     init_index = index
#     num_tried = 0 #curr_row[index]
#     curr_row[index] = curr_row[index-1] = 0
#     index -=1
#     count = 0
#     while True:
#
#         column_nums = []
#         row_counter = 0
#         while _sudoku[row_counter] != curr_row:
#             column_nums.append(_sudoku[row_counter][index])
#             row_counter += 1
#
#         while num_tried + 1 in column_nums or num_tried + 1 in curr_row:
#             num_tried += 1
#             if count == 5:
#                 count = 0
#                 index -= 1
#             count += 1
#         num_tried += 1
#         curr_row[index] = num_tried
#         if index != init_index:
#             index += 1
#         else:
#             break


# def check_rows_above(_sudoku, row, index, num_to_insert, orig_base_case, nums_tried=[]):
# def check_rows_above(_sudoku, row, index, orig_ele=0):
#     # check all available rows to the row above it
#     curr_row = _sudoku[row]
#     column_nums = []
#     row_counter = 0
#     while row_counter <= row - 1:
#         column_nums.append(_sudoku[row_counter][index])
#         row_counter += 1
#
#     orig_num = []
#     if orig_ele:
#         orig_num.append(orig_ele)
#         num_to_insert = orig_ele
#     else:
#         # set the # to check to 1 if it will increase past 5, else add one to it and keep moving
#         num_to_insert = 1 if curr_row[index] + 1 == 6 else curr_row[index] + 1
#     counter = 0
#     while curr_row[index] in column_nums or curr_row[index] == 0:
#         if counter == 5:
#             curr_bad_num = curr_row[index]
#             curr_row[index] = 0
#             if index > 0:
#                 prev_index = curr_row[index - 1]
#                 curr_row[index - 1] = 0
#                 check_rows_above(_sudoku, row, index - 1, prev_index)
#                 orig_num.clear()
#                 orig_num.append(curr_bad_num)
#             else:
#                 check_rows_above(_sudoku, row - 1, len(_sudoku[0]) - 1)
#             print("nN")
#             # counter = 0
#             # break
#
#         counter = 0
#
#         # add the number that was tried in the above while loop to the list
#         orig_num.append(curr_row[index])
#
#
#
#
#         # skip over the number if it is in the list already
#         while (num_to_insert in orig_num or num_to_insert in curr_row or num_to_insert in column_nums) and counter != 5:
#             orig_num.append(num_to_insert)
#             num_to_insert = 1 if num_to_insert + 1 == 6 else num_to_insert + 1
#             counter += 1
#         # if counter != 5 and num_to_insert != 0:
#         curr_row[index] = num_to_insert
#
#     print(f"_sudoku: {_sudoku}")
#     print(f"orig_num: {orig_num}")


def check_for_combo(curr_row, combinations):
    for combo in combinations:
        if curr_row == combo:
            return True
    return False


def row_and_column_check(num_to_insert, curr_row, orig_num, column_nums):
    if num_to_insert in orig_num or num_to_insert in curr_row or num_to_insert in column_nums:
        return True
    return False

# _sudoku, row, index=0, num_to_insert=1, base_case=6
# sudoku_algo_fill(sudoku, 0)
# sudoku_c = copy.deepcopy(sudoku)
# parse_sudoku_row(sudoku_c)
# print(sudoku)
#
# for _row in sudoku:
#     print(f'''{_row}''')

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
