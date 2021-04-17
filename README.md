# Numerical_transfer_function_approach
This repository show how to approach First-Order Linear Time Systems (LTI) with numerical techniques, additionally the algorithm proposes gains for a PID Controller.

# Pre-requisites
## Packages
- Matplotlib
- Numpy
- Sympy
- Scipy
- Pandas

## Control-Theory
First-Order Linear Time Systems (LTI) can be approximated to

![formula](https://render.githubusercontent.com/render/math?math=\hat{G}(s)=\frac{Ke^{-sL}}{sT%2B1})


L, K and T are paramters of the system and they are calculated as above

L = t2-T
T = (3/2)(t2-t1)

t1 and t2 are timestamp where y1 reaches 0.283K and y2 reaches 0.632K respectively

## PID Controller
Gains of the controller are approximated with the following table

|       |	 kp	 | 	ki	 | kd |
|  PID	| 1.2T/L | kp/(2L)	| 0.5kpL |

*The response with the controller applied is not implemented in this code yet*