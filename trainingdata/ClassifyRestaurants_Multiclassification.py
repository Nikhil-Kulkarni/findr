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

for index in range(0,len(restaurant_names)-1):
    print(restaurant_names[index])
    print(restaurant_categories[index])
    print(restaurant_categories2[index])
    

import numpy as np

#Creates menus to test on and classifies which category each belongs to
test_menu1 = "pizza"
test_menu2 = "cake"
test_menus = []
test_menus.append(test_menu1)
test_menus.append(test_menu2)

predicted_categories = text_clf.predict(test_menus)
print(predicted_categories)

'''
#Takes in customer information and predicts which restaurant he should go to
predicted_restaurants = []
predicted_restaurants_links = []

for predicted_category in predicted_categories:
    for i in range(0,len(restaurant_categories)-1):
        if ''.join(restaurant_categories[i]) == predicted_category:
            predicted_restaurants.append(restaurant_names[i])
            predicted_restaurants_links.append(restaurant_links[i])

print(predicted_restaurants)
print(predicted_restaurants_links)
'''
