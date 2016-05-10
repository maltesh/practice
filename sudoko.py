# def done_or_not(board):
# #Finished!
# #'Try again!'
#     TRY_AGAIN='Try again!'
#     FINISHED='Finished!'
#     i=0
#     j=0
#     row_ele=[[]]*9
#     if board:
#         for row in board:
#             if  len(row) != len(list(set(row))):
#                 return TRY_AGAIN
#             row_ele[i]=[]
#
#             j=0
#             row_ele[i]=[None]*9
#             for col in row:
#                 if col>9 and col <0:
#                     return TRY_AGAIN
#                 row_ele[i][j]= col
#                 j=j+1
#             i=i+1
#
#
#
#         # Column wise uniqueness
#         test=[]
#         i=0
#         j=0
#         while i<9  :
#             while j<9:
#                 if test.count(board[j][i])==0:
#                     test.append(board[j][i])
#                 else:
#                     return TRY_AGAIN
#                 j=j+1
#             j=0
#             i=i+1
#             test=[]
#         # Validate 3 *3 boxes
#         i=0
#         j=0
#         test=[]
#         while i<9:
#             while j<9:
#                 test.extend(board[j][i:3+i])
#                 j=j+1
#                 if j%3 == 0:
#                     if len(test) != len(list(set (test))):
#                         return TRY_AGAIN
#                     else:
#                         test=[]
#
#             i=i+3
#             j=0
#         return FINISHED



def done_or_not(board):
  rows = board
  cols = [map(lambda x: x[i], board) for i in range(9)]
  # print cols
  squares = [
    board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
      for i in range(0, 9, 3)
      for j in range(0, 9, 3)]
  print squares
  for clusters in (rows, cols, squares):
    for cluster in clusters:
      if len(set(cluster)) != 9:
        return 'Try again!'
  return 'finished!'



print done_or_not([      [1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])

# print done_or_not([  [1, 3, 2,   5, 7, 9,     4, 6, 8]
#                     ,[4, 9, 8,   2, 6, 1,     3, 7, 5]
#                     ,[7, 5, 6,   3, 8, 4,     2, 1, 9]
#
#                     ,[6, 4, 3,   1, 5, 8,     7, 9, 2]
#                     ,[5, 2, 1,   7, 9, 3,     8, 4, 6]
#                     ,[9, 8, 7,   4, 2, 6,     5, 3, 1]
#
#                     ,[2, 1, 4,   9, 3, 5,     6, 8, 7]
#                     ,[3, 6, 5,   8, 1, 7,     9, 2, 4]
#                     ,[8, 7, 9,   6, 4, 2,     1, 3, 5]])
