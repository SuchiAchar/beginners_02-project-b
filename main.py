def on_button_pressed_a():
    basic.show_leds("""
        . # # . .
                . . # . .
                . # # # .
                . # # # .
                . # # # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_number(3)
basic.show_number(2)
basic.show_number(1)

def on_forever():
    basic.show_leds("""
        . . . . .
                . . # . .
                . # # # .
                . # # # .
                . # # # .
    """)
basic.forever(on_forever)
