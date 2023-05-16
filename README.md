# Squishy Scale
 A versatile LCD upscaling program. Included is an NES Ninja Gaiden screenshot and it's upscaled version.
## Requirements
 Please install Python. This script also requires Pygame, but it will be automatically installed if it isn't already.
## How to use it:
 If you don't care about customization, just drag and drop your PNG files (and ONLY PNG files) into the "Input" folder. Then run the Python file and they'll be upscaled
## How does it work?
 For each pixel in the original image, the script makes a copy of "Pixel.png" and multiplies it by that pixels color. It then forms a grid with all of these pixels making a larger image. It does the same thing with "Glow.png" with an additive blend mode, thus producing a final image. Note that the size of the original image will be multiplied by the size of "Pixel.png", and each copy of "Glow.png" will be centered on the appropriate pixel.
## How can I customize it?
 Modify "Pixel.png" to be whatever a pixel on your chosen display looks like at the desired size, then create a larger image with "Pixel.png" in the center, draw whatever glow you think that pixel should make, and save it as "Glow.png". Leave this black if you'd like to have no glow.