input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . # # . .
        . . # . .
        . # # # .
        . # # # .
        . # # # .
        `)
})
basic.showNumber(3)
basic.showNumber(2)
basic.showNumber(1)
basic.forever(function () {
    basic.showLeds(`
        . . . . .
        . . # . .
        . # # # .
        . # # # .
        . # # # .
        `)
})
