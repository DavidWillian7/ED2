from csv import reader

class Analyzer:
  def __init__(self,arq):
    self.arq = arq
    self.opened_file = open(self.arq, encoding='utf-8')
    self.read_file = reader(self.opened_file)
    self.file = list(self.read_file)
    self.dataset_header = self.file[0]
    self.dataset = self.file[1:]

  def explore_data(self, start, end, rows_and_columns=False):
    dataset_slice = self.dataset[start:end]    
    for row in dataset_slice:
      print(row)
      print('\n') 

    if(rows_and_columns):
      print('Number of rows:', len(self.dataset))
      print('Number of columns:', len(self.dataset[0]))

  def delete_row(self, number_row):
    del self.dataset[number_row]
  
  def show_duplicates(self):
    duplicate_apps = []
    unique_apps = []

    for app in self.dataset:
      name = app[0]
      if(name in unique_apps):
        duplicate_apps.append(name)
      else:
        unique_apps.append(name)
    
    print('Number of duplicate apps:', len(duplicate_apps))
    print('\n')
    print('Examples of duplicate apps:', duplicate_apps[:15])
  
  def remove_duplicate(self):
    reviews_max = {}

    for app in self.dataset:
      name = app[0]
      n_reviews = float(app[3])
      if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
      elif(name not in reviews_max):
        reviews_max[name] = n_reviews

    dataset_clean = []
    already_added = []

    for app in self.dataset:
      name = app[0]
      n_reviews = float(app[3])
      if(reviews_max[name] == n_reviews) and (name not in already_added):
        dataset_clean.append(app)
        already_added.append(name)

    self.dataset = dataset_clean

  def is_english(self,string):
    non_ascii = 0
    for character in string:
      if ord(character) > 127:
        non_ascii += 1
    
    if non_ascii > 3:
      return False
    else:
      return True

  def clean_english(self, index):
    dataset_english = []

    for app in self.dataset:
      name = app[index]
      if self.is_english(name):
        dataset_english.append(app)
    
    self.dataset = dataset_english