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
P 2850 1750
F 0 "R2" H 2909 1796 50  0000 L CNN
F 1 "35kΩ" H 2909 1705 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 2850 1750 50  0001 C CNN
F 3 "~" H 2850 1750 50  0001 C CNN
	1    2850 1750
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:R_Small R3
U 1 1 5DE866ED
P 2850 2150
F 0 "R3" H 2909 2196 50  0000 L CNN
F 1 "30kΩ" H 2909 2105 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 2850 2150 50  0001 C CNN
F 3 "~" H 2850 2150 50  0001 C CNN
	1    2850 2150
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:R_Small R1
U 1 1 5DE86C13
P 2250 1000
F 0 "R1" V 2054 1000 50  0000 C CNN
F 1 "50kΩ" V 2145 1000 50  0000 C CNN
F 2 "Snowflake:0805-R_Handsolder" H 2250 1000 50  0001 C CNN
F 3 "~" H 2250 1000 50  0001 C CNN
	1    2250 1000
	0    1    1    0   
$EndComp
$Comp
L felcana:C_Small C1
U 1 1 5DE87959
P 1650 1850
F 0 "C1" H 1742 1948 50  0000 L CNN
F 1 "C_Small" H 1742 1857 50  0000 L CNN
F 2 "Snowflake:0805-C_Handsolder" H 1650 1850 50  0001 C CNN
F 3 "~" H 1650 1850 50  0001 C CNN
F 4 "Temp_Coef" H 1742 1785 25  0000 L CNN "TempCoef"
F 5 "Vrating" H 1742 1733 25  0000 L CNN "VRating"
	1    1650 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 1500 2850 1500
Wire Wire Line
	2850 1500 2850 1000
Connection ~ 2850 1500
Wire Wire Line
	2850 1500 3000 1500
Wire Wire Line
	1650 1400 2150 1400
Wire Wire Line
	1650 1400 1650 1750
Connection ~ 1650 1400
Wire Wire Line
	2150 1600 2050 1600
Wire Wire Line
	2050 1600 2050 1950
Wire Wire Line
	2050 1950 2850 1950
Wire Wire Line
	2850 1500 2850 1650
Wire Wire Line
	2850 1850 2850 1950
Wire Wire Line
	2850 1950 2850 2050
Connection ~ 2850 1950
Wire Wire Line
	2850 2250 2850 2350
$Comp
L Snowflake:R_POT_Small RV1
U 1 1 5DE8F84F
P 1650 1200
F 0 "RV1" H 1590 1246 50  0000 R CNN
F 1 "200kΩ" H 1590 1155 50  0000 R CNN
F 2 "Snowflake:0805-R_Handsolder" H 1650 1200 50  0001 C CNN
F 3 "~" H 1650 1200 50  0001 C CNN
	1    1650 1200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1650 1300 1650 1400
Wire Wire Line
	2350 1000 2850 1000
Wire Wire Line
	1650 1950 1650 2050
$Comp
L power:GND #PWR0101
U 1 1 5DE9A0B6
P 2850 2350
F 0 "#PWR0101" H 2850 2100 50  0001 C CNN
F 1 "GND" H 2855 2177 50  0000 C CNN
F 2 "" H 2850 2350 50  0001 C CNN
F 3 "" H 2850 2350 50  0001 C CNN
	1    2850 2350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 5DE9A498
P 1650 2050
F 0 "#PWR0102" H 1650 1800 50  0001 C CNN
F 1 "GND" H 1655 1877 50  0000 C CNN
F 2 "" H 1650 2050 50  0001 C CNN
F 3 "" H 1650 2050 50  0001 C CNN
	1    1650 2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	1750 1200 1850 1200
Wire Wire Line
	1850 1200 1850 1000
Wire Wire Line
	1850 1000 2150 1000
Text GLabel 3000 1500 2    50   Input ~ 0
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
F 2 "" H 8000 1300 50  0001 C CNN
F 3 "~" H 8000 1300 50  0001 C CNN
	1    8000 1300
	0    1    1    0   
$EndComp
Wire Wire Line
	8000 1500 8000 1600
Wire Wire Line
	1650 1100 1650 1000
NoConn ~ 1650 1000
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
P 900 1850
F 0 "#PWR0109" H 900 1600 50  0001 C CNN
F 1 "GND" H 905 1677 50  0000 C CNN
F 2 "" H 900 1850 50  0001 C CNN
F 3 "" H 900 1850 50  0001 C CNN
	1    900  1850
	1    0    0    -1  
$EndComp
Text GLabel 900  1050 1    50   Input ~ 0
VBAT
Wire Wire Line
	900  1150 900  1050
Wire Wire Line
	900  1850 900  1750
Wire Notes Line
	500  4000 3700 4000
Wire Notes Line
	3700 4000 3700 500 
Wire Notes Line
	6000 3000 6000 500 
Wire Notes Line
	7500 3000 7500 500 
Wire Notes Line
	9300 3000 9300 500 
Wire Notes Line
	3700 3000 11200 3000
$Comp
L Snowflake:Opamp_Single U1
U 1 1 5DEBF37F
P 2450 1500
F 0 "U1" H 2450 1867 50  0000 C CNN
F 1 "Opamp_Single" H 2450 1776 50  0000 C CNN
F 2 "" H 2450 1500 50  0001 C CNN
F 3 "~" H 2450 1500 50  0001 C CNN
	1    2450 1500
	1    0    0    -1  
$EndComp
$Comp
L Snowflake:Opamp_Single U1
U 2 1 5DEBF9DB
P 900 1450
F 0 "U1" H 958 1496 50  0000 L CNN
F 1 "Opamp_Single" H 958 1405 50  0000 L CNN
F 2 "" H 900 1450 50  0001 C CNN
F 3 "~" H 900 1450 50  0001 C CNN
	2    900  1450
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
$EndSCHEMATC
