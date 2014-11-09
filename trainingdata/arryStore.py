import sys, string, re
import numpy as np
from sklearn import svm
from sklearn import datasets

def main():
  file_list = []
  file_list1 = []
  while True: #while loop that runs until the user puts in a file name...
    #or types in quit
    #asks the user for a file name, or gives them an option to quit
    file_name = "C:\HackNash\Tomo.txt"
    file_name1 = "C:\HackNash\Leawood.txt"
    if file_name == "quit":
            sys.exit(0) #quits the program
    else:
            try: #attempts to open the file
                fin = open(file_name)
                fin1 = open(file_name1)
                break
            except: #prints out if file name doesn't exist
                    print "No, no, file no here."

  for eachLine in fin: #strips out the new lines from the file
        file_list.append(eachLine.strip())
  for eachLine in fin1: #strips out the new lines from the file
        file_list1.append(eachLine.strip())
  print file_list
  print file_list1
  #---x = [np.array(range(len(np.array(file_list)))), np.array(range(len(np.array(file_list1))))]
  #---y = np.array(["organiric", "vegetarian"]), np.array(["meat", "vegan"])
  #x = [file_list, file_list1]
  #y = ["organic", "vegan"]
  iris = datasets.load_iris()
  x = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
  y = np.array([1, 1, 2, 6])
  clf = svm.SVC()
  #clf.fit(x,range(len(y)))
  clf.fit(x,y)
  print(clf.predict([[2, 1]]))
  #labels = [y[i] for i in clf.predict(x)]
  #clf.fit(x, range(len(y)))
  
if __name__ == '__main__':
    main()
