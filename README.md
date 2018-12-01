# OrangePi.GPIO_Examples

I tested on OrangePi ONE with Raspbian operating system

  -	More information about [OrangePi_One](http://www.orangepi.org/orangepione/) or [here](http://linux-sunxi.org/Orange_Pi_One#Expansion_Port)
  -	[Raspbian](http://www.orangepi.org/downloadresources/orangepipc/oragepipc_e930546e866b23585721e5d2a6.html) operating    system for OrangePi One
  - The library that i used [OPi.GPIO](https://github.com/Jeremie-C/OrangePi.GPIO)
  
# OrangePi One GPIO Pin Layout

<table class="wikitable" style="width:700px;">
<tbody><tr>
<th colspan="4"> 2x20 Header
</th></tr>
<tr>
<td> 1 </td>
<td> <i>3.3V</i>
</td>
<td> 2 </td>
<td> <i>5V</i>
</td></tr>
<tr>
<td> 3 </td>
<td> PA12 <small>(TWI0_SDA/DI_RX/PA_EINT12)</small>
</td>
<td> 4 </td>
<td> <i>5V</i>
</td></tr>
<tr>
<td> 5 </td>
<td> PA11 <small>(TWI0_SCK/DI_TX/PA_EINT11)</small>
</td>
<td> 6 </td>
<td> <i>GND</i>
</td></tr>
<tr>
<td> 7 </td>
<td> PA6 <small>(SIM_PWREN/PWM1/PA_EINT6)</small>
</td>
<td> 8 </td>
<td> PA13 <small>(SPI1_CS/UART3_TX/PA_EINT13)</small>
</td></tr>
<tr>
<td> 9 </td>
<td> <i>GND</i>
</td>
<td> 10 </td>
<td> PA14 <small>(SPI1_CLK/UART3_RX/PA_EINT14)</small>
</td></tr>
<tr>
<td> 11 </td>
<td> PA1 <small>(UART2_RX/JTAG_CK/PA_EINT1)</small>
</td>
<td> 12 </td>
<td> PD14
</td></tr>
<tr>
<td> 13 </td>
<td> PA0 <small>(UART2_TX/JTAG_MS/PA_EINT0)</small>
</td>
<td> 14 </td>
<td> <i>GND</i>
</td></tr>
<tr>
<td> 15 </td>
<td> PA3 <small>(UART2_CTS/JTAG_DI/PA_EINT3)</small>
</td>
<td> 16 </td>
<td> PC4
</td></tr>
<tr>
<td> 17 </td>
<td> <i>3.3V</i>
</td>
<td> 18 </td>
<td> PC7
</td></tr>
<tr>
<td> 19 </td>
<td> PC0 <small>(SPI0_MOSI)</small>
</td>
<td> 20 </td>
<td> <i>GND</i>
</td></tr>
<tr>
<td> 21 </td>
<td> PC1 <small>(SPI0_MISO)</small>
</td>
<td> 22 </td>
<td> PA2 <small>(UART2_RTS/JTAG_DO/PA_EINT2)</small>
</td></tr>
<tr>
<td> 23 </td>
<td> PC2 <small>(SPI0_CLK)</small>
</td>
<td> 24 </td>
<td> PC3 <small>(SPI0_CS)</small>
</td></tr>
<tr>
<td> 25 </td>
<td> <i>GND</i>
</td>
<td> 26 </td>
<td> PA21 <small>(PCM0_DIN/SIM_VPPPP/PA_EINT21)</small>
</td></tr>
<tr>
<td> 27 </td>
<td> PA19 <small>(PCM0_CLK/TWI1_SDA/PA_EINT19)</small>
</td>
<td> 28 </td>
<td> PA18 <small>(PCM0_SYNC/TWI1_SCK/PA_EINT18)</small>
</td></tr>
<tr>
<td> 29 </td>
<td> PA7 <small>(SIM_CLK/PA_EINT7)</small>
</td>
<td> 30 </td>
<td> <i>GND</i>
</td></tr>
<tr>
<td> 31 </td>
<td> PA8 <small>(SIM_DATA/PA_EINT8)</small>
</td>
<td> 32 </td>
<td> PG8 <small>(UART1_RTS/PG_EINT8)</small>
</td></tr>
<tr>
<td> 33 </td>
<td> PA9 <small>(SIM_RST/PA_EINT9)</small>
</td>
<td> 34 </td>
<td> <i>GND</i>
</td></tr>
<tr>
<td> 35 </td>
<td> PA10 <small>(SIM_DET/PA_EINT10)</small>
</td>
<td> 36 </td>
<td> PG9 <small>(UART1_CTS/PG_EINT9)</small>
</td></tr>
<tr>
<td> 37 </td>
<td> PA20 <small>(PCM0_DOUT/SIM_VPPEN/PA_EINT20)</small>
</td>
<td> 38 </td>
<td> PG6 <small>(UART1_TX/PG_EINT6)</small>
</td></tr>
<tr>
<td> 39 </td>
<td> <i>GND</i>
</td>
<td> 40 </td>
<td> PG7 <small>(UART1_RX/PG_EINT7)</small>
</td></tr></tbody></table>
