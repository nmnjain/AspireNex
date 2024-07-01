import random
board = [' ' for _ in range(9)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceisFree(pos):
    return board[pos] == ' '

def print_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def is_board_full(board):
    return board.count(' ') == 0


def is_winner(x, y):
    return ((x[0] == y and x[1] == y and x[2] == y) or
            (x[3] == y and x[4] == y and x[5] == y) or
            (x[6] == y and x[7] == y and x[8] == y) or
            (x[0] == y and x[3] == y and x[6] == y) or
            (x[1] == y and x[4] == y and x[7] == y) or
            (x[2] == y and x[5] == y and x[8] == y) or
            (x[0] == y and x[4] == y and x[8] == y) or
            (x[2] == y and x[4] == y and x[6] == y))


def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'X'):
        return -10
    elif is_winner(board, 'O'):
        return 10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if spaceisFree(i):
                insertLetter('O', i)
                score = minimax(board, depth + 1, False, alpha, beta)
                insertLetter(' ', i)
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if spaceisFree(i):
                insertLetter('X', i)
                score = minimax(board, depth + 1, True, alpha, beta)
                insertLetter(' ', i)
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

# AI move 
def ai_move():
    best_score = -1000
    best_move = 0
    for i in range(9):
        if spaceisFree(i):
            insertLetter('O', i)
            score = minimax(board, 0, False, -1000, 1000)
            insertLetter(' ', i)
            if score > best_score:
                best_score = score
                best_move = i
    insertLetter('O', best_move)
    return

def human_move():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisFree(move - 1):
                    run = False
                    insertLetter('X', move - 1)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def main():
    print('Welcome to Tic-Tac-Toe!')
    print_board(board)

    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            human_move()
            print_board(board)
        else:
            print('AI wins this time!')
            break

        if not(is_winner(board, 'X')):
            ai_move()
            print_board(board)
        else:
            print('You win!')
            break

    if is_board_full(board):
        print('Tie Game!')

if __name__ == '__main__':
    main()