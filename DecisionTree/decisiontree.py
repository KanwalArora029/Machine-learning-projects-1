from sklearn import tree


clf = tree.DecisionTreeClassifier()

#[height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

clf = clf.fit(X, Y)

# now we use our classifier to predict somevalue
print("Welcome to a simple Decision Tree Algorithm.".center(80, '*'))
print("Press Ctrl-C to exit".center(80))

while True:
    height = int(input("Enter the user's height in cms =  "))
    weight = int(input("Enter the user's weight in kgs =  "))
    shoesize = int(input("Enter the user's shoesize (say 43) =  "))
    print()
    print()

    prediction = clf.predict([[height, weight, shoesize]])
    gender = prediction[0]
    
    print("I think the gender of the user is = ", gender)
    print()
    
    print("*" * 80)
