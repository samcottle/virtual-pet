# Virtual Pet

Very basic, very needy virtual pet for the [BBC Micro:bit v2](https://microbit.org/new-microbit/).

## Getting Started

To breathe life into a virtual pet, follow these steps.

### Prerequisites

- [BBC Micro:bit v2](https://microbit.org/buy/) (it may work on a v1, but I haven't tested it)
- [Supported code editor](https://microbit.org/code/)

### Installation

1. Clone the repo:

   ```sh
   git clone https://github.com/samcottle/virtual-pet.git
   ```

2. [Transfer the code](https://support.microbit.org/support/solutions/articles/19000013986-how-do-i-transfer-my-code-onto-the-micro-bit-via-usb) to your Micro:bit.

3. Plug your Micro:bit into a power source (either USB or a battery pack).

## Usage

Each virtual pet is born happy and healthy, and in need of constant attention.

The attention your virtual pet craves is:

- Tapping on the [touch logo](https://www.microbit.org/get-started/user-guide/features-in-depth/#touch-logo) (`TouchButtonEvent.Pressed`).
- Pressing on the [A or B buttons](https://www.microbit.org/get-started/user-guide/features-in-depth/#buttons) (`Button.A` or `Button.B`).
- Getting a [shake](https://www.microbit.org/get-started/user-guide/features-in-depth/#accelerometer) (`Gesture.Shake`).

This attention keeps your pet healthy. Without attention, your pet loses health.

As its health decreases the pet becomes `Confused`, then `Sad`. Neglect it for too long and it will ascend to virtual pet heaven. Funeral music will play (`Melodies.Funeral`), and a reminder of your neglect will forever be immortalized on the display (`IconNames.Skull`).

Fortunately, you can use the [Reset button](https://www.microbit.org/get-started/user-guide/features-in-depth/#buttons) on the back of the Micro:bit to resuscitate your pet.
