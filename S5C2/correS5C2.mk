GraficaS5C2PLOT.png: plotS5C2.py datos.dat
	python plotS5C2.py
datos.dat: a.out
	./a.out>>datos.dat
a.out: ArevaloSergioS5C2.cpp
	g++ ArevaloSergioS5C2.cpp 