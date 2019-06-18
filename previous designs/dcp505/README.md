### Overview

The core of the EEZ DIB DCP505 Power board still represents adopted Leonid Ivanovitch design that is used in [EEZ H24005 Power board](https://github.com/eez-open/psu-hw/tree/master/Power%20board). The major improvements on this board include new form factor for housing in the EEZ DIB enclosure, 3-range autoranging circuit, OVP with triac and local EEPROM storage. 

### Feature list
- Power input: [EEZ CF-DIC]((https://github.com/eez-open/CF-DIC)_) power pre-regulator and bias power supply
- Power output: 250 W (max. 5 A)
- Voltage regulation (CV), 0 – 50 V. Voltage set (_U_SET_) resolution: 16-bit, read resolution (_U_MON_): 15-bit
- Current regulation (CC) with 3-range (50 mA, 500 mA, 5 A) **on-board auto-ranging circuit**. Current set resolution (_I_SET_): 16-bit, Current read resolution (_I_MON_): 15-bit for each range (i.e. 1.5 uA / 15 uA / 0.15 mA)
- **On-board OVP** with triac and two fuses
- Down-programmer
- Temperature sensor (SPI)
- Output enable (OE) circuit with LED indicator
- Fault/Powergood LED indicator
- On-board output terminals
- Pass-thru connector for serial and parallel coupling with other Power board
- Remote voltage sense with LED indicator and inverse polarity protection
- Remote voltage programming with LED indicator
- External digital trigger (3.3 or 5 V logic level)
- Galvanically isolated SPI bus for communication with [MCU board](https://github.com/eez-open/modular-psu/tree/master/mcu)
- I2C EEPROM for storing board specific configuration and calibration parameters
- Dimensions: 160 x 95 mm, 2-layer PCB

### Spice simulations

- [Current auto-ranging](https://github.com/eez-open/modular-psu/tree/master/dcp505/Spice/Auto-ranging) (LTspice)
- [OVP simulations](https://github.com/eez-open/modular-psu/tree/master/dcp505/Spice/OVP) (LTspice)

### r1B2 prototype (without OVP)

![Top side](Images/DCP505_r1B2_prototype.jpg)

