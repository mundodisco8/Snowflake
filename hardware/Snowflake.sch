EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text GLabel 950  5100 0    50   Input ~ 0
ROW1
Wire Wire Line
	1050 5000 950  5000
$Sheet
S 1050 4850 1000 650 
U 5DCE640D
F0 "Led Stem 1" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 1050 5000 50 
F3 "VLED1" I L 1050 5100 50 
F4 "VK" I L 1050 5350 50 
$EndSheet
Wire Wire Line
	950  5100 1050 5100
Text GLabel 950  5900 0    50   Input ~ 0
ROW0
Text GLabel 950  6000 0    50   Input ~ 0
ROW1
Wire Wire Line
	1050 5900 950  5900
$Sheet
S 1050 5750 1000 650 
U 5DD08BF1
F0 "Stem 2" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 1050 5900 50 
F3 "VLED1" I L 1050 6000 50 
$EndSheet
Wire Wire Line
	950  6000 1050 6000
Text GLabel 950  6750 0    50   Input ~ 0
ROW0
Text GLabel 950  6850 0    50   Input ~ 0
ROW1
Wire Wire Line
	1050 6750 950  6750
$Sheet
S 1050 6600 1000 650 
U 5DD09BFC
F0 "Stem 3" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 1050 6750 50 
F3 "VLED1" I L 1050 6850 50 
$EndSheet
Wire Wire Line
	950  6850 1050 6850
Text GLabel 2450 5000 0    50   Input ~ 0
ROW0
Text GLabel 2450 5100 0    50   Input ~ 0
ROW1
Wire Wire Line
	2550 5000 2450 5000
$Sheet
S 2550 4850 1000 650 
U 5DD0ACE2
F0 "Stem 4" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 2550 5000 50 
F3 "VLED1" I L 2550 5100 50 
$EndSheet
Wire Wire Line
	2450 5100 2550 5100
Text GLabel 2450 5900 0    50   Input ~ 0
ROW0
Text GLabel 2450 6000 0    50   Input ~ 0
ROW1
Wire Wire Line
	2550 5900 2450 5900
$Sheet
S 2550 5750 1000 650 
U 5DD0BF7E
F0 "Stem 5" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 2550 5900 50 
F3 "VLED1" I L 2550 6000 50 
$EndSheet
Wire Wire Line
	2450 6000 2550 6000
Text GLabel 2450 6750 0    50   Input ~ 0
ROW0
Text GLabel 2450 6850 0    50   Input ~ 0
ROW1
Wire Wire Line
	2550 6750 2450 6750
$Sheet
S 2550 6600 1000 650 
U 5DD0D430
F0 "Stem 6" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 2550 6750 50 
F3 "VLED1" I L 2550 6850 50 
$EndSheet
Wire Wire Line
	2450 6850 2550 6850
$Comp
L Device:Battery BT1
U 1 1 5DCE8C77
P 8000 1800
F 0 "BT1" H 8108 1846 50  0000 L CNN
F 1 "Battery" H 8108 1755 50  0000 L CNN
F 2 "Snowflake:Battery_Holder-AAA" V 8000 1860 50  0001 C CNN
F 3 "~" V 8000 1860 50  0001 C CNN
	1    8000 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	8000 1100 8000 1000
Wire Wire Line
	8000 2000 8000 2100
$Comp
L power:GND #PWR0130
U 1 1 5DCED3CD
P 8000 2100
F 0 "#PWR0130" H 8000 1850 50  0001 C CNN
F 1 "GND" H 8005 1927 50  0000 C CNN
F 2 "" H 8000 2100 50  0001 C CNN
F 3 "" H 8000 2100 50  0001 C CNN
	1    8000 2100
	1    0    0    -1  
