View this project on [CADLAB.io](https://cadlab.io/project/26393).

# Snowflake

A Snowflake Christmas decoration.
<p align="middle">
  <img src="/support/img/Snowflake-3D_blenderTopSlanted.png" width="40%" />
  <img src="/support/img/Snowflake-3D_blenderTop.png" width="40%" />
</p>

<p align="middle">
  <img src="/support/img/Snowflake-3D_blenderBottomSlanted.png" width="40%" />
  <img src="/support/img/Snowflake-3D_blenderBottom.png" width="40%" />
</p>

Just a design exercise, aiming to get a hand-solderable board (although a bit challenging) that blinks its LEDs without using a microcontoller. I guess you can call it a mix of digital and analogue electronics, because the main trigger is a binary counter that is fed by a clock generated with an opamp in astable multivibrator config.

## Documentation

You can find the [design document](docs/Design%20Justification.ipynb) in the docs section, as a Jupyter notebook.

The documentation can be [explored here](https://mundodisco8.github.io/Snowflake), as a static rendering of the jupyter notebooks, or in binder if you want to play with the sliders.

In the LTSpice folder you will find the circuits used on the Jupyter notebook to guess the current consumption as the battery discharges.

The `docs` folder also contains a couple of Excel spreadsheets I used to calculate some stuff, but they are not that interesting.

## Support Folder

The support folder contains random stuff that I needed at some point, mostly graphics.

I nicked the graphics from [here](https://svgsilh.com/image/2960229.html), which in turn is a variation of [this](https://pixabay.com/illustrations/snowflake-pattern-decor-decorative-2960229/).
