ArevaloSergio.png: ArevaloSergio_S6C1_PlotCasa.py datos.dat datos2.dat
	python ArevaloSergio_S6C1_PlotCasa.py
datos.dat datos2.dat: a.out
	./a.out
a.out: ArevaloSergio_S6C1_Casa.cpp
	g++ ArevaloSergio_S6C1_Casa.cpp