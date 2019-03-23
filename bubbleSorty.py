def bubbleSort(data):
	for i in range(0, len(data) - 1, 1):
		for j in range(i + 1, len(data), 1):
			if(data[j] < data[i]:
			   temp = data[j]
			   data[j] = data[i]
			   data[i] = temp
	return data
