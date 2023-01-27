# Demo population with filters

By following this build order, it's relatively easy to test the different modules in the circuit in isolation, minimising the risk of building the PCB. Obviously a scope and a multimeter will be handy, but the board can be effectively troubleshot with a throughole LED, so I recommend getting one from the spare parts box.

- [[front | ]] This is the front side of the board we are populating
- [[back | ]] This is the back side of the board we are populating
- [[back | _kf(clock)]] First, populate the clock generation, OpAmp, 10KΩ resistors, cap and pot.
- [[back | BT1, SW1]] Then add the switch and the battery, so the battery clip is not on the way when soldering the OpAmp.
- When the clock generation is placed, you can test it works properly. Connect the cathode of a diode to pin 1 of U1 and the anode to GND (for example, the "bottom" pad of R2). The LED must blink. Turning the potentiometer RV1 should change the blink period.
- [[back | Q1, R6, R11, R12]] Now let's move to the switching. Place the transistor Q1 and the current limiting resistors for the centre LED and one of the stems of the snowflake (R11, R12).
- [[front | D1, D6, D7]] Now place some LEDs to test the transistor is working. Seems obvious, but make sure you populate the LEDs corresponding to the current-limiting resistors you just placed! Before soldering D1, I recommend placing some Kapton tape around the pad, to protect the exposed art around it. Otherwise, unless you are incredibly skilled, you risk dropping a blob of solder around it, and it will look rather messy and ugly. The same can be said about the rest of the LEDs, but the risk is lower, and just by being careful, you can avoid messing it up!. Be careful, those LEDs are delicate!
- With this, you can either use a jumper cable to connect the output of the opamp (pin 1 in U1) to the gates of the transistors (pins 2 and 5 of Q1) and the "top" pad of R6. The LEDs should blink (the opamp should provide enough current for D1, don't worry). Alternatively, you can connect the gates or the top pad of R6 to VCC to switch them LEDs on.
- [[back | U2]] Place the binary counter. This is tricky, as it's easy to sort the pins, so make sure the chip is well aligned on the footprint, and add lots of flux.
- After this, you board is more or less fully functional. Switching it on should trigger the alternate blinking of the three LEDs already placed. If this doesn't work, then there must be a problem with your counter.
- [[back | _kf(currentResistors)]] Place the remaining current limiting resistors (nearly there)...
- [[front | _kf(LEDs)]] ... and the remaining current LEDs.

And here is the finished board

- [[back | ]] Back, fully assembled.
- [[front | ]] Front, ready to blink.
