import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def  		ft_revert_data(arr):
	res = {}
	i = 0

	while (i <= len(arr)):
		consumer_id = arr[i][0]
		res[consumer_id] = []
		#print(consumer_id, arr[i][0])
		#print("Array length: {}".format(len(arr)))
		if (i < len(arr) and arr[i][0] == consumer_id):
			while arr[i][0] == consumer_id:
				#print("Current i value before: {}".format(i))
				res[consumer_id].append(arr[i][2:])
				#print(res[consumer_id][:4])
				if (i < len(arr) - 1):
					i += 1
				else:
					break
				#print("Current i value after: {}".format(i))
		if (i == len(arr) - 1):
			break
		elif (i < len(arr)):
			i += 1
	return (res)

def check_consumer_amount(arr, consumers):
	i = 0
	valid_arr = {}
	# print("HERE!")
	for key in arr:
		j = 0
		valid_arr[key] = []
		# print(len(consumers['target']))
		while (j < len(consumers['target'])):
		#	print("OLA!")
			if (key == consumers['target'][j][0]):
				valid_arr[key] = arr[key]
				i += 1
			j += 1
	# print(i)
	return (valid_arr)


def  	extract_values_from_dict(arr):
	new_arr = []
	for key in arr:
		new_arr.append(arr[key])
	return (np.array(new_arr))

def  	get_mean_values(arr, consumers):
	mean_arr = {}

	arr = check_consumer_amount(arr, consumers)
	for key in arr:
		i = 0
		mean_arr[key] = []
		while (i < 42):
			value = 0.0
			j = 0
			while (j < len(arr[key])):
				num = arr[key][j][i]
				value += num
				j += 1
			mean_arr[key].append(value / j)
			i += 1
	mean_arr = extract_values_from_dict(mean_arr)
	return (mean_arr)

def  cast_dict_to_float(arr, consumers):
	i = 0
	new_data = {}
	for key in arr:
		int_key = int(key)
		new_data[int_key] = []
		i = 0
		while (i < len(arr[key])):
			new_data[int_key].append(arr[key][i])
			j = 0
			while (j < len(new_data[int_key][i])):
				if (new_data[int_key][i][j] == ""):
					new_data[int_key][i][j] = 0
				new_data[int_key][i][j] = float(new_data[int_key][i][j])
				j += 1
			i += 1

	return (get_mean_values(new_data, consumers))

def 	cast_ndarr(arr, flag):
	i = 0

	while i < len(arr):
		j = 0
		while j < len(arr[i]):
			if (arr[i][j] == ""):
				arr[i][j] = 0
			if (flag):
				arr[i][j] = float(arr[i][j])
			else:
				arr[i][j] = int(arr[i][j])
			j += 1
		i += 1
	return (np.array(arr))


def 	parse_data_file(consumers):
	data_fd = open('Base1.txt', 'r')
	data = []
	for line in data_fd:
		data.append(line);
	data_fd.close();
	
	i = 0
	data = data[1:]

	while i < len(data):
		data[i] = data[i].split('\t')
		data[i][-1] = data[i][-1][:-1]
		i += 1

	data = ft_revert_data(data)
	data = cast_dict_to_float(data, consumers)
	# print(data[:2])
	# [print("\n\n\n\n.{}".format(item)) for item in data]
	return (data)

def 	parse_labels_file():
	data_fd = open('train.txt', 'r')
	labels = []
	for line in data_fd:
		labels.append(line);
	data_fd.close();
	i = 0
	labels = labels[1:]

	while i < len(labels):
		labels[i] = labels[i].split('\t')
		labels[i][-1] = labels[i][-1][:-1]
		i += 1
	return (cast_ndarr(labels, 0))
	

def main():
	consumers = {}
	consumers['target'] = parse_labels_file()
	consumers['data'] = parse_data_file(consumers)
	# check_consumer_amount(consumers)
	print(consumers['data'].shape)
	print(consumers['target'].shape)
	X_train, X_test, y_train, y_test = train_test_split(consumers['data'], consumers['target'], random_state=0)
	#print(X_test.shape)
	#print(consumers['data'].shape)
	#print(consumers)

if __name__ == '__main__':
	main()