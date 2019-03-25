What is this?
------------------------------------
This is a simple python script to simulate a Galton board and generate a normal (Gaussian) distribution.
You can find more about the Galton board on [Wikipedia](https://en.wikipedia.org/wiki/Bean_machine) or by watching this excellent [Vsauce video](https://www.youtube.com/watch?v=UCmPmkHqHXk).

How does it work?
------------------------------------

There are two files: ```bellcurve.py``` and ```sd.py```. The first of the two is used to generate the data by simulating a ball dropped in a Galton board. The paramaters can be tweaked by changing the `TOTAL_BALLS` and `TOTAL_LINES` which change the amount of balls simulated respectively the amount of lines. The second script shows the probability to have `CONSECUTIVE_START` up to `MAX_CONS` balls go in the same direction (left or right) consecutively (example: right-right-right -> three times right).

Requirements
------------------------------------
You need ```matplotlib``` to visualize the data. If you do not wish to do so, feel free to remove the `plot` functions.

Examples
------------------------------------
<img src="/img/Figure_1.png" height="300"> <img src="/img/Figure_2.png" height="300">
