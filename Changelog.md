# CHANGELOG

## v2.0.0-RC1

General improvements after building the first batch. The main change is the replacement of the decade counter package with a SOIC-16 from a TSSOP-16. It's a bit uglier, but it's easier to solder and it was the main source of issues on the first batch.

### Added

- Fancy CI/CD with KiBot
- Published the documentation as a webpage.

### Changed

- Changed the decade counter package to SOIC-16. I ordered them by mistake and while they are chunky, the previous one (TSSOP-16) was a source of issues while soldering without magnification (these poor eyes...).
- Rotated the Battery holder so replacing the battery is a bit easier. It also avoids the battery hitting one of the current limiter resistors and knocking it out
- F.Fab is a tad neater.
- Added test points to help during assembly.
- Extended some footprints to help with hand assembly.

## v1.0.0

### Added

- First Release.
