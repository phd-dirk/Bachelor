set term post enhanced color "Helvetica" 22
set out "Y2V2O7_FM_bands.ps"
set size 1.1,1.0
set title "Y_2V_2O_7 (FM): Bandstructure without U"
set ylabel "energy [eV]"
set xtics ("L" 0, "{/Symbol G}" 0.28753, "W" 0.65874, "X" 0.82474)
set grid xtics front lt 1 lc 7 lw 2

set style line 1 lt 1 lc rgb "#e51836" lw 2 pt 0 ps 1           # rot
set style line 2 lt 1 lc rgb "#002a5c" lw 2 pt 0 ps 1           # dunkelblau
set style line 3 lt 1 lc rgb "#00aeef" lw 2 pt 0 ps 1           # hellblau
set style line 4 lt 1 lc rgb "#78288d" lw 2 pt 0 ps 1           # purple
set style line 5 lt 1 lc rgb "#7ac142" lw 2 pt 0 ps 1           # grün
set style line 6 lt 1 lc rgb "#ffc425" lw 2 pt 0 ps 1           # gelb
set style line 7 lt 1 lc rgb "#000000" lw 2 pt 7 ps 1           # schwarz

#set xrange [0:402]
set yrange [-2.75:1.5]

plot \
0 w l ls 7 notitle, \
'Y2V2O7.bandsup.agr' u 1:2 w l ls 2 notitle, \
'Y2V2O7.bandsdn.agr' u 1:2 w l ls 10 notitle
