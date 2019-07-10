ArevaloSergioS6C2.pdf: Plots_cuerdayTambor.py datos.dat datos3.dat
	python Plots_cuerdayTambor.py
%.dat:a.out
	./a.out
a.out: ArevaloSergio_cuerdayTambor.cpp
	g++ ArevaloSergio_cuerdayTambor.cpp