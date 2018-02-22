import time
import pandas.tools.plotting as pdplt
import matplotlib.pylab as plt
import seaborn as sns
import subprocess
import pandas as pd
import numpy as np
import serial
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from Tkinter import *
#import plotly.plotly as py

#reading the training data and storing it in pandas dataframe
df = pd.read_csv("test_file1.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])

print df['output'].unique()
sns.pairplot(df, hue="output", size=3)
plt.show()
pdplt.andrews_curves(df,"output",ax=None)
plt.show()

#modifying the dataframe, encoding the categorical variables to integers since the decision_tree classifier takes
#only integer inputs
def encode_target(df, target_column):
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)
    return df_mod, targets
df2, targets = encode_target(df, "output")

features = list(df2.columns[:4])
y = df2["Target"]
X = df2[features]
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
dt.fit(X, y)
#plt.figure()
#plt.show()
arduino_data = []
#dt_test = pd.read_csv("test_this.csv", names=['humidity', 'temp', 'moisture', 'LDR']
ser = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=1)
def getValues():
    ser.write(b'g')
    arduino_data = ser.readline().decode('ascii')
    return arduino_data

userInput = input("Get Test Data?")
if userInput == 0:
    test_data = []
    test_data = getValues()
    myFile = open("test_data_1.csv",'w+')
    myFile.write(test_data)
    myFile.close()
    print ("File Written")
    dt_test = pd.read_csv("test_data_1.csv", names=['humidity', 'temp', 'moisture', 'LDR'])
    final_data = dt_test.head(1)
    type = dt.predict(final_data)
    # print dt.predict(x_test)
    print type


root = Tk()
w = Label(root, text="Dry")
w.pack()
root.mainloop()

'''
type = dt.predict(arduino_data)
#print dt.predict(x_test)
if type==0:
    print "dry"
elif type==1:
    print "Healthy"

#test_features = []
#test_features = dt_test.head(1)
#x_test =['15','30','1000','99']
def visualize_tree(tree,feature_names):

    with open("dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f, feature_names=feature_names)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")

visualize_tree(dt, features)
'''
'''
data_clean = AH_data.dropna()
#data_clean.dtypes
#data_clean.describe()

predictors = [['Humidity','Temp','Moisture','LDR']]
targets = data_clean.output

pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)
'''
'''
classifier = DecisionTreeClassifier()
classifier = classifier.fit(pred_train,tar_train)

predictions = classifier.predict(pred_test)
print predictions

sklearn.metrics.accuracy_score(tar_test, predictions)
'''
