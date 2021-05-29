// Define 'health' of virtualpet
let health = 10

// Define rate at which 'health' decreases
basic.forever(function () {
    if (health > 0) {
        basic.pause(10000)
        health += -1
    }
})

// Define virtualpet's reactions to 'health' level
basic.forever(function () {
    if (health > 5) {
        basic.showIcon(IconNames.Happy)
    }
    if (health <= 5 && health > 3) {
        basic.showIcon(IconNames.Confused)
    }
    if (health <= 3 && health > 0) {
        basic.showIcon(IconNames.Sad)
    }
    if (health == 0) {
        music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
        while (true) {
            basic.showIcon(IconNames.Skull)
        }
        music.setBuiltInSpeakerEnabled(false)
    }
})

// Define inputs and effect on 'health'
input.onButtonPressed(Button.A, function () {
    if (health < 10) {
        health += 1
        basic.showIcon(IconNames.Asleep)
        soundExpression.giggle.playUntilDone()
    }
})
input.onButtonPressed(Button.B, function () {
    if (health < 10) {
        health += 1
        basic.showIcon(IconNames.Asleep)
        soundExpression.giggle.playUntilDone()
    }
})
input.onGesture(Gesture.Shake, function () {
    if (health < 10) {
        health += 1
        basic.showIcon(IconNames.Surprised)
        soundExpression.giggle.playUntilDone()
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (health < 10) {
        health += 1
        basic.showIcon(IconNames.Asleep)
        music.playTone(880, music.beat(BeatFraction.Sixteenth))
    }
})
