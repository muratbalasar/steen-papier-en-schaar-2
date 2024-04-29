def on_button_pressed_a():
    global OnsGetal
    OnsGetal = 1
    WieWint()
    basic.show_string(winnaar)
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def WieWint():
    global winnaar
    # basic.pause(3000)
    if CGetal == steen and OnsGetal == papier:
        winnaar = "W"
    if CGetal == steen and OnsGetal == schaar:
        winnaar = "C"
    if CGetal == papier and OnsGetal == steen:
        winnaar = "C"
    if CGetal == papier and OnsGetal == schaar:
        winnaar = "W"
    if CGetal == schaar and OnsGetal == papier:
        winnaar = "C"
    if CGetal == schaar and OnsGetal == steen:
        winnaar = "W"

def on_button_pressed_ab():
    global OnsGetal
    OnsGetal = 3
    WieWint()
    basic.show_string(winnaar)
    basic.show_leds("""
        # # # . .
        # # # . .
        # # . # .
        . . # . #
        . . . # .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global OnsGetal
    OnsGetal = 2
    WieWint()
    basic.show_string(winnaar)
    basic.show_leds("""
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

OnsGetal = 0
winnaar = ""
schaar = 0
papier = 0
steen = 0
CGetal = 0
CGetal = randint(1, 3)
steen = 1
papier = 2
schaar = 3
winnaar = "C"
music.play(music.string_playable("G B A G C5 B A B ", 259),
    music.PlaybackMode.UNTIL_DONE)