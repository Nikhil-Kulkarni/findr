import sklearn
from sklearn import svm;
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier

one = "Ani beast"
two = "Saurabh salt"
three = "beast"
four = "salt"
five = "Saurabh"
six = "Ani"

data = [one, two, three, four, five, six]

cat1 = [0,3]
cat2 = [1,2]
cat3 = [0]
cat4 = [1]
cat5 = [2]
cat6 = [3]

categories = [cat1, cat2, cat3, cat4, cat5, cat6]

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                     ('tfidf', TfidfTransformer()),
                      ('clf', OneVsRestClassifier(MultinomialNB()))])

categories = MultiLabelBinarizer().fit_transform(categories)
print(categories)

                     
text_clf = text_clf.fit(data, categories)

new_data = ["Saurabh beast","salt"]
predicted_categories = text_clf.predict(new_data)
print(predicted_categories)
