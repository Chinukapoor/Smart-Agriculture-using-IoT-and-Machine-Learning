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
import Tkinter as Tk



class EnterInterface:
    def __init__(self, master):
        self.master = master
        master.title("Farmer-Scientist Tool")
        master.minsize(width=1000, height=550)

        f1 = Frame(master, height=100, width=175)
        f1.pack_propagate(0)  # don't shrink
        f1.pack()
        f1.place(x=200, y=60)

        self.greet_button = Button(f1, text="Scientist", command=self.graph_menu)
        self.greet_button.config(activebackground='Green', relief='raised')
        self.greet_button.pack(fill=BOTH, expand=1)

        f = Frame(master, height=100, width=175)
        f.pack_propagate(0)  # don't shrink
        f.pack()
        f.place(x=650, y=60)

        self.greet_button = Button(f, text="Farmer", command=self.greet_1)
        self.greet_button.config(activebackground='Green')
        self.greet_button.pack(fill=BOTH, expand=1)

        f3 = Frame(master, height=50, width=175)
        f3.pack_propagate(0)  # don't shrink
        f3.pack()
        f3.place(x=425, y=200)

        self.close_button = Button(f3, text="Close", command=master.quit)
        self.close_button.config(activebackground='Red')
        self.close_button.pack(fill=BOTH, expand=1)

    def graph_menu(self):
        menubar = Menu(root)
        menubar.add_command(label="Andrews Graph", activebackground='Light Green', command=self.display_andrews_graph)
        menubar.add_command(label="Regression Graph", activebackground='Light Green', command=self.regression_graph)
        menubar.add_command(label="Temperature Gradient", activebackground='Light Green', command=self.temp)
        menubar.add_command(label="Facegrid", activebackground='Light Green', command=self.face)
        menubar.add_command(label="Humidity Gradient", activebackground='Light Green', command=self.humidity)
        menubar.add_command(label="Quit", activebackground='Light Green', command=root.quit)
        # display the menu
        root.config(menu=menubar)

    def display_andrews_graph(self):
        pdplt.andrews_curves(df, "output", ax=None)
        plt.show()

    def regression_graph(self):
        df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])
        sns.jointplot("moisture", "humidity", df, kind='reg')

    def temp(self):
        df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])
        g = sns.FacetGrid(df, col="output")
        g.map(sns.distplot, "temp")
        plt.show()

    def humidity(self):
        df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])
        g = sns.FacetGrid(df, col="output")
        g.map(sns.distplot, "humidity")
        plt.show()

    def face(self):
        df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])
        g = sns.FacetGrid(df, col="output")
        g.map(sns.regplot, "humidity", "temp")
        plt.xlim(0, 100)
        plt.ylim(0, 35)
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
            print ("Result obtained\n")
            print ("Go to Interface to find solution")
            dt_test = pd.read_csv("test_data_1.csv", names=['humidity', 'temp', 'moisture', 'LDR'])
            final_data = dt_test.head(1)
            type = dt.predict(final_data)
            # print dt.predict(x_test)
            if type == '[0]':
                labelframe = LabelFrame(root, text="Problem-Solution Interface")
                labelframe.pack(fill="both")
                left = Label(labelframe, text="Dry \n 1. Check irrigation Methods \n 2. Urgent addition of water needed")
                left.pack()
            elif type == '[1]':
                labelframe = LabelFrame(root, text="Problem-Solution Interface")
                labelframe.pack(fill="both")
                left = Label(labelframe, text="Healthy \n The Plant looks fine, Be happy !")
                left.pack()
            else:
                labelframe = LabelFrame(root, text="Solution Interface")
                labelframe.pack(fill="both")
                left = Label(labelframe, text="Unfavourable\n 1. Excess Pesticides May be added \n 2. Add Ammonia if the problem persists")
                left.pack()


#reading the training data and storing it in pandas dataframe
df = pd.read_csv("test_file2.csv", names=['humidity', 'temp', 'moisture', 'LDR', 'output'])

# print df['output'].unique()

# sns.pairplot(df, hue="output", size=2)
# plt.show()


root = Tk.Tk()
background_image = Tk.PhotoImage(file="/home/kapoor1/Desktop/hello.png")
background_label = Tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
my_gui = EnterInterface(root)
# root["bg"] = 'white'
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
