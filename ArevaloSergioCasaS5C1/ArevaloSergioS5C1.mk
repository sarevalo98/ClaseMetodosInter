S5C1PLOT.pdf: plotsS5C1.py datosderiv.dat
	python plotsS5C1.py
datosderiv.dat: a.out
	./a.out>>datosderiv.dat
a.out: S5C1Deriv.cpp
	g++ S5C1Deriv.cpp 