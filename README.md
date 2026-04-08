# Floating Dandelion Art with Python Turtle

## Description

This project creates a simple and visually pleasing Python program that draws a sunny sky with floating dandelion seeds using the `turtle` graphics library. Each seed has a stem and radiating lines, giving the appearance of seeds drifting in the wind.

The program demonstrates basic concepts in Python graphics, including:

* Drawing shapes (circles and lines)
* Using functions to modularize code
* Randomization for natural-looking placement
* Simple geometric transformations

## Features

* A yellow sun with 12 radiating beams
* Multiple floating dandelion seeds with stems
* Randomized seed positions and stem angles for a natural effect
* Interactive window that closes on click

## Requirements

* Python 3.x
* `turtle` module (built-in)
* `random` module (built-in)
* `math` module (built-in)

> ⚠️ Note: The `panda` import is unused in this project and can be removed.

## How to Run

1. Clone or download this repository.
2. Open the project file `dandelion_art.py` in your Python IDE or text editor.
3. Run the program:

```bash
python dandelion_art.py
```

4. A window will open showing the sun and floating dandelion seeds.
5. Click anywhere in the window to close it.

## Code Overview

The project is structured around reusable functions:

* `draw_circle(t, x, y, radius, color)` – Draws a filled circle.
* `draw_sun_beams(t, x, y, color, outer_radius, beam_length)` – Draws beams around a circle (used for the sun and dandelion seeds).
* `draw_dandelion_seed(t, x, y, size, stem_angle)` – Draws a dandelion seed with a stem.

Random positions and angles make each execution slightly different, creating a whimsical effect.

## Screenshots

![Example Output](project1_drawing_dandelions_flying_under_sun.png)

## License

This project is open-source and free to use for educational purposes.
