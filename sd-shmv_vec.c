/*
* sd-shmv_vec.c
*
* Shutdown script BrewVectrex by MatixVision v1.0 - 2024
* www.matixvision.it
*
* GNU General Public License version 3
* https://www.gnu.org/licenses/gpl-3.0.en.html
*
* sudo apt install wiringpi
* gcc -o  sd-shmv_vec  sd-shmv_vec.c -lwiringPi
*
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <wiringPi.h>

// switchPin 6 = GPIO6 (HW PIN 31)
#define switchPin 6

int main() {
    // Disable GPIO warnings
    wiringPiSetupGpio();

    // Set the switch pin as input
    pinMode(switchPin, INPUT);

    int ButtonONOFF = 0;

    while (1) { // loop
        int inputgpio = digitalRead(switchPin);
        if (ButtonONOFF == inputgpio) {
            system("sudo shutdown -h now");
            delay(60); // 60 milliseconds
        }
    }

    return 0;
}

