[![GitHub release](https://img.shields.io/github/release/eez-open/modular-psu.svg)](https://github.com/eez-open/modular-psu/releases) [![liberapay](https://img.shields.io/liberapay/receives/eez-open.svg?logo=liberapay)](https://liberapay.com/eez-open/donate)

![Enclosure 3D model](enclosure/eez_bb3_chassis.jpg)

### Ownership and License
The contributors are listed in CONTRIB.TXT. This project uses the TAPR v1.0 license, see LICENSE.TXT.

[![OSHW-HR000002](OSHW_UID_HR2.svg)](https://certification.oshwa.org/hr000002.html)

### Introduction

EEZ Bench Box 3 (BB3) represents a new category of *modular* Test and Measurement (T&M) equipment. It provides a complete open-source hardware and software framework that bridges the gap between – and combines the best features of – DIY hobbyist tools and professional benchtop equipment. 
BB3 was inspired by the [EEZ H24005](https://github.com/eez-open/psu-hw) power supply project ([OSHWA UID HR000001](https://certification.oshwa.org/hr000001.html)), which attracted many enthusiasts with its broad feature-set, rich user interface, DIY-friendliness, and fully open-source design. 
It initially comes with two DC power modules (hence the name of repository *modular-psu*) and will be expanded with new T&M modules (e.g. multi-channel power source, 2/4-quadrant power module, multi-channel temperature sensor module, data logger, switch matrix, digital I/O expander, function generator, data acquisition module, etc.). 
BB3 is made up of the following components:

* _[BP3C](https://github.com/eez-open/modular-psu/tree/master/bp3c)_ EEZ DIB backplane with power output coupling capability of first two modules
* _[AUX power supply](https://github.com/eez-open/modular-psu/tree/master/aux-ps)_ board with AC input protection, soft-start/power-up control, DC fan controller and +5 V / +12 V power outputs
* _[MCU](https://github.com/eez-open/modular-psu/tree/master/mcu)_ board based on STM32F769IIT6 32-bit ARM Cortex-M7
* _[DCP405](https://github.com/eez-open/modular-psu/tree/master/dcp405)_, 0 - 40 V / 50 mA / 5 A DC power source module
* _[DCM220](https://github.com/eez-open/modular-psu/tree/master/dcm220)_, dual sync buck 0 - 20 V / max. 4 A module
* _[Metal enclosure](https://github.com/eez-open/modular-psu/tree/master/enclosure)_ for housing up to 3 modules with 4.3" TFT LCD. Dimensions: 290 (W) x 123 (H) x 240 (D) mm

### Supported technologies

* SCPI (Reference Guide in [PDF](https://github.com/eez-open/modular-psu-firmware/blob/master/docs/SCPI%20reference%20guide/EEZ%20BB3%20SCPI%20reference%20guide.pdf))
* MicroPython (script [examples](https://github.com/eez-open/modular-psu-firmware/tree/master/scripts), an example [video](https://www.youtube.com/watch?v=I0y6fgv8G00))
* MQTT (an intro [video](https://www.youtube.com/watch?v=THyfLSSAhrI))
* Node-RED integration (an intro [video](https://www.youtube.com/watch?v=0xQ6Xuq53fA))

### Other DIB modules

* [MIO168](https://github.com/eez-open/dib-mio168) Mixed I/O module
* [PREL6](https://github.com/eez-open/dib-prel6) power relays module
* [SMX46](https://github.com/eez-open/dib-smx46) programmable switch matrix module
* [MUX14D](https://github.com/eez-open/dib-mux14d) dual 7:1 reed relay 2-wire multiplexer

### Related topics and links

* EEZ BB3 [firmware](https://github.com/eez-open/modular-psu-firmware)
* [EEZ Studio](https://www.envox.eu/studio/studio-introduction)
* EEZ [DIB v1.0](https://github.com/eez-open/modular-psu/tree/master/DIB) specification
* [Discord](https://discord.gg/dhYMnCB) server
* [YouTube](https://www.youtube.com/c/eezopen) channel
* [EEVblog forum](https://www.eevblog.com/forum/projects/eez-h25005-a-possible-successor-of-eez-h24005-programmable-power-supply/) discussion
* [Crowd Supply](https://www.crowdsupply.com/envox/eez-bb3) crowdfunding landing page
* [Liberpay](https://liberapay.com/eez-open/donate) donations


Please note that some previous board types and revisions that could be still usable in some cases can be found under *[previous design](https://github.com/eez-open/modular-psu/tree/master/previous%20designs)* folder.
