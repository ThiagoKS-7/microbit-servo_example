def on_button_pressed_a():
    servos.P0.set_angle(0)
    basic.show_leds("""
        . . # . .
                . # . . .
                # . # # #
                . # . . .
                . . # . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    servos.P0.set_angle(180)
    basic.show_leds("""
        . . # . .
                . . . # .
                # # # . #
                . . . # .
                . . # . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

servos.P0.set_range(0, 180)
servos.P0.set_angle(0)
servos.P0.set_stop_on_neutral(True)