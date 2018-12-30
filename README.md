Modular programmable bench power supply is based on [EEZ H24005](https://github.com/eez-open/psu-hw) project and introduce new digital control and better modularity. It's work in progress and it's conceived to have the following components/modules:

* _[AUX power supply](https://github.com/eez-open/modular-psu/tree/master/aux-ps)_ with AC input protection, soft-start/power-up control, DC fan controller and +5 V / +12 V power outputs
* _[MCU board](https://github.com/eez-open/modular-psu/tree/master/mcu)_ based on STM32F769IGT6 32-bit ARM Cortex-M7 as replacement for Arduino Due
* _[Power preregulator CF-DIC](https://github.com/eez-open/CF-DIC)_ as replacement for off-the-shelf AC/DC power module and preregulator section on the Power module  (work in progress)
* _[New power module](https://github.com/eez-open/modular-psu/tree/master/dcp505)_ (require power pre-regulator) 0 – 50 V / 5 A with on-board  3-range current auto-ranging and triac OVP circuit
* _Backplane_ (coming soon)
* Metal enclosure for housing up to 3 modules with 4.3" TFT LCD, dimensions: 300 mm (W) x 119 mm (H) x 205 mm (D)

As a possible alternative for the new power module and power preregulator the existing [EEZ H24005 Power module](https://github.com/eez-open/psu-hw/tree/master/Power%20board) will be adopted to new format that can be powered with off-the-shelf 48 Vdc AC/DC power module (fixed output).