$EndComp
Text GLabel 8000 1000 1    50   Input ~ 0
VBAT
$Comp
L power:PWR_FLAG #FLG0101
U 1 1 5DCF0073
P 8750 1600
F 0 "#FLG0101" H 8750 1675 50  0001 C CNN
F 1 "PWR_FLAG" V 8750 1728 50  0000 L CNN
F 2 "" H 8750 1600 50  0001 C CNN
F 3 "~" H 8750 1600 50  0001 C CNN
	1    8750 1600
	0    1    1    0   
$EndComp
Wire Wire Line
	8750 1600 8600 1600
Text GLabel 8600 1600 0    50   Input ~ 0
VBAT
$Comp
L Snowflake:R_Small R2
U 1 1 5DE85FD7
P 3275 1725
F 0 "R2" H 3334 1771 50  0000 L CNN
F 1 "35kΩ" H 3334 1680 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 3275 1725 50  0001 C CNN
F 3 "~" H 3275 1725 50  0001 C CNN
	1    3275 1725
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:R_Small R3
U 1 1 5DE866ED
P 3275 2125
F 0 "R3" H 3334 2171 50  0000 L CNN
F 1 "30kΩ" H 3334 2080 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 3275 2125 50  0001 C CNN
F 3 "~" H 3275 2125 50  0001 C CNN
	1    3275 2125
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:R_Small R1
U 1 1 5DE86C13
P 2675 975
F 0 "R1" V 2479 975 50  0000 C CNN
F 1 "50kΩ" V 2570 975 50  0000 C CNN
F 2 "Snowflake:0805-R_Handsolder" H 2675 975 50  0001 C CNN
F 3 "~" H 2675 975 50  0001 C CNN
	1    2675 975 
	0    1    1    0   
$EndComp
$Comp
L felcana:C_Small C1
U 1 1 5DE87959
P 2075 1825
F 0 "C1" H 2167 1923 50  0000 L CNN
F 1 "C_Small" H 2167 1832 50  0000 L CNN
F 2 "Snowflake:0805-C_Handsolder" H 2075 1825 50  0001 C CNN
F 3 "~" H 2075 1825 50  0001 C CNN
F 4 "Temp_Coef" H 2167 1760 25  0000 L CNN "TempCoef"
F 5 "Vrating" H 2167 1708 25  0000 L CNN "VRating"
	1    2075 1825
	1    0    0    -1  
$EndComp
Wire Wire Line
	3175 1475 3275 1475
Wire Wire Line
	3275 1475 3275 975 
Connection ~ 3275 1475
Wire Wire Line
	3275 1475 3425 1475
Wire Wire Line
	2075 1375 2575 1375
Wire Wire Line
	2075 1375 2075 1725
Connection ~ 2075 1375
Wire Wire Line
	2575 1575 2475 1575
Wire Wire Line
	2475 1575 2475 1925
Wire Wire Line
	2475 1925 3275 1925
Wire Wire Line
	3275 1475 3275 1625
Wire Wire Line
	3275 1825 3275 1925
Wire Wire Line
	3275 1925 3275 2025
Connection ~ 3275 1925
Wire Wire Line
	3275 2225 3275 2325
$Comp
L Snowflake:R_POT_Small RV1
U 1 1 5DE8F84F
P 2075 1175
F 0 "RV1" H 2015 1221 50  0000 R CNN
F 1 "200kΩ" H 2015 1130 50  0000 R CNN
F 2 "Snowflake:Potentiometer_TC33X-2-204E" H 2075 1175 50  0001 C CNN
F 3 "https://www.bourns.com/docs/Product-Datasheets/TC33.pdf" H 2075 1175 50  0001 C CNN
	1    2075 1175
	1    0    0    -1  
$EndComp
Wire Wire Line
	2075 1275 2075 1375
Wire Wire Line
	2775 975  3275 975 
Wire Wire Line
	2175 1175 2275 1175
Wire Wire Line
	2275 1175 2275 975 
Wire Wire Line
	2275 975  2575 975 
