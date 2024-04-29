input.onButtonPressed(Button.A, function () {
    OnsGetal = steen
    WieWint()
    basic.pause(2000)
    ToonFiguur(OnsGetal)
    basic.pause(2000)
    ToonFiguur(CGetal)
})
function WieWint () {
    // basic.pause(3000)
    if (CGetal == steen && OnsGetal == papier) {
        basic.showIcon(IconNames.Happy)
    }
    if (CGetal == steen && OnsGetal == schaar) {
        basic.showIcon(IconNames.Sad)
    }
    if (CGetal == papier && OnsGetal == steen) {
        basic.showIcon(IconNames.Sad)
    }
    if (CGetal == papier && OnsGetal == schaar) {
        basic.showIcon(IconNames.Happy)
    }
    if (CGetal == schaar && OnsGetal == papier) {
        basic.showIcon(IconNames.Sad)
    }
    if (CGetal == schaar && OnsGetal == steen) {
        basic.showIcon(IconNames.Happy)
    }
}
input.onButtonPressed(Button.AB, function () {
    OnsGetal = schaar
    WieWint()
    basic.pause(2000)
    ToonFiguur(OnsGetal)
    basic.pause(2000)
    ToonFiguur(CGetal)
})
function ToonFiguur (getal: number) {
    if (getal == 1) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    }
    if (getal == 2) {
        basic.showLeds(`
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
    }
    if (getal == 3) {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
    }
}
input.onButtonPressed(Button.B, function () {
    OnsGetal = papier
    WieWint()
    basic.pause(2000)
    ToonFiguur(OnsGetal)
    basic.pause(2000)
    ToonFiguur(CGetal)
})
let OnsGetal = 0
let schaar = 0
let papier = 0
let steen = 0
let CGetal = 0
CGetal = randint(1, 3)
steen = 1
papier = 2
schaar = 3
music.play(music.stringPlayable("G B A G C5 B A B ", 259), music.PlaybackMode.UntilDone)
