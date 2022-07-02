import pandas as pd
import numpy as np
from functools import reduce

#1. Adding Csv table into python
dt=pd.read_csv(data_path)
dc.head()

#2. Dropping Unnecessary Columns
to_drop=[column_name]
dt.drop(to_drop, inplace=true, axis=1)  #or: dt.drop(columns=to_drop, inplace =True)

#3.Changing the index
dt = dt.set_index('Identifier') #or: dt.set_index('Identifier', inplace = True)
dt.head()

#4. Cleaning specific columns (unwanted characters)
unwanted_characters = ['[', ',', '-']
def clean_dates(item):
    dop= str(item.loc['Date of Publication'])
    
    if dop == 'nan' or dop[0] == '[':
        return np.NaN
    
    for character in unwanted_characters:
        if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]
    
    return dop

dt['Date of Publication'] = dt.apply(clean_dates, axis = 1)
dt.head()


#alternate way of cleaning Date of Publication
#run cell to see output
unwanted_characters = ['[', ',', '-']

def clean_dates(dop):
    dop = str(dop)
    if dop.startswith('[') or dop == 'nan':
        return 'NaN'
    for character in unwanted_characters:
        if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]
    return dop

dt['Date of Publication'] = dt['Date of Publication'].apply(clean_dates)
dt.head()


#5. Cleaning Author Names from columns
def clean_author_names(item):
    
    author = str(item.loc['Author'])
    
    if author == 'nan':
        return np.NaN
    
    author = author.split(',')

    if len(author) == 1:
        name = filter(lambda x: x.isalpha(), author[0])
        return reduce(lambda x, y: x + y, name)
    
    last_name, first_name = author[0], author[1]

    first_name = first_name[:first_name.find('-')] if '-' in first_name else first_name
    
    if first_name.endswith(('.', '.|')):
        parts = first_name.split('.')
        
        if len(parts) > 1:
            first_occurence = first_name.find('.')
            final_occurence = first_name.find('.', first_occurence + 1)
            first_name = first_name[:final_occurence]
        else:
            first_name = first_name[:first_name.find('.')]
    
    last_name = last_name.capitalize()
    
    return f'{first_name} {last_name}'


dt['Author'] = dt.apply(clean_author_names, axis = 1)
dt.head()

#6. Cleaning Place of Publication
pub = df['Place of Publication']
dt['Place of Publication'] = np.where(pub.str.contains('London'), 'London',
    np.where(pub.str.contains('Oxford'), 'Oxford',
        np.where(pub.eq('Newcastle upon Tyne'),
            'Newcastle-upon-Tyne', dt['Place of Publication'])))
dt.head()

#7. Cleaning Title
def clean_title(item):
    title = str(item['Title'])
    
    if title == 'nan':
        return np.NaN
    
    if title[0] == '[':
        title = title[1: title.find(']')]
        
    if 'by' in title:
        title = title[:title.find('by')]
    elif 'By' in title:
        title = title[:title.find('By')]
        
    if '[' in title:
        title = title[:title.find('[')]

    title = title[:-2]
        
    title = list(map(str.capitalize, title.split()))
    return ' '.join(title)
    
dt['Title'] = dt.apply(clean_title, axis = 1)
dt.head()

#8. Cleaning Entire dataset Text dataset
university_towns = []

with open('university_towns.txt' file path, 'r') as file:
    items = file.readlines()
    states = list(filter(lambda x: '[edit]' in x, items))
    
    for index, state in enumerate(states):
        start = items.index(state) + 1
        if index == 49: #since 50 states
            end = len(items)
        else:
            end = items.index(states[index + 1])
            
        pairs = map(lambda x: [state, x], items[start:end])
        university_towns.extend(pairs)
        
towns_dt = pd.DataFrame(university_towns, columns = ['State', 'RegionName'])
towns_dt.head()

###cleaning
def clean_up(item):
    if '(' in item:
        return item[:item.find('(') - 1] #since space before '('
    
    if '[' in item:
        return item[:item.find('[')]
    

towns_df =  towns_df.applymap(clean_up)
towns_df.head()


#9. Renaming columns and skipping rows

##Adding Data to python
olympics_dt = pd.read_csv('olympics.csv', skiprows=1, header=0)
olympics_dt.head()

##Renaming
new_names = {'Unnamed: 0': 'Country',
           '? Summer': 'Summer Olympics',
           '01 !': 'Gold',
           '02 !': 'Silver',
           '03 !': 'Bronze',
           '? Winter': 'Winter Olympics',
           '01 !.1': 'Gold.1',
           '02 !.1': 'Silver.1',
           '03 !.1': 'Bronze.1',
           '? Games': '# Games', 
           '01 !.2': 'Gold.2',
           '02 !.2': 'Silver.2',
           '03 !.2': 'Bronze.2'}

olympics_dt.rename(columns=new_names, inplace=1)
olympics_dt.head()

