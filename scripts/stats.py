from bs4 import BeautifulSoup

print('opening file')
# Reading the data inside the xml
# file to a variable under the name 
# data
# with open('D:\healthdata/apple_health_export/export_cda.xml', 'r') as f:
#     data = f.read()

with open('D:\healthdata/test_data/export_test.xml') as f:
    data = f.read()

print('adding file to BeatifulSoup')
# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object 
health_data = BeautifulSoup(data, "xml")

print('searching for title')
export_date = health_data.find('ExportDate')
print(export_date['value'])

# Finding all instances of tag 
# `unique`
# all_texts = Bs_data.find_all('text')

## Types: HKQuantityTypeIdentifierBodyMassIndex, 

# print(b_unique)

# Using find() to extract attributes 
# of the first instance of the tag
# b_name = Bs_data.find('child', {'name':'Frank'})

# print(b_name)

# Extracting the data stored in a
# specific attribute of the 
# `child` tag
# value = b_name.get('test')

# print(value)