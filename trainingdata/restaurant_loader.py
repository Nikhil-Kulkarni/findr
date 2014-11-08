import os
import json
import io
"""
We load the text files containing each restaurant's menu information
"""
categories_path = 'C:/Users/Anirudh/Desktop/findr/trainingdata/RestaurantCategories.txt'

def get_restaurants():

    restaurants = []
    with open(categories_path, 'r') as filestream:
        lines = filestream.readlines()
        for eachline in lines:
            line = eachline.split()
            restaurant_file = line[0]
            restaurant_name = restaurant_file[:-4]
            print(restaurant_name)
            categories = line[1].split(',')
            print(categories)
            with open('C:/Users/Anirudh/Desktop/findr/trainingdata/'+restaurant_file, 'r') as sub_file:
                #menu_text = json.load(io.StringIO(sub_file.read()))
                menu_text = sub_file.read().replace('\n',' ')
                #print(menu_text)
                restaurants.append((restaurant_name, menu_text, categories))

    return restaurants


articles = get_restaurants()
#print(articles[10][0]['text'])
#raw_input('Press enter to exit...')
