def ConquestCampaign(N, M, L, battalion):
	days = 1
	list_1 = []
	list_2 = []
	fieldsList = [[0] * M for c in range(N)]

	for c in range(len(battalion)):
		if c % 2 == 0:
			list_1.append(battalion[c])
		if c % 2 != 0:
			list_2.append(battalion[c])
	print("list_1 = ", list_1)
	print("list_2 = ", list_2)

	for c in range(L):
		fieldsList[list_1[c]-1][list_2[c]-1] = 1
	print("fieldsList = ", fieldsList)
	print("fieldsList length = ", len(fieldsList))

	for i in range(N-1):
		for j in range(M-1):
			#print("i = ", i)
			#print("j = ", j)
			if fieldsList[i][j] == 1:
				if i == 0:
					break
				else:
					fieldsList[i-1][j] = 1

				if j == 0:
					break
				else:
					fieldsList[i][j-1] = 1
				if j == M - 1:
					break
				else:
					fieldsList[i][j+1] = 1

				if i == N - 1:
					break
				else:
					fieldsList[i+1][j] = 1
				print("fieldsList_next = ", fieldsList)
			days += 1
			print("days = ", days)
