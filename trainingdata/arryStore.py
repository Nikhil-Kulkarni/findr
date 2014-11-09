import sys, string, re
import numpy as np
import numpy
from sklearn import svm
from sklearn import datasets
import zmq

def main():
  file_list = []
  file_list1 = []
  file_listtest = []
  while True: #while loop that runs until the user puts in a file name...
    #or types in quit
    #asks the user for a file name, or gives them an option to quit
    file_name = "C:\HackNash\Tomo.txt"
    file_name1 = "C:\HackNash\Ecco.txt"
    file_name_Test = "C:\HackNash\Raja.txt"
    if file_name == "quit":
            sys.exit(0) #quits the program
    else:
            try: #attempts to open the file
                fin = open(file_name)
                fin1 = open(file_name1)
                fintest = open(file_name_Test)
                break
            except: #prints out if file name doesn't exist
                    print "No, no, file no here."
  for eachLine in fin: #strips out the new lines from the file
        file_list.append(eachLine.strip())
  for eachLine in fin1: #strips out the new lines from the file
        file_list1.append(eachLine.strip())
  for eachLine in fintest: #strips out the new lines from the file
        file_listtest.append(eachLine.strip())
  #print file_list
  #print file_list1
  #---x = [np.array(range(len(np.array(file_list)))), np.array(range(len(np.array(file_list1))))]
  #---y = np.array(["organiric", "vegetarian"]), np.array(["meat", "vegan"])
  maxsize = 0
  if(len(file_list) > len(file_list1)):
      maxsize = len(file_list)
  if(len(file_list) < len(file_list1)):
      maxsize = len(file_list1)
  file_list_hash = [0] * maxsize
  file_list_hash1 = [0] * maxsize
  file_list_testhash = [0] * maxsize
  tag = 0
  tag1 = 0
  tagtest = 0
  while(tag < len(file_list)) :
      file_list_hash[tag] = hash(file_list[tag])
      #file_list_hash.append(hash(file_list[tag]))
      tag = tag + 1
  while(tag1 < len(file_list1)) :
      file_list_hash1[tag1] = hash(file_list1[tag1])
      #file_list_hash1.append(hash(file_list1[tag1]))
      tag1 = tag1 + 1
  while(tagtest < len(file_listtest)) :
      file_list_testhash[tagtest] = hash(file_listtest[tagtest])
      #file_list_hash1.append(hash(file_list1[tag1]))
      tagtest = tagtest + 1      
  print file_list_hash
  print file_list_hash1
  print file_list_testhash
  x = [np.array(file_list_hash), np.array(file_list_hash1)]
  #y = [[hash("diabetic")],[hash("vegans")]]
  y = [1,2]
  iris = datasets.load_iris()
  #x = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
  #y = np.array([1, 5, 2, 6])
  clf = svm.SVC()
  #clf.fit(x,range(len(y)))
  clf.fit(x,y)
  print(clf.predict(np.array(file_list_testhash)))
  #labels = [y[i] for i in clf.predict(x)]
  #clf.fit(x, range(len(y)))
  context = zmq.Context()
  subscriber = context.socket(zmq.SUB)
  subscriber.bind("tcp://127.0.0.1:5000")
  subscriber.setsockopt(zmq.SUBSCRIBE, '')
  while True:
      print subscriber.recv()
  server = context.socket(zmq.REP)
  server.connect("tcp://127.0.0.1:5000")
  while True:
      message = server.recv()
      print "Sending", message, "World\n"
      server.send("Hello World")
  
if __name__ == '__main__':
    main()