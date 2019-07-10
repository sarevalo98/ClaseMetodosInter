ArevaloSergioS6C2.pdf: Plots_cuerda.py datos.dat datos2.dat datos3.dat
	python Plots_cuerda.py
%.dat:a.out
	./a.out
a.out: ArevaloSergio_cuerda.cpp
	g++ ArevaloSergio_cuerda.cpp