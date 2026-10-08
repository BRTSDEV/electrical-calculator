# Electrical Calculator (Python)

A command-line calculator for common electrical formulas. I wrote it at school
(Elektrotechnische wetenschappen) to check my homework. The interface is in Dutch.

## Calculations
1. Ohm's law (U, I or R)
2. Electrical power P = U·I
3. Resistors in series
4. Resistors in parallel
5. Voltage divider
6. AC power P = U·I·cos φ
7. Energy stored in a capacitor E = ½·C·U²

## Run
    python calculator.py

Only needs Python 3.

## Note
The original file had lost its line breaks, so I re-formatted it (indentation
and blank lines only). The logic is unchanged.

## Known limitations / ideas
- No error handling yet: typing text instead of a number, or dividing by zero
  (e.g. R = 0), crashes the program
- Everything is in one `while` loop; each calculation could become a function
- More tools (e.g. oscilloscope: f = 1/T, Vpp = 2·Vp, Vrms = Vp/√2)