Text GLabel 3425 1475 2    50   Input ~ 0
CLK
Text GLabel 4300 1150 0    50   Input ~ 0
CLK
$Comp
L power:GND #PWR0103
U 1 1 5DEA49B0
P 4950 2250
F 0 "#PWR0103" H 4950 2000 50  0001 C CNN
F 1 "GND" H 4955 2077 50  0000 C CNN
F 2 "" H 4950 2250 50  0001 C CNN
F 3 "" H 4950 2250 50  0001 C CNN
	1    4950 2250
	1    0    0    -1  
$EndComp
Text GLabel 4950 850  1    50   Input ~ 0
VBAT
$Comp
L power:GND #PWR0104
U 1 1 5DEB8DFB
P 4150 2000
F 0 "#PWR0104" H 4150 1750 50  0001 C CNN
F 1 "GND" H 4155 1827 50  0000 C CNN
F 2 "" H 4150 2000 50  0001 C CNN
F 3 "" H 4150 2000 50  0001 C CNN
	1    4150 2000
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:74HC595 U2
U 1 1 5DE80081
P 4950 1550
F 0 "U2" H 5250 2100 50  0000 C CNN
F 1 "74HC595" H 5200 1000 40  0000 C CNN
F 2 "Snowflake:16-TSSOP_5x6.5mm_P0.65-74HC565" H 4900 1700 50  0001 C CNN
F 3 "" H 4900 1700 50  0001 C CNN
	1    4950 1550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 950  4950 850 
Wire Wire Line
	5400 1250 5500 1250
Wire Wire Line
	5400 1350 5500 1350
Wire Wire Line
	4950 2150 4950 2250
Wire Wire Line
	4500 1250 4400 1250
Wire Wire Line
	4500 1150 4400 1150
Wire Wire Line
	4500 1800 4450 1800
Wire Wire Line
	5400 1450 5500 1450
Wire Wire Line
	5400 1550 5500 1550
Wire Wire Line
	5500 1150 5400 1150
Wire Wire Line
	5400 1650 5500 1650
Wire Wire Line
	5400 1750 5500 1750
Wire Wire Line
	5400 1850 5500 1850
Wire Wire Line
	5400 1950 5500 1950
NoConn ~ 5500 1150
NoConn ~ 5500 1950
NoConn ~ 5500 1850
NoConn ~ 5500 1750
NoConn ~ 5500 1650
Text GLabel 4450 1800 0    50   Input ~ 0
RESET
Wire Wire Line
	4150 1550 4150 1900
Wire Wire Line
	4150 1550 4500 1550
Wire Wire Line
	4150 1900 4500 1900
Wire Wire Line
	4150 1900 4150 2000
Connection ~ 4150 1900
Wire Wire Line
	4400 1250 4400 1150
Wire Wire Line
	4400 1150 4300 1150
Connection ~ 4400 1150
$Comp
L Snowflake:LED_Small_ALT D3
U 1 1 5DE8DAC0
P 6800 1750
F 0 "D3" V 6846 1682 50  0000 R CNN
F 1 "White" V 6755 1682 50  0000 R CNN
F 2 "Snowflake:0603_LED_HandSolder" V 6800 1750 50  0001 C CNN
F 3 "~" V 6800 1750 50  0001 C CNN
	1    6800 1750
	0    -1   -1   0   
$EndComp
$Comp
L Snowflake:R_Small R4
U 1 1 5DE8E4A3
P 6800 1450
F 0 "R4" H 6859 1496 50  0000 L CNN
F 1 "XYZΩ" H 6859 1405 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 6800 1450 50  0001 C CNN
F 3 "~" H 6800 1450 50  0001 C CNN
	1    6800 1450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 5DE8EBF3
P 6800 1950
F 0 "#PWR0105" H 6800 1700 50  0001 C CNN
F 1 "GND" H 6805 1777 50  0000 C CNN
F 2 "" H 6800 1950 50  0001 C CNN
F 3 "" H 6800 1950 50  0001 C CNN
	1    6800 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6800 1950 6800 1850
Wire Wire Line
	6800 1650 6800 1600
Wire Wire Line
	6800 1350 6800 1250
