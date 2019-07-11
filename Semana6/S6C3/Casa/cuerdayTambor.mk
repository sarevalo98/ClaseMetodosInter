FuncionSen.png: Plots_cuerdayTambor.py datos5.dat datos6.dat
	python Plots_cuerdayTambor.py
ExtremosFijos.png: Plots_cuerdayTambor.py datos.dat datos2.dat
	python Plots_cuerdayTambor.py
ExtremosFijoYsuelto.png:Plots_cuerdayTambor.py datos4.dat datos3.dat
	python Plots_cuerdayTambor.py
%.dat:a.out
	./a.out
a.out: ArevaloSergio_cuerdayTambor.cpp
	g++ ArevaloSergio_cuerdayTambor.cpp