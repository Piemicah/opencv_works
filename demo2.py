from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

print(digits.data)
print(digits.target)
print(digits.images[0])
