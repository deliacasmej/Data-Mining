

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
# Delia C

# iris data set from sklearn
iris = load_iris()
#pre-processing future X & y
data = iris.data
target = iris.target

# Splitting data into 50% seen, 50% unseen
split =int(len(data) * .5)

seen_data_set_X = data[:split]
unseen_data_set_X = data[split:]
seen_data_set_y = target[:split]
unseen_data_set_y = target[split:]

#using to test if I preprocessed my seen and unseen data correctly
#seen_data_set_X, unseen_data_set_X, seen_data_set_y, unseen_data_set_y = train_test_split(data,target, test_size=0.5, shuffle =False)

#renaming seen datasets for aesthetic purposes(unnecessary)
X = seen_data_set_X
y = seen_data_set_y

# using train_test_split methods to split 60/40
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1234)
# initializing k = 10
clf = KNeighborsClassifier(10)
#training KNN classifier
clf.fit(X_train, y_train)
#predicting on test set
pred = clf.predict(X_test)

print(pred)

#testing for accuracy
acc= clf.score(X_test,y_test)
print("Accuracy of K = 10 is : ", acc)

# Elbow plot for seen data

#var created to input into plot easier
k_val = range(3, 10)

acc_score = []

#loop for precision list 3-10
for i in k_val:
    knn = KNeighborsClassifier(i)
    knn.fit(X_train, y_train)
    prediction = knn.predict(X_test)

    #precision of seen data
    accuracy = knn.score(X_test, y_test)
    acc_score.append(accuracy)

plt.figure(figsize=(10,6))
plt.plot(k_val, acc_score, marker='o', linestyle="-")
plt.title('Precision for K=3-15 of Seen Data Set')
plt.xlabel('K Value')
plt.ylabel('Precision Score')
plt.xticks(k_val)

plt.show()

k_val = range(3, 10)

#Comparing seen to unseen
acc_score1 = []
acc_score2 = []
for i in k_val:
    knn = KNeighborsClassifier(i)
    knn.fit(X_train, y_train)
    prediction = knn.predict(X_test)

    #accuracy for seen data
    accuracy = knn.score(X_test, y_test)
    acc_score1.append(accuracy)

    #accuracy for unseen
    acc2 = knn.score(unseen_data_set_X,unseen_data_set_y)
    acc_score2.append(acc2)

plt.figure(figsize=(10,6))
plt.plot(k_val, acc_score, label= 'Seen Data', marker='o', linestyle="-")
plt.plot(k_val, acc_score2, label= 'Unseen Data', marker='o', linestyle="-")
plt.title('Comparing Seen To Unseen')
plt.xlabel('K Value')
plt.ylabel('Precision Score')
plt.xticks(k_val)

plt.show()
