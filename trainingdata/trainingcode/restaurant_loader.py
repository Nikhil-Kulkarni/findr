import os
import json
import io
"""
We load the text files containing each restaurant's menu information
"""
categories_path = 'C:/Users/Anirudh/Desktop/findr/trainingdata/RestaurantCategories.txt'
category_types_database = 'C:/Users/Anirudh/Desktop/findr/trainingdata/CategoryTypes.txt'

def get_restaurants():

    restaurants = []
    with open(categories_path, 'r') as filestream:
        lines = filestream.readlines()
        for eachline in lines:
            line = eachline.split()
            restaurant_file = line[0]
            restaurant_name = restaurant_file[:-4]
            #print(restaurant_name)
            categories = line[1].split(',')

            category_indices = []
            for category in categories:
                category_indices.append(get_category_index(category))

            categories = category_indices
            #print(categories)
            
            with open('C:/Users/Anirudh/Desktop/findr/trainingdata/'+restaurant_file, 'r') as sub_file:
                menu_file_lines = sub_file.readlines()
                link = menu_file_lines[0]
                
                menu_text = sub_file.read().replace('\n',' ')
                
                #for word in menu_text:
                #    word = hash(word)
                #print(menu_text)
                restaurants.append((restaurant_name, menu_text, categories, link))
    return restaurants

def get_category_index(category):
    with open(category_types_database, 'r') as filestream:
        category_index = 0
        lines = filestream.readlines()
        for i in range(0, len(lines)-1):
            lines[i] = lines[i][:-1]
        #print(lines)
        for index in range(0,len(lines)-1):
            if category == lines[index]:
                category_index = index     
    return category_index

def get_category_from_index(index):
    with open(category_types_database, 'r') as filestream:
        lines = filestream.readlines() 
    return lines[index]
