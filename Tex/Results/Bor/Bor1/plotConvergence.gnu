set term post enhanced color "Helvetica" 22
set out "bor1Convergence.ps"
set title "Convergence of C_{1-x}B_{x}, x=1/2"
set ylabel "Total energy (Ha)"
set xlabel "k-point density (x - x - 4)" 
unset key
set terminal postscript eps

set style line 1 lt 1 lc rgb "#e51836" lw 2 pt 0 ps 1           # rot
set style line 2 lt 1 lc rgb "#002a5c" lw 2 pt 0 ps 1           # dunkelblau
set style line 3 lt 1 lc rgb "#00aeef" lw 2 pt 0 ps 1           # hellblau
set style line 4 lt 1 lc rgb "#78288d" lw 2 pt 0 ps 1           # purple
set style line 5 lt 1 lc rgb "#7ac142" lw 2 pt 0 ps 1           # grün
set style line 6 lt 1 lc rgb "#ffc425" lw 2 pt 0 ps 1           # gelb
set style line 7 lt 1 lc rgb "#000000" lw 2 pt 7 ps 1           # schwarz

plot 'bor1Convergence.dat' u 1:2 w l 
