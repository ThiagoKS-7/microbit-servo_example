input.onButtonPressed(Button.A, function on_button_pressed_a() {
    servos.P0.setAngle(0)
    basic.showLeds(`
        . . # . .
                . # . . .
                # . # # #
                . # . . .
                . . # . .
    `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    servos.P0.setAngle(180)
    basic.showLeds(`
        . . # . .
                . . . # .
                # # # . #
                . . . # .
                . . # . .
    `)
})
servos.P0.setRange(0, 180)
servos.P0.setAngle(0)
servos.P0.setStopOnNeutral(true)
