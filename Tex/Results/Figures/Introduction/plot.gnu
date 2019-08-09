set term png truecolor
set output "grapheneManuscripts.png"
set xlabel "Year"
set ylabel "Number of manuscripts"
set grid
set boxwidth 0.80 relative
set style fill transparent solid 1  noborder
plot [2005:2013]  "graphenePublications.dat" u 1:2 w boxes lc rgb"black" notitle
