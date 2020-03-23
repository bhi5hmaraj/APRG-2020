for i in 100 500 1000 2000 5000 7000 10000 50000 75000 100000
do
	python gen.py $i
	python anirudh.py < input.txt
done
