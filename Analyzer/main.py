from Analyzer import Analyzer

dataIos = Analyzer('AppleStore.csv')
print(dataIos.dataset_header)
dataIos.explore_data(3,6,True)

print('\n')

dataAndroid = Analyzer('googleplaystore.csv')
print(dataAndroid.dataset_header)
dataAndroid.explore_data(3,6,True)

dataAndroid.explore_data(0,1,True)
dataAndroid.delete_row(10472)
dataAndroid.explore_data(0,1,True)

dataAndroid.show_duplicates()
dataAndroid.remove_duplicate()

print(dataAndroid.dataset_header)
dataAndroid.explore_data(0,1,True)

dataAndroid.clean_english(0)
dataIos.clean_english(1)

dataAndroid.explore_data(0, 1, True)
print('\n')
dataIos.explore_data(0, 1, True)

dataAndroid.free_apps(7)
dataIos.free_apps(4)
dataAndroid.explore_data(0, 1, True)
dataIos.explore_data(0, 1, True)

dataAndroid.display_table(1)
print("\n")
dataIos.display_table(-5)