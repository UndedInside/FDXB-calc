# FDXB-calc
## About:
This program takes the hexadecimal data stored on FDX-B microchips and converts, and then formats, this data to make it human readable. The data is output in a similar way to how it is shown on the [Flipper Zero](https://flipperzero.one). The Flipper can be used to find this information, but my program is a way to find it without needing the device.

### But... why?
When working with RFID chips on the Flipper Zero, it tells you the information that is saved on the chips. If you extract the saved chip to another device, the file only contains the hexadecimal data and not the human readable information. I wrote this program to be able to get that information without needing the Flipper on-hand.

## Usage:
Run the program with Python 3. You will then be prompted to enter the hex data. This must be 22 bytes long. Spaces are allowed but optional, as they are stripped before calculations are done.

## To-Do:
Plenty of more work can be done on this. I would like to be able to generate hex from information, to be able to add microchips to the flipper.

## Help:
For help, create an issue or reach out to me on [Twitter](https://twitter.com/undedinside)
