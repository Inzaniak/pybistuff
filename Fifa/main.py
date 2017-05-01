from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

# Let's open the dataset
players = pd.read_csv("data/Fulldata.csv")
# Add a column that tells us if it's Training Data or not
players['is_train'] = np.random.uniform(0, 1, len(players)) <= .75

# Divide between training and testing data
train, test = players[players['is_train'] == True],players[players['is_train'] == False]

# We choose the columns with player stats
features = players.columns[17:53]
# Split into Training X(stats) and Y(rating) data
X = train[features]
Y = train.loc[:,'Rating']

# Initialize the Classifier and train it
clf = RandomForestClassifier(n_jobs=4)
clf.fit(X, Y)

# Get the predictions
preds = clf.predict(test[features])

# Create an output dataframe
out = test.loc[:,['Name','Rating']]
out['prediction'] = preds
out['diff']=out.loc[:,'Rating']-out.loc[:,'prediction']
# Let's print mean difference between predicted and actual
print('Mean difference: ',out['diff'].mean())
# And the number of exact matches
print('Exact Matches:',len(out[out['diff']==0]))

#Let's print the players with rating and prediction
print(out.loc[:,['Name','Rating','prediction','diff']])