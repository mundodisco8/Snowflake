EESchema Schematic File Version 4
LIBS:Snowflake-cache
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
Wire Wire Line
	2850 5050 2750 5050
Wire Wire Line
	2750 5150 2850 5150
$Comp
L Snowflake:Battery_Cell BT1
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
	8000 1900 8000 2100
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
L Snowflake:C_Small C1
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
F 3 "https://assets.nexperia.com/documents/data-sheet/74HC_HCT595.pdf" H 4900 1700 50  0001 C CNN
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
	5400 1450 5800 1450
Wire Wire Line
	5400 1550 5800 1550
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
P 7000 1750
F 0 "D3" V 7046 1682 50  0000 R CNN
F 1 "White" V 6955 1682 50  0000 R CNN
F 2 "Snowflake:0603_LED_HandSolder" V 7000 1750 50  0001 C CNN
F 3 "~" V 7000 1750 50  0001 C CNN
	1    7000 1750
	0    -1   -1   0   
$EndComp
$Comp
L Snowflake:R_Small R4
U 1 1 5DE8E4A3
P 7000 1450
F 0 "R4" H 7059 1496 50  0000 L CNN
F 1 "XYZΩ" H 7059 1405 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 7000 1450 50  0001 C CNN
F 3 "~" H 7000 1450 50  0001 C CNN
	1    7000 1450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 5DE8EBF3
P 7000 1950
F 0 "#PWR0105" H 7000 1700 50  0001 C CNN
F 1 "GND" H 7005 1777 50  0000 C CNN
F 2 "" H 7000 1950 50  0001 C CNN
F 3 "" H 7000 1950 50  0001 C CNN
	1    7000 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 1950 7000 1850
Wire Wire Line
	7000 1650 7000 1600
Wire Wire Line
	7000 1350 7000 1250
Text GLabel 7000 1250 1    50   Input ~ 0
LED0
Text GLabel 5500 1350 2    50   Input ~ 0
LED0
Text GLabel 5800 1450 2    50   Input ~ 0
DRIVE_ROW0
Text GLabel 5800 1550 2    50   Input ~ 0
DRIVE_ROW1
Text GLabel 5700 1550 3    50   Input ~ 0
RESET
$Comp
L Snowflake:SW_SPST SW1
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
Text GLabel 6950 1600 0    50   Input ~ 0
V1
Wire Wire Line
	6950 1600 7000 1600
Connection ~ 7000 1600
Wire Wire Line
	7000 1600 7000 1550
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
Text Notes 6700 1850 1    50   ~ 0
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
	6350 3050 6350 550 
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
L Snowflake:R_Small R5
U 1 1 5DEF1C7E
P 1400 1350
F 0 "R5" H 1459 1396 50  0000 L CNN
F 1 "6.8kΩ" H 1459 1305 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 1400 1350 50  0001 C CNN
F 3 "~" H 1400 1350 50  0001 C CNN
	1    1400 1350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0101
U 1 1 5DEF7581
P 1400 1850
F 0 "#PWR0101" H 1400 1600 50  0001 C CNN
F 1 "GND" H 1405 1677 50  0000 C CNN
F 2 "" H 1400 1850 50  0001 C CNN
F 3 "" H 1400 1850 50  0001 C CNN
	1    1400 1850
	1    0    0    -1  
$EndComp
Text GLabel 1500 1500 2    50   Input ~ 0
VBIAS
$Comp
L power:GND #PWR0102
U 1 1 5DEFC3A0
P 1400 1150
F 0 "#PWR0102" H 1400 900 50  0001 C CNN
F 1 "GND" H 1405 977 50  0000 C CNN
F 2 "" H 1400 1150 50  0001 C CNN
F 3 "" H 1400 1150 50  0001 C CNN
	1    1400 1150
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
$Comp
L Snowflake:Q_DUAL_NMOS Q1
U 1 1 5DF11E19
P 1500 5450
F 0 "Q1" H 1706 5496 50  0000 L CNN
F 1 "Q_DUAL_NMOS" H 1706 5405 50  0000 L CNN
F 2 "Snowflake:SOT-23-6_DMN2004DMK_Handsoldering" H 2250 5300 50  0001 C CNN
F 3 "~" H 1700 5450 50  0001 C CNN
	1    1500 5450
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:Q_DUAL_NMOS Q1
U 2 1 5DF186F5
P 1500 6650
F 0 "Q1" H 1706 6696 50  0000 L CNN
F 1 "Q_DUAL_NMOS" H 1706 6605 50  0000 L CNN
F 2 "Snowflake:SOT-23-6_DMN2004DMK_Handsoldering" H 2250 6500 50  0001 C CNN
F 3 "~" H 1700 6650 50  0001 C CNN
	2    1500 6650
	1    0    0    -1  
$EndComp
Wire Wire Line
	1600 6450 1600 6350
Wire Wire Line
	1600 5650 1600 5750
Wire Wire Line
	1600 5250 1600 5150
Wire Wire Line
	1300 5450 1200 5450
Wire Wire Line
	1300 6650 1200 6650
Wire Wire Line
	1600 6850 1600 6950
$Comp
L power:GND #PWR0106
U 1 1 5DF24FA5
P 1600 5750
F 0 "#PWR0106" H 1600 5500 50  0001 C CNN
F 1 "GND" H 1605 5577 50  0000 C CNN
F 2 "" H 1600 5750 50  0001 C CNN
F 3 "" H 1600 5750 50  0001 C CNN
	1    1600 5750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0107
U 1 1 5DF256CD
P 1600 6950
F 0 "#PWR0107" H 1600 6700 50  0001 C CNN
F 1 "GND" H 1605 6777 50  0000 C CNN
F 2 "" H 1600 6950 50  0001 C CNN
F 3 "" H 1600 6950 50  0001 C CNN
	1    1600 6950
	1    0    0    -1  
