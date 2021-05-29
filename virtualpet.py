# Define base 'health' of pet
health = 10
# Define rate at which 'health' decreases (in milliseconds)

def on_forever():
    global health
    if health > 0:
        basic.pause(10000)
        health += -1
basic.forever(on_forever)

# Define 'health' levels

def on_forever2():
    if health > 5:
        basic.show_icon(IconNames.HAPPY)
    if health <= 5 and health > 3:
        basic.show_icon(IconNames.CONFUSED)
    if health <= 3 and health > 0:
        basic.show_icon(IconNames.SAD)
    if health == 0:
        music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)
        while True:
            basic.show_icon(IconNames.SKULL)
        music.set_built_in_speaker_enabled(False)
basic.forever(on_forever2)

# Define inputs for giving 'attention' to pet

def on_button_pressed_a():
    global health
    if health < 10:
        health += 1
        basic.show_icon(IconNames.ASLEEP)
        soundExpression.giggle.play_until_done()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global health
    if health < 10:
        health += 1
        basic.show_icon(IconNames.ASLEEP)
        soundExpression.giggle.play_until_done()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global health
    if health < 10:
        health += 1
        basic.show_icon(IconNames.SURPRISED)
        soundExpression.giggle.play_until_done()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global health
    if health < 10:
        health += 1
        basic.show_icon(IconNames.ASLEEP)
        music.play_tone(880, music.beat(BeatFraction.SIXTEENTH))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
