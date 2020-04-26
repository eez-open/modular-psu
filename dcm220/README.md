### Overview

The EEZ DIB DCM220 Power module features dual sync buck converters based on [LT3763](https://www.analog.com/en/products/lt3763.html) with programmable output voltage and current limit.

![module](Images/DCM220_r2B8.jpg)

### Feature list
- On-board STM32F373 MCU
Power input: 48 Vdc (e.g. Mean Well LRS-150F-48)
- Max. output power: up to 2 x 80 W
- Voltage regulation (CV), 1 – 20 V. Voltage set resolution (_U_SET_): 12-bit, read resolution (_U_MON_): 15-bit
- Current regulation (CC), 0.3 – 4 A. Current set resolution (_I_SET_): 12-bit, Current read resolution (_I_MON_): 15-bit
- On-board power pre-regulator and bias power supply
- Output Enable (_OE_) and Constant Current mode (_CC_) LED indications
- Output LC filter for improved ripple and noise
- On-board 4 mm power output terminals with standard (19.05 mm) pitch
- Pass-thru connector for Vout- coupling with other DIB power modules
- Galvanically isolated SPI bus for communication with [MCU board](https://github.com/eez-open/modular-psu/tree/master/mcu)
- I2C EEPROM for storing board specific configuration and calibration parameters
- Dimensions: 155 x 95 mm, 2-layer PCB
