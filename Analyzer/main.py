from Analyzer import Analyzer

dataIos = Analyzer('AppleStore.csv')
print(dataIos.dataset_header)
dataIos.explore_data(3,6,True)

print('\n')

dataAndroid = Analyzer('googleplaystore.csv')
print(dataAndroid.dataset_header)
dataAndroid.explore_data(3,6,True)

dataAndroid.explore_data(3,6,True)
dataAndroid.delete_row(10472)
dataAndroid.explore_data(3,6,True)

dataAndroid.show_duplicates()
dataAndroid.remove_duplicate()

print(dataAndroid.dataset_header)
dataAndroid.explore_data(3,6,True)

dataAndroid.clean_english(0)
dataIos.clean_english(1)

dataAndroid.explore_data(0, 3, True)
print('\n')
dataIos.explore_data(0, 3, True)

