#
# # Standardize data (0 mean, 1 stdev)
# from sklearn.preprocessing import StandardScaler
#
# import pandas
# import numpy
# url = "https://goo.gl/vhm1eU"
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# dataframe = pandas.read_csv(url, names=names)
# array = dataframe.values
# # separate array into input and output components
# X = array[:,0:8]
# Y = array[:,8]
# scaler = StandardScaler().fit(X)
# rescaledX = scaler.transform(X)
# # summarize transformed data
# numpy.set_printoptions(precision=3)
# print(rescaledX[0:5,:])

if __name__ == '__main__':
    n = int(input())

for i in range(1,n+1):
    print(str(i),end='')
