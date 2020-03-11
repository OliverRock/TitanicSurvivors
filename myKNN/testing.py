from _csv import reader
from math import sqrt

# Test distance function
dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
           [3.396561688, 4.400293529, 0],
           [1.38807019, 1.850220317, 0],
           [3.06407232, 3.005305973, 0],
           [7.627531214, 2.759262235, 1],
           [5.332441248, 2.088626775, 1],
           [6.922596716, 1.77106367, 1],
           [8.675418651, -0.242068655, 1],
           [7.673756466, 3.508563011, 1]]


def open_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


def euclidean_distance(point_a, point_b):
    distance = 0.0
    for i in range(len(point_a) - 1):
        distance += (point_a[i] - point_b[i]) ** 2
    return sqrt(distance)


def get_neighbours(train, test_row, num_neighbours):
    all_distances = list()
    for train_row in train:
        dist = euclidean_distance(test_row, train_row)
        all_distances.append((train_row, dist))
    all_distances.sort(key=lambda tup:tup[1])
    neighbours = list()
    for i in range(num_neighbours):
        neighbours.append(all_distances[i][0])
    return neighbours


def make_preditction(train, test_row, num_neighbours):
    neighbours = get_neighbours(train, test_row, num_neighbours)
    output_values = [row[-1] for row in neighbours]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


"""for i in range(len(dataset)):
    target = dataset[i]
    prediction = make_preditction(dataset, target, 3)
    print('Expected %d, Got %d.' % (target[-1], prediction))"""

data = open("iris_data.csv")
for x in data:
    print(x)
