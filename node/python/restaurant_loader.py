import os
import json
import io
"""
We load the text files containing each restaurant's menu information
"""
categories_path = 'RestaurantCategories.txt'
category_types_database = 'CategoryTypes.txt'

def get_restaurants():

    restaurants = []
    with open(categories_path, 'r') as filestream:
        lines = filestream.readlines()
        for eachline in lines:
            line = eachline.split("\t")
            restaurant_file = line[0]
            #print(restaurant_file)
            restaurant_name = restaurant_file[:-4]
            #print(restaurant_name)
            categories = line[1][:-1].split(',')
            #print(categories)

            category_indices = []
            for category in categories:
                #print(category)
                category_indices.append(get_category_index(category))

            categories = category_indices
            #print(categories)
            
            link = ''
            with open(restaurant_file, 'r') as sub_file:
                menu_file_lines = sub_file.readlines()
                link = menu_file_lines[0]
                #print(link) 
               
                
            with open(restaurant_file, 'r') as sub_file2:
                menu_text = sub_file2.read().replace('\n',' ')
                
                #print(menu_text)
                restaurants.append((restaurant_name, menu_text, categories, link))
    return restaurants

def get_category_index(category):
    with open(category_types_database, 'r') as filestream:
        category_index = 0
        lines = filestream.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i][:-1]
        #print(lines)
        for index in range(len(lines)):
            if category == lines[index]:
                category_index = index     
    return category_index

def get_category_from_index(index):
    with open(category_types_database, 'r') as filestream:
        lines = filestream.readlines() 
        return lines[index].rstrip()

restaurants = get_restaurants()
#index = get_category_index('Indian')
#print(index)
