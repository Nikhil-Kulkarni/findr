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
import numpy as np

arryCui = []
def format (cui):
    return np.array((cui.split(", ")))

        
    
    