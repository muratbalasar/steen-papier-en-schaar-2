from appJar import gui

def create_widgets(app, board, current_player):
    app.addLabel("title", "Tic Tac Toe", 0, 0, 3)
    app.setLabelBg("title", "lightblue")
    app.addLabel("turn", f"Turn: {current_player[0]}", 1, 0, 3)
    for i in range(9):
        row, col = divmod(i, 3)
        app.addButton(f"btn{i}", lambda btn: make_move(btn, app, board, current_player), row+2, col, 1, 1)
        app.setButtonFont(f"btn{i}", size=20)
        app.setButtonWidth(f"btn{i}", 4)
    app.addButton("Reset", lambda btn: reset_game(app, board, current_player), 5, 0, 3)
    app.setButtonBg("Reset", "orange")

def make_move(btn, app, board, current_player):
    idx = int(btn[3:])
    if board[idx] == "" and not check_winner(board):
        board[idx] = current_player[0]
        app.setButton(btn, current_player[0])
        winner = check_winner(board)
        if winner:
            app.setLabel("turn", f"{winner} wins!" if winner != "Draw" else "Draw!")
        else:
            current_player[0] = "O" if current_player[0] == "X" else "X"
            app.setLabel("turn", f"Turn: {current_player[0]}")

def check_winner(board):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for c in combos:
        if board[c[0]] and board[c[0]] == board[c[1]] == board[c[2]]:
            return board[c[0]]
    if all(board):
        return "Draw"
    return None

def reset_game(app, board, current_player):
    for i in range(9):
        board[i] = ""
        app.setButton(f"btn{i}", "")
    current_player[0] = "X"
    app.setLabel("turn", "Turn: X")

def run():
    app = gui("Tic Tac Toe", "300x350")
    board = [""] * 9
    current_player = ["X"]
    create_widgets(app, board, current_player)
    app.go()


run()