$EndComp
Text GLabel 1200 5450 0    50   Input ~ 0
DRIVE_ROW0
Text GLabel 1200 6650 0    50   Input ~ 0
DRIVE_ROW1
Wire Wire Line
	2750 6050 2850 6050
Wire Wire Line
	2850 5950 2750 5950
Text GLabel 2750 6050 0    50   Input ~ 0
ROW1
Text GLabel 2750 5950 0    50   Input ~ 0
ROW0
Wire Wire Line
	2750 6900 2850 6900
Wire Wire Line
	2850 6800 2750 6800
Text GLabel 2750 6900 0    50   Input ~ 0
ROW1
Text GLabel 2750 6800 0    50   Input ~ 0
ROW0
Wire Wire Line
	4250 6900 4350 6900
Wire Wire Line
	4350 6800 4250 6800
Text GLabel 4250 6900 0    50   Input ~ 0
ROW1
Text GLabel 4250 6800 0    50   Input ~ 0
ROW0
Wire Wire Line
	4250 6050 4350 6050
Wire Wire Line
	4350 5950 4250 5950
Text GLabel 4250 6050 0    50   Input ~ 0
ROW1
Text GLabel 4250 5950 0    50   Input ~ 0
ROW0
Wire Wire Line
	4250 5150 4350 5150
Wire Wire Line
	4350 5050 4250 5050
Text GLabel 4250 5150 0    50   Input ~ 0
ROW1
Text GLabel 4250 5050 0    50   Input ~ 0
ROW0
Text GLabel 2750 5050 0    50   Input ~ 0
ROW0
Text GLabel 2750 5150 0    50   Input ~ 0
ROW1
$Sheet
S 4350 4900 1000 650 
U 5DD0ACE2
F0 "Stem 4" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 4350 5050 50 
F3 "VLED1" I L 4350 5150 50 
$EndSheet
$Sheet
S 4350 5800 1000 650 
U 5DD0BF7E
F0 "Stem 5" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 4350 5950 50 
F3 "VLED1" I L 4350 6050 50 
$EndSheet
$Sheet
S 4350 6650 1000 650 
U 5DD0D430
F0 "Stem 6" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 4350 6800 50 
F3 "VLED1" I L 4350 6900 50 
$EndSheet
$Sheet
S 2850 6650 1000 650 
U 5DD09BFC
F0 "Stem 3" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 2850 6800 50 
F3 "VLED1" I L 2850 6900 50 
$EndSheet
$Sheet
S 2850 5800 1000 650 
U 5DD08BF1
F0 "Stem 2" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 2850 5950 50 
F3 "VLED1" I L 2850 6050 50 
$EndSheet
$Sheet
S 2850 4900 1000 650 
U 5DCE640D
F0 "Led Stem 1" 50
F1 "LED_Stem.sch" 50
F2 "VLED0" I L 2850 5050 50 
F3 "VLED1" I L 2850 5150 50 
$EndSheet
Text GLabel 1600 5150 1    50   Input ~ 0
ROW0
Text GLabel 1600 6350 1    50   Input ~ 0
ROW1
NoConn ~ 1300 1650
$Comp
L Snowflake:TL431D U3
U 1 1 5DEF05F4
P 1400 1650
F 0 "U3" V 1446 1580 50  0000 R CNN
F 1 "LM4041_1.2V" V 1355 1580 50  0000 R CNN
F 2 "Snowflake:SOT-23_LM4041_1.2V_Handsolder" H 1400 1400 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/LM4040-41-Precision-Micropower-Shunt-Voltage-Reference-DS20005757B.pdf" H 1400 1650 50  0001 C CIN
	1    1400 1650
	0    -1   -1   0   
$EndComp
Wire Wire Line
	1400 1850 1400 1750
Wire Wire Line
	1400 1550 1400 1500
Wire Wire Line
	1400 1500 1500 1500
Connection ~ 1400 1500
Wire Wire Line
	1400 1500 1400 1450
Wire Wire Line
	1400 1250 1400 1150
$Comp
L Device:R R6
U 1 1 5DF2400A
P 9400 4150
F 0 "R6" H 9470 4196 50  0000 L CNN
F 1 "0" H 9470 4105 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" V 9330 4150 50  0001 C CNN
F 3 "~" H 9400 4150 50  0001 C CNN
	1    9400 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 3900 9400 4000
Wire Wire Line
	9400 4400 9400 4300
$Comp
L power:GND #PWR0110
U 1 1 5DF28486
P 9400 3900
F 0 "#PWR0110" H 9400 3650 50  0001 C CNN
F 1 "GND" H 9405 3727 50  0000 C CNN
F 2 "" H 9400 3900 50  0001 C CNN
F 3 "" H 9400 3900 50  0001 C CNN
	1    9400 3900
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR0111
U 1 1 5DF28908
P 9400 4400
F 0 "#PWR0111" H 9400 4150 50  0001 C CNN
F 1 "GND" H 9405 4227 50  0000 C CNN
F 2 "" H 9400 4400 50  0001 C CNN
F 3 "" H 9400 4400 50  0001 C CNN
	1    9400 4400
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:MountingHole H1
U 1 1 5DF39162
P 9900 4150
F 0 "H1" H 10000 4196 50  0000 L CNN
F 1 "MountingHole" H 10000 4105 50  0000 L CNN
F 2 "Snowflake:MountingHole_2.1mm_M2" H 9900 4150 50  0001 C CNN
F 3 "~" H 9900 4150 50  0001 C CNN
	1    9900 4150
	1    0    0    -1  
$EndComp
$EndSCHEMATC
