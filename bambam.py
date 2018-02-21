from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = clf.fit(X, Y)

p1 = raw_input('Enter Height')
p2 = raw_input('Enter Weight')
p3 = raw_input('Enter Shoe Size')

mode = raw_input("Train or Test")
if(mode == "Train"):
     x1 = [p1,p2,p3]
     predict = clf.predict(p1, p2, p3)
     av = raw_input('Enter Actual Value: ')
     if (predict == av):
          print "Correct"
     else:
          print "Wrong"
     X.append(x1)
     Y.append(av)
else:
     print clf.predict(p1,p2,p3)

clf = clf.fit(X,Y)  





