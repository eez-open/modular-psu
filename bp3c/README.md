EEZ DIB BP3C is backplane for connecting up to three EEZ DIB peripheral modules. When power modules (e.g. [DCP405](https://github.com/eez-open/modular-psu/tree/master/dcp405)) are plugged into slot #1 and #2, their outputs can be combined under firmware control in one of the following way:

- Serial coupling to double max. output voltage 
- Parallel coupling to double max. output current
- Coupling of all Out- terminals (common GND)
- Ch#1 Out- and Ch#2 Out+ coupling for split rail output

The BP3C backplane provides dedicated BOOT output for each peripheral module that comes with on-board MCU and which firmware could be uploaded via SPI or UART. Programmable reset output is also featured that firmware upload procedure can be initiated without power recycling.
Optionally, a 8-pin 0.1" header for ADXL345 3-axis I2C accelerator module is provided
Dimensions: 110 x 90 mm, 2-layer PCB

### PCB r3B1 preview

![Top side](Images/EEZ_DIB_BP-3C_PCB_top.png)