Text GLabel 6800 1250 1    50   Input ~ 0
LED0
Text GLabel 950  5000 0    50   Input ~ 0
ROW0
Text GLabel 5500 1350 2    50   Input ~ 0
LED0
Text GLabel 5500 1450 2    50   Input ~ 0
ROW0
Text GLabel 5500 1550 2    50   Input ~ 0
ROW1
Text GLabel 5500 1550 3    50   Input ~ 0
RESET
$Comp
L Switch:SW_SPST SW1
U 1 1 5DE9961F
P 8000 1300
F 0 "SW1" V 7954 1398 50  0000 L CNN
F 1 "SW_SPST" V 8045 1398 50  0000 L CNN
F 2 "Snowflake:Slide_Switch_JS202011SCQN" H 8000 1300 50  0001 C CNN
F 3 "https://dznh3ojzb2azq.cloudfront.net/products/Slide/JS/documents/datasheet.pdf" H 8000 1300 50  0001 C CNN
	1    8000 1300
	0    1    1    0   
$EndComp
Wire Wire Line
	8000 1500 8000 1600
Wire Wire Line
	2075 1075 2075 975 
NoConn ~ 2075 975 
Text GLabel 6750 1600 0    50   Input ~ 0
V1
Wire Wire Line
	6750 1600 6800 1600
Connection ~ 6800 1600
Wire Wire Line
	6800 1600 6800 1550
Wire Wire Line
	9600 1650 9600 1750
Wire Wire Line
	9600 1250 9600 1150
$Comp
L power:GND #PWR0108
U 1 1 5DEA9D26
P 9600 1750
F 0 "#PWR0108" H 9600 1500 50  0001 C CNN
F 1 "GND" H 9605 1577 50  0000 C CNN
F 2 "" H 9600 1750 50  0001 C CNN
F 3 "" H 9600 1750 50  0001 C CNN
	1    9600 1750
	1    0    0    -1  
$EndComp
Text GLabel 9600 1150 1    50   Input ~ 0
V1
Text Notes 1300 3350 0    50   ~ 0
Astable Multivibrator\nR2 and R3 add some hysteresis to the comparison\nB=R3/R2+R3 and the switching point is +/- B Vdd\n\nThe period of the square signal is\nT = 2RC * ln ( 1+B/1-B)\n\nBy making B so 1+B/1-B is e, \nT = 2RC -> f = 1/2RC
Text Notes 9400 2300 0    50   ~ 0
Note: The pins in this part are a little hack \nto use two of the copper arms as conducting\n traces for the centre LED
Text Notes 6500 1850 1    50   ~ 0
Centre LED\n
$Comp
L power:GND #PWR0109
U 1 1 5DEB46EF
P 650 1950
F 0 "#PWR0109" H 650 1700 50  0001 C CNN
F 1 "GND" H 655 1777 50  0000 C CNN
F 2 "" H 650 1950 50  0001 C CNN
F 3 "" H 650 1950 50  0001 C CNN
	1    650  1950
	1    0    0    -1  
$EndComp
Text GLabel 650  1150 1    50   Input ~ 0
VBAT
Wire Wire Line
	650  1250 650  1150
Wire Wire Line
	650  1950 650  1850
Wire Notes Line
	500  4000 3700 4000
Wire Notes Line
	6000 3000 6000 500 
Wire Notes Line
	7500 3000 7500 500 
Wire Notes Line
	9300 3000 9300 500 
Wire Notes Line
	3700 3000 11200 3000
$Comp
L Snowflake:Opamp_Single_MCP6001 U1
U 1 1 5DEBF37F
P 2875 1475
F 0 "U1" H 2875 1842 50  0000 C CNN
F 1 "Opamp_Single" H 2875 1751 50  0000 C CNN
F 2 "Snowflake:Op_Amp_SOT23_MCP6001T" H 2875 1475 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20001733K.pdf" H 2875 1475 50  0001 C CNN
	1    2875 1475
	1    0    0    1   
