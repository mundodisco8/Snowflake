EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Snowflake:LED_Small_ALT D1
U 1 1 5DCE67D4
P 2000 2600
AR Path="/5DCE640D/5DCE67D4" Ref="D1"  Part="1" 
AR Path="/5DCECA79/5DCE67D4" Ref="D7"  Part="1" 
AR Path="/5DCED58A/5DCE67D4" Ref="D13"  Part="1" 
AR Path="/5DCEE099/5DCE67D4" Ref="D19"  Part="1" 
AR Path="/5DD08BF1/5DCE67D4" Ref="D5"  Part="1" 
AR Path="/5DD09BFC/5DCE67D4" Ref="D9"  Part="1" 
AR Path="/5DD0ACE2/5DCE67D4" Ref="D13"  Part="1" 
AR Path="/5DD0BF7E/5DCE67D4" Ref="D17"  Part="1" 
AR Path="/5DD0D430/5DCE67D4" Ref="D21"  Part="1" 
F 0 "D1" V 2046 2532 50  0000 R CNN
F 1 "White" V 1955 2532 50  0000 R CNN
F 2 "Snowflake:0603_LED_HandSolder" V 2000 2600 50  0001 C CNN
F 3 "~" V 2000 2600 50  0001 C CNN
	1    2000 2600
	0    -1   -1   0   
$EndComp
$Comp
L Snowflake:R_Small R7
U 1 1 5DCE7281
P 2000 2900
AR Path="/5DCE640D/5DCE7281" Ref="R7"  Part="1" 
AR Path="/5DCECA79/5DCE7281" Ref="R13"  Part="1" 
AR Path="/5DCED58A/5DCE7281" Ref="R19"  Part="1" 
AR Path="/5DCEE099/5DCE7281" Ref="R25"  Part="1" 
AR Path="/5DD08BF1/5DCE7281" Ref="R11"  Part="1" 
AR Path="/5DD09BFC/5DCE7281" Ref="R15"  Part="1" 
AR Path="/5DD0ACE2/5DCE7281" Ref="R19"  Part="1" 
AR Path="/5DD0BF7E/5DCE7281" Ref="R23"  Part="1" 
AR Path="/5DD0D430/5DCE7281" Ref="R27"  Part="1" 
F 0 "R7" H 2059 2946 50  0000 L CNN
F 1 "XYZΩ" H 2059 2855 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 2000 2900 50  0001 C CNN
F 3 "~" H 2000 2900 50  0001 C CNN
	1    2000 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	2000 2700 2000 2800
Wire Wire Line
	2000 3000 2000 3100
$Comp
L Snowflake:LED_Small_ALT D2
U 1 1 5DCE9B66
P 2500 2600
AR Path="/5DCE640D/5DCE9B66" Ref="D2"  Part="1" 
AR Path="/5DCECA79/5DCE9B66" Ref="D8"  Part="1" 
AR Path="/5DCED58A/5DCE9B66" Ref="D14"  Part="1" 
AR Path="/5DCEE099/5DCE9B66" Ref="D20"  Part="1" 
AR Path="/5DD08BF1/5DCE9B66" Ref="D6"  Part="1" 
AR Path="/5DD09BFC/5DCE9B66" Ref="D10"  Part="1" 
AR Path="/5DD0ACE2/5DCE9B66" Ref="D14"  Part="1" 
AR Path="/5DD0BF7E/5DCE9B66" Ref="D18"  Part="1" 
AR Path="/5DD0D430/5DCE9B66" Ref="D22"  Part="1" 
F 0 "D2" V 2546 2532 50  0000 R CNN
F 1 "White" V 2455 2532 50  0000 R CNN
F 2 "Snowflake:0603_LED_HandSolder" V 2500 2600 50  0001 C CNN
F 3 "~" V 2500 2600 50  0001 C CNN
	1    2500 2600
	0    -1   -1   0   
$EndComp
$Comp
L Snowflake:R_Small R8
U 1 1 5DCE9B6C
P 2500 2900
AR Path="/5DCE640D/5DCE9B6C" Ref="R8"  Part="1" 
AR Path="/5DCECA79/5DCE9B6C" Ref="R14"  Part="1" 
AR Path="/5DCED58A/5DCE9B6C" Ref="R20"  Part="1" 
AR Path="/5DCEE099/5DCE9B6C" Ref="R26"  Part="1" 
AR Path="/5DD08BF1/5DCE9B6C" Ref="R12"  Part="1" 
AR Path="/5DD09BFC/5DCE9B6C" Ref="R16"  Part="1" 
AR Path="/5DD0ACE2/5DCE9B6C" Ref="R20"  Part="1" 
AR Path="/5DD0BF7E/5DCE9B6C" Ref="R24"  Part="1" 
AR Path="/5DD0D430/5DCE9B6C" Ref="R28"  Part="1" 
F 0 "R8" H 2559 2946 50  0000 L CNN
F 1 "XYZΩ" H 2559 2855 50  0000 L CNN
F 2 "Snowflake:0805-R_Handsolder" H 2500 2900 50  0001 C CNN
F 3 "~" H 2500 2900 50  0001 C CNN
	1    2500 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	2500 2700 2500 2800
Wire Wire Line
	2500 2500 2500 2200
Wire Wire Line
	2500 3000 2500 3100
Text HLabel 2000 2200 1    50   Input ~ 0
VLED0
Wire Wire Line
	2000 2200 2000 2500
Text HLabel 2500 2200 1    50   Input ~ 0
VLED1
Text HLabel 2000 3100 3    50   Input ~ 0
VK
Text HLabel 2500 3100 3    50   Input ~ 0
VK
$EndSCHEMATC
