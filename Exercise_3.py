def ConquestCampaign(N, M, L, battalion):
	days = 1
	count = 0
	list_1 = []
	list_2 = []
	run = True
	fieldsList = [[0] * M for c in range(N)]
	fieldsList_ = [[0] * M for c in range(N)]

	for c in range(len(battalion)):
		if c % 2 == 0:
			list_1.append(battalion[c])
		if c % 2 != 0:
			list_2.append(battalion[c])

	for c in range(L):
		fieldsList[list_1[c]-1][list_2[c]-1] = 1

	for i in range(N):
		for j in range(M):
			if fieldsList[i][j] < 1:
				count += 1

	while count > 0:
		for i in range(N):
			for j in range(M):
				if fieldsList[i][j] == 1:
					fieldsList[i][j] += 1
		for i in range(N):
			for j in range(M):
				if fieldsList[i][j] >= 2:
					if i-1 >= 0:
						fieldsList[i-1][j] += 1

					if i+1 <= N-1:
						fieldsList[i+1][j] += 1

					if j-1 >= 0:
						fieldsList[i][j-1] += 1

					if j+1 <= M-1:
						fieldsList[i][j+1] += 1
		days += 1
		count = 0
		for i in range(N):
			for j in range(M):
				if fieldsList[i][j] < 1:
					count += 1
	return days
