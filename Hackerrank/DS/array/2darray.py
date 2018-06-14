mat = []
for i in range(6):
	mat.append(map(int, raw_input().split()))
maxm = -1000000
for i in range(4):
	for j in range(4):
		hr = 0
		for k in range(i, i+3):
			for l in range(j, j+3):
				if k==i+1:
					if l != j+1:
						pass
					else:
						hr += mat[k][l]
				else:
					hr += mat[k][l]
		if hr > maxm:
			maxm = hr
		# hr = mat[i][j] + mat[i][j+1] + mat[i][j+2]
		# hr += mat[i+1][j+1]
		# hr += mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
		# if hr > maxm:
		# 	maxm = hr

print maxm