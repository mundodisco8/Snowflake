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

## Outputs

The outputs of this project can be found in the Releases area.

## Documentation

### Design Intention

You can find the design document in the [docs section](docs/Design%20Justification.ipynb), as a Jupyter notebook, or [better rendered here](https://mundodisco8.github.io/Snowflake), as a static rendering of the jupyter notebooks. For an interactive session, you can launch it on Binder if you want to play with the sliders.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mundodisco8/Snowflake/JupyterToWebPage?labpath=docs%2FDesign_Justification.ipynb)

### Other bits and bobs

In the LTSpice folder you will find the circuits used on the Jupyter notebook to guess the current consumption as the battery discharges.

The `docs` folder also contains a couple of Excel spreadsheets I used to calculate some stuff, but they are not that interesting.

## Support Folder

The support folder contains random stuff that I needed at some point, mostly graphics.

I nicked the graphics from [here](https://svgsilh.com/image/2960229.html), which in turn is a variation of [this](https://pixabay.com/illustrations/snowflake-pattern-decor-decorative-2960229/).

## Running the CI/CD locally

The Release section only contains the artifacts of some hand-picked commits. Github Actions run on each commit on master, but the artifacts generated there have a self-life and get deleted after 15 days, I think. If you want, you can run the CICD pipeline locally.

```bash
# on the folder containing the project
# pull the KiBot image
docker pull ghcr.io/inti-cmnb/kicad7_auto_full:dev
# create a container named KiBotSnowDev, attaching the current folder as /Snowflake
docker run -it --name KiBotSnowDev -v .:/SnowFlake --entrypoint=/bin/bash ghcr.io/inti-cmnb/kicad7_auto_full:dev
# Now you are attached to the container
kibot -c ArtifactCreation.kibot.yaml -e hardware/Snowflake.kicad_sch -b hardware/Snowflake.kicad_pcb
```