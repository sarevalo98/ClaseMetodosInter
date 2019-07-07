ArevaloSergioResorte.pdf: ArevaloSergio_S5C3_plots.py runge.dat
	python ArevaloSergio_S5C3_plots.py
runge.dat: a.out
	./a.out
a.out: ArevaloSergio_S5C3_ODEs.cpp
	g++ ArevaloSergio_S5C3_ODEs.cpp