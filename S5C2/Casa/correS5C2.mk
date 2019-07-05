EulerS5C2PLOT.pdf: plotS5C2.py euler.dat
	python plotS5C2.py
RungeS5C2PLOT.pdf: plotS5C2.py runge.dat
	python plotS5C2.py
euler.dat: a.out
	./a.out
runge.dat: a.out
	./a.out
a.out: ArevaloSergioS5C2casa.cpp
	g++ ArevaloSergioS5C2casa.cpp
 