from appJar import gui
from random import randint
 
# Hokje 1 t/m 9 geklikt
def btnClick(name): 
  # Bepaal de huidige waarde van de knop
  current_value = app.getButton(name)
  
  # Als de knop leeg is, zet er een X of O in
  if current_value == "  ":
    if app.getLabel("titel") == "TicTacToe - X":
      app.setButton(name, "X")
      app.setLabel("titel", "TicTacToe - O")
    else:
      app.setButton(name, "O")
      app.setLabel("titel", "TicTacToe - X")
  
    # Controleer op winst
    checkWin()
  
  # Controleer of iemand gewonnen heeft
  def checkWin():
    # Mogelijke winnende combinaties
    win_combos = [
      ["btn1", "btn2", "btn3"],
      ["btn4", "btn5", "btn6"],
      ["btn7", "btn8", "btn9"],
      ["btn1", "btn4", "btn7"],
      ["btn2", "btn5", "btn8"],
      ["btn3", "btn6", "btn9"],
      ["btn1", "btn5", "btn9"],
      ["btn3", "btn5", "btn7"]
    ]
    for combo in win_combos:
      values = [app.getButton(btn) for btn in combo]
      if values[0] != "  " and values.count(values[0]) == 3:
        app.setLabel("titel", f"{values[0]} wint!")
        # Optioneel: knoppen uitschakelen na winst
        for i in range(1, 10):
          app.disableButton(f"btn{i}")
        break
 
# Reset knop geklikt
def btnReset(name):
  # Reset het spel
  app.clearAll()
  app.setLabel("titel", "TicTacToe")
  for i in range(1, 10):
    app.setButton(i, "  ")
 
  
# De app
app = gui("TicTacToe", "300x350")
app.setFont(size=20)
 
# Titel
app.addLabel("titel", "TicTacToe", 0, 0, 3)
 
# Buttons
app.addNamedButton("  ", "btn1", btnClick, 1, 0)
app.addNamedButton("  ", "btn2", btnClick, 1, 1)
app.addNamedButton("  ", "btn3", btnClick, 1, 2)
app.addNamedButton("  ", "btn4", btnClick, 2, 0)
app.addNamedButton("  ", "btn5", btnClick, 2, 1)
app.addNamedButton("  ", "btn6", btnClick, 2, 2)
app.addNamedButton("  ", "btn7", btnClick, 3, 0)
app.addNamedButton("  ", "btn8", btnClick, 3, 1)
app.addNamedButton("  ", "btn9", btnClick, 3, 2)
 
# Reset
app.addButton("reset", btnReset, 4, 0, 3)
 
# Start!
app.go()
