from Analyzer import Analyzer

dataIos = Analyzer('AppleStore.csv')
print(dataIos.dataset_header)
dataIos.explore_data(3,6,True)

print('\n')

dataAndroid = Analyzer('googleplaystore.csv')
print(dataAndroid.dataset_header)
dataAndroid.explore_data(3,6,True)

dataAndroid.showDuplicates()
dataAndroid.removeDuplicate()

print(dataAndroid.dataset_header)
dataAndroid.explore_data(3,6,True)