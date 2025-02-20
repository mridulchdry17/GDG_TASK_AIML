def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	trans = []

	for i in range(len(a[0])):
		new_row = []
		for j in range(len(a)):
			new_row.append(a[j][i])
		trans.append(new_row)
		
	return trans