$EndComp
$Comp
L Snowflake:Opamp_Single_MCP6001 U1
U 2 1 5DEBF9DB
P 650 1550
F 0 "U1" H 708 1596 50  0000 L CNN
F 1 "Opamp_Single" H 708 1505 50  0000 L CNN
F 2 "Snowflake:Op_Amp_SOT23_MCP6001T" H 650 1550 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20001733K.pdf" H 650 1550 50  0001 C CNN
	2    650  1550
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:Snowflake Logo1
U 1 1 5DEC275F
P 10400 1400
F 0 "Logo1" H 10866 1400 40  0000 L CNN
F 1 "Snowflake" H 10700 950 60  0001 C CNN
F 2 "Snowflake:Snowflake" V 10500 1400 25  0001 C CNN
F 3 "" H 10650 1500 50  0001 C CNN
	1    10400 1400
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:Snowflake Logo1
U 2 1 5DEC2E31
P 9600 1450
F 0 "Logo1" H 9658 1450 40  0000 L CNN
F 1 "Snowflake" H 9900 1000 60  0001 C CNN
F 2 "Snowflake:Snowflake" V 9700 1450 25  0001 C CNN
F 3 "" H 9850 1550 50  0001 C CNN
	2    9600 1450
	1    0    0    -1  
$EndComp
Wire Notes Line
	3700 4000 3700 500 
$Comp
L Snowflake:TL431D U?
U 1 1 5DEF05F4
P 1425 1700
F 0 "U?" V 1471 1630 50  0000 R CNN
F 1 "LM4041_1.2V" V 1380 1630 50  0000 R CNN
F 2 "Snowflake:SOT-23_LM4041_1.2V_Handsolder" H 1425 1450 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/LM4040-41-Precision-Micropower-Shunt-Voltage-Reference-DS20005757B.pdf" H 1425 1700 50  0001 C CIN
	1    1425 1700
	0    -1   -1   0   
$EndComp
$Comp
L Snowflake:R_Small R?
U 1 1 5DEF1C7E
P 1425 1375
F 0 "R?" H 1484 1421 50  0000 L CNN
F 1 "6.8kΩ" H 1484 1330 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 1425 1375 50  0001 C CNN
F 3 "~" H 1425 1375 50  0001 C CNN
	1    1425 1375
	1    0    0    -1  
$EndComp
Wire Wire Line
	1325 1700 1275 1700
Wire Wire Line
	1275 1700 1275 1550
Wire Wire Line
	1425 1550 1425 1600
Wire Wire Line
	1425 1550 1425 1475
Connection ~ 1425 1550
Wire Wire Line
	1425 1275 1425 1200
Wire Wire Line
	1425 1800 1425 1900
$Comp
L power:GND #PWR?
U 1 1 5DEF7581
P 1425 1900
F 0 "#PWR?" H 1425 1650 50  0001 C CNN
F 1 "GND" H 1430 1727 50  0000 C CNN
F 2 "" H 1425 1900 50  0001 C CNN
F 3 "" H 1425 1900 50  0001 C CNN
	1    1425 1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	1275 1550 1425 1550
Wire Wire Line
	1425 1550 1525 1550
Text GLabel 1525 1550 2    50   Input ~ 0
VBIAS
$Comp
L power:GND #PWR?
U 1 1 5DEFC3A0
P 1425 1200
F 0 "#PWR?" H 1425 950 50  0001 C CNN
F 1 "GND" H 1430 1027 50  0000 C CNN
F 2 "" H 1425 1200 50  0001 C CNN
F 3 "" H 1425 1200 50  0001 C CNN
	1    1425 1200
	-1   0    0    1   
$EndComp
Text GLabel 1975 2325 0    50   Input ~ 0
VBIAS
Wire Wire Line
	3275 2325 2075 2325
Wire Wire Line
	2075 1925 2075 2325
Wire Wire Line
	1975 2325 2075 2325
Connection ~ 2075 2325
$EndSCHEMATC
