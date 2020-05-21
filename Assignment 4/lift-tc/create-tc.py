fin = open('raw_3.txt', 'r')
lines = fin.readlines()
ptr = 0
start = 133
while ptr < len(lines):
	# print(lines[ptr].split())

	n, k = map(int, lines[ptr].split())
	fout = open('input\\input%02d.txt' % start, 'w')
	print(lines[ptr].strip(), file=fout)
	ptr += 1
	print(lines[ptr].strip(), file=fout)
	ptr += 1
	print(''.join(lines[ptr :ptr + n ]), file=fout)
	fout.close()
	ptr += n
	start += 1

