# Mandelbrot Set

## This program computes mandelbrot set (a fractal) for a given set of co-ordinates.

## Pseudocode - Wikipedia
[Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set)

```python
for each pixel (Px, Py) on the screen do
    x0 := scaled x coordinate of pixel (scaled to lie in the Mandelbrot X scale (-2.5, 1))
    y0 := scaled y coordinate of pixel (scaled to lie in the Mandelbrot Y scale (-1, 1))
    x := 0.0
    y := 0.0
    iteration := 0
    max_iteration := 1000
    while (x*x + y*y ≤ 2*2 AND iteration < max_iteration) do
        xtemp := x*x - y*y + x0
        y := 2*x*y + y0
        x := xtemp
        iteration := iteration + 1
        
    color := palette[iteration]
    plot(Px, Py, color)
```
## How to
*  Get this repository
* Run the file **'mandelbrot_gpu.py'** in your favourite python environment
* If you dont have a GPU, comment out **'@jit(mopython=Ture)'** in the code
* The default cooridonates are **(xmin=-2.5, xmax=1.0, ymin=-1.0,ymax=1.0)**
* Change these coordinates to any interesting location and compute.

## Images 
<img width="600px" height="400px" src="/mandelbrot.png">
<img width="600px" height="400px" src="/coastline_ocean.png">
<img width="600px" height="400px" src="/snowflake.png">
<img width="600px" height="400px" src="/near_fibonacci5.png">
<img width="600px" height="400px" src="/galaxy_spiral.png">
