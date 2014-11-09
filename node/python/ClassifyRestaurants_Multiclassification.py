import sklearn
from sklearn import svm;
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MultiLabelBinarizer
from restaurant_loader import get_restaurants
from restaurant_loader import get_category_from_index
from sklearn.multiclass import OneVsRestClassifier


restaurant_array = get_restaurants()
restaurant_names = [restaurant[0] for restaurant in restaurant_array]
restaurant_menus = [restaurant[1] for restaurant in restaurant_array]
restaurant_categories = [restaurant[2] for restaurant in restaurant_array]
restaurant_links = [restaurant[3] for restaurant in restaurant_array]

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                     ('tfidf', TfidfTransformer()),
                     ('clf', OneVsRestClassifier(MultinomialNB()))])

#make sure each category shows up at least once in training set
restaurant_categories2 = MultiLabelBinarizer().fit_transform(restaurant_categories)

text_clf = text_clf.fit(restaurant_menus, restaurant_categories2)

'''
for index in range(len(restaurant_names)):
    print(restaurant_names[index])
    print(restaurant_categories[index])
    print(restaurant_categories2[index])
'''
    

import numpy as np

'''
#Creates menus to test on and classifies which category each belongs to
test_menu1 = "Indian"
test_menu2 = ""
test_menus = []
test_menus.append(test_menu1)
test_menus.append(test_menu2)

predicted_categories = text_clf.predict(test_menus)
print(predicted_categories)
'''
'''
def __init__(location, cuisine, restriction):
    location = 'Atlanta'
    cuisine = 'Indian'
    restriction = 'diabetic'
    getInfo(location, cuisine, restriction)
'''

#Takes in customer information and predicts which restaurant he should go to
recommended_restaurants = []
recommended_restaurants_links = []
#category_list = ['Vegetarian', 'organic']

#THIS IS THE FUNCTION THAT YOU NEED TO USE
def format (cui):
    return (cui.split(", "))


def getInfo(location, cuisine, allergic_info):
    cuisineArr  = format(cuisine)
    allergic_infoArr = format(allergic_info)
    restaurant_array = get_restaurants()
    restaurant_names = [restaurant[0] for restaurant in restaurant_array]
    restaurant_menus = [restaurant[1] for restaurant in restaurant_array]
    restaurant_categories = [restaurant[2] for restaurant in restaurant_array]
    restaurant_links = [restaurant[3][3:].rstrip() for restaurant in restaurant_array]
    
    count_array = []
    category_list = cuisineArr + allergic_infoArr
    
    for category in restaurant_categories:
        #print(category)
        for index in range(len(category)):
            category_name = get_category_from_index(category[index])
            category[index] = category_name
        #print(category)

    for i in range(len(restaurant_categories)):
        count = 0
        for each_category in restaurant_categories[i]:
            for category in category_list:
                if  each_category == category:
                    count = count + 1
        count_array.append(count)

    max_indices = []
    maxCount = 0
    max_index = 0
    for index in range(len(count_array)):
        frickingstupid = int(count_array[index])
        if (frickingstupid > maxCount):
            maxCount = frickingstupid
            max_index = index

    return [restaurant_names[max_index],restaurant_links[max_index]]
    #print(restaurant_names[max_index])
    #print(restaurant_links[max_index])

with open(r'C:\Users\IMSA Student\Desktop\findr\node\myOutput.txt', 'r') as input_file:
        read_text = input_file.read().split(';')
        read_text[0] = read_text[0].replace('\n','')
        read_text[1] = read_text[1].replace('\n','')
        read_text[2] = read_text[2].replace('\n','')
        print(getInfo(read_text[0], read_text[1], read_text[2])[0])
        print(getInfo(read_text[0], read_text[1], read_text[2])[1])
    
#print(getInfo('Atlanta',"Indian", "Vegetarian"))
#print(recommended_restaurants)
#print(recommended_restaurants_links)


