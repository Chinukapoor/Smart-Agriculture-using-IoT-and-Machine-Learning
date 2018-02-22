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
class EnterInterface:
    def __init__(self, master):
        self.master = master
        master.title("Welcome to Farmer-Scientist Tool")

        self.label = Label(master, text="You are?")
        self.label.pack()

        self.greet_button = Button(master, text="Scientist", command=self.graph_menu)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Farmer", command=self.greet_1)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def graph_menu(self):
        menubar = Menu(root)
        menubar.add_command(label="Andrews Graph", command=self.display_andrews_graph)
        menubar.add_command(label="Quit!", command=root.quit)
        # display the menu
        root.config(menu=menubar)

    def display_andrews_graph(self):
        pdplt.andrews_curves(df, "output", ax=None)
        plt.show()

    def greet_1(self):
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
        # plt.figure()
        # plt.show()
        arduino_data = []
        # dt_test = pd.read_csv("test_this.csv", names=['humidity', 'temp', 'moisture', 'LDR']
        ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)

        def getValues():
            ser.write(b'g')
            arduino_data = ser.readline().decode('ascii')
            return arduino_data

        userInput = input("Get Test Data?")
        if userInput == 0:
            test_data = []
            test_data = getValues()
            myFile = open("test_data_1.csv", 'w+')
            myFile.write(test_data)
            myFile.close()
            print ("File Written")
            dt_test = pd.read_csv("test_data_1.csv", names=['humidity', 'temp', 'moisture', 'LDR'])
            final_data = dt_test.head(1)
            type = dt.predict(final_data)
            # print dt.predict(x_test)
        if type == '[0]':
            print 'dry'
        else:
            print 'Healthy'


#reading the training data and storing it in pandas dataframe
df = pd.read_csv("test_file1.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])

#print df['output'].unique()

#sns.pairplot(df, hue="output", size=2)
#plt.show()


root = Tk()
my_gui = EnterInterface(root)
root.mainloop()



'''
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
