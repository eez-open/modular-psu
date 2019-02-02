Modular programmable bench power supply is based on [EEZ H24005](https://github.com/eez-open/psu-hw) project and introduce new digital control and better modularity by using EEZ DIB backplane that allows adding of new functions in the future (e.g. multi-channel power source, 2/4-quadrant power module, multi-channel temperature sensor module, data logger, switch matrix, digital I/O expander, function generator, data acquisition module, etc.). 
It is work in progress and it's conceived to have the following components/modules:

* _[AUX power supply](https://github.com/eez-open/modular-psu/tree/master/aux-ps)_ with AC input protection, soft-start/power-up control, DC fan controller and +5 V / +12 V power outputs
* _[MCU board](https://github.com/eez-open/modular-psu/tree/master/mcu)_ based on STM32F769IGT6 32-bit ARM Cortex-M7 as replacement for Arduino Due
* _[Power pre-regulator CF-DIC](https://github.com/eez-open/CF-DIC)_ as replacement for off-the-shelf AC/DC power module and pre-regulator section on the Power module  (work in progress)
* _[New power module](https://github.com/eez-open/modular-psu/tree/master/dcp505)_ (require power pre-regulator) 0 – 50 V / 5 A with on-board  3-range current auto-ranging and triac OVP circuit
* _[EEZ DIB Backplane](https://github.com/eez-open/modular-psu/tree/master/bp3c)_ with series/parallel power coupling capability of first two modules
* _[Metal enclosure](https://github.com/eez-open/modular-psu/tree/master/enclosure)_ for housing up to 3 modules with 4.3" TFT LCD, dimensions: 290 mm (W) x 119 mm (H) x 240 mm (D)

As a possible alternative for the new power module and power pre-regulator the existing [EEZ H24005 Power module](https://github.com/eez-open/psu-hw/tree/master/Power%20board) will be adopted to new format that can be powered with off-the-shelf 48 Vdc AC/DC power module (fixed output).

### 3-module (Bench Box 3) enclosure front panel preview

![Enclosure front panel](enclosure/DIB_chassis_front_panel.png)