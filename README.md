# Virtual Pet

Very basic, very needy virtual pet for the [BBC Micro:bit v2](https://microbit.org/new-microbit/).

## Prerequisites

- [BBC Micro:bit v2](https://microbit.org/buy/) (it may work on a v1, but I haven't tested it)
- [Supported code editor](https://microbit.org/code/)

## Installation

1. Clone the repo:

   ```sh
   git clone https://github.com/samcottle/virtual-pet.git
   ```

2. [Transfer](https://microbit.org/get-started/first-steps/set-up/#transfer-from-a-computer) the file [virtualpet.hex](/virtualpet.hex) to your Micro:bit.

3. Plug your Micro:bit into a power source (either USB or battery pack) to breathe life into your virtual pet.

## Usage

Each virtual pet is born happy and healthy, and in need of constant attention.

The attention your virtual pet craves is:

- Tapping on the [touch logo](https://www.microbit.org/get-started/user-guide/features-in-depth/#touch-logo) (`TouchButtonEvent.Pressed`).
- Pressing on the [A or B buttons](https://www.microbit.org/get-started/user-guide/features-in-depth/#buttons) (`Button.A` or `Button.B`).
- Getting a [shake](https://www.microbit.org/get-started/user-guide/features-in-depth/#accelerometer) (`Gesture.Shake`).

Attention keeps your pet healthy. Without it, your pet loses `health`.

As your pet's health decreases it becomes `Confused`, then `Sad`. Neglect it for too long and it will ascend to virtual pet heaven. Funeral music will play (`Melodies.Funeral`), and a reminder of your neglect will forever be immortalized on the display (`IconNames.Skull`).

Fortunately, you can use the [Reset button](https://www.microbit.org/get-started/user-guide/features-in-depth/#buttons) on the back of the Micro:bit to resuscitate your pet.
