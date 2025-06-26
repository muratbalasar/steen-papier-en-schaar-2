from appJar import gui

class TicTacToe:
    def __init__(self):
        self.app = gui("Tic Tac Toe", "300x350")
        self.current_player = "X"
        self.board = [""] * 9
        self.create_widgets()

    def create_widgets(self):
        self.app.addLabel("title", "Tic Tac Toe", 0, 0, 3)
        self.app.setLabelBg("title", "lightblue")
        self.app.addLabel("turn", "Turn: X", 1, 0, 3)
        for i in range(9):
            row, col = divmod(i, 3)
            self.app.addButton(f"btn{i}", self.make_move, row+2, col, 1, 1)
            self.app.setButtonFont(f"btn{i}", size=20)
            self.app.setButtonWidth(f"btn{i}", 4)
        self.app.addButton("Reset", self.reset_game, 5, 0, 3)
        self.app.setButtonBg("Reset", "orange")

    def make_move(self, btn):
        idx = int(btn[3:])
        if self.board[idx] == "" and not self.check_winner():
            self.board[idx] = self.current_player
            self.app.setButton(btn, self.current_player)
            winner = self.check_winner()
            if winner:
                self.app.setLabel("turn", f"{winner} wins!" if winner != "Draw" else "Draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.app.setLabel("turn", f"Turn: {self.current_player}")

    def check_winner(self):
        combos = [
            [0,1,2],[3,4,5],[6,7,8], # rows
            [0,3,6],[1,4,7],[2,5,8], # cols
            [0,4,8],[2,4,6]          # diags
        ]
        for c in combos:
            if self.board[c[0]] and self.board[c[0]] == self.board[c[1]] == self.board[c[2]]:
                return self.board[c[0]]
        if all(self.board):
            return "Draw"
        return None

    def reset_game(self, btn):
        self.board = [""] * 9
        self.current_player = "X"
        for i in range(9):
            self.app.setButton(f"btn{i}", "")
        self.app.setLabel("turn", "Turn: X")

    def run(self):
        self.app.go()

if __name__ == "__main__":
    TicTacToe().run()
