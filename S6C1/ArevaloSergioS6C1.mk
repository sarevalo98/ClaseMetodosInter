ArevaloSergio.pdf: ArevaloSergio_S6C1_plot.py datos.dat
	python ArevaloSergio_S6C1_plot.py
datos.dat: a.out
	./a.out
a.out: ArevaloSergio_S6C1.cpp
	g++ ArevaloSergio_S6C1.cpp