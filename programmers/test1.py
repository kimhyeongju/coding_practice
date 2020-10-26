def solution(board, moves):
    basket = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break

    n = 0
    while n < len(basket) - 1:
        if basket[n] == basket[n+1]:
            basket.pop(n)
            basket.pop(n)
            answer += 2
            n = 0
        else:
            n += 1


    return print(answer)


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

solution(board, moves)
"""
00000
00000
00500
02402
05131

4311324
"""
