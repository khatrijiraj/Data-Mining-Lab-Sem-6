def check_species(dataset):
    n = dataset.shape[0]
    species = dataset["Species"][dataset["Species"] != 'NA']
    correct_n = species[species.isin(
        ["setosa", "versicolor", "virginica"])].shape[0]
    return n-correct_n, "Checking if all species consist of setosa, versicolor and virginica"


def check_positive(dataset):
    violation_n = 0
    for i in dataset.values:
        for j in i:
            if isinstance(j, float):
                if j < 0:
                    violation_n += 1
    return violation_n, "Checking if there all the length values are greater than 0"


def check_petal_length(dataset):
    n = dataset.shape[0]
    correct_n = 0
    for i in range(n):
        if dataset["Petal.Width"][i] == 'NA' or dataset["Petal.Length"][i] == 'NA':
            continue
        elif dataset["Petal.Width"][i]*2 > dataset["Petal.Length"][i]:
            continue
        else:
            correct_n += 1
    return n-correct_n, "Checking if petal length is at least twice of petal width"


def check_sepal_length(dataset):
    n = dataset.shape[0]
    sl = dataset["Sepal.Length"][dataset["Sepal.Length"] != 'NA']
    correct_n = sl[sl <= 30].shape[0]
    return n-correct_n, "Checking if all sepal lengths are below 30 cm"


def check_sepal_length2(dataset):
    n = dataset.shape[0]
    correct_n = 0
    for i in range(n):
        if dataset["Sepal.Length"][i] == 'NA' or dataset["Petal.Length"][i] == 'NA':
            continue
        elif dataset["Petal.Length"][i] >= dataset["Sepal.Length"][i]:
            continue
        else:
            correct_n += 1
    return n-correct_n, "Checking if sepal length is more than petal length"
