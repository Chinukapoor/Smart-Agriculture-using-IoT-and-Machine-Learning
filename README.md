# Smart-Agriculture-using-IoT-and-Machine-Learning
The project uses Arduino UNO with multiple sensors attached to it like  Soil Moisture sensor, Photoelectric Diode Sensor,Humidity sensor etc that takes readings of the surrounding environment on a periodic basis.The mission of the project is to intimate the farmers or other stakeholders in predicting crop-failure. This is accomplished by a Machine Learning Layer that has been modeled to identify the degradation of a crop's health before its degradation starts. It uses KNN-algorithm to cluster the crops according to the impeding eventuality.The next iteration identifies the most probable cause and thorugha UI intimates the stakeholder what steps needs to be taken to prevent crop-failure.

The Arduino assembly line is arranged meticulously according to the circuit design. The whole process is divided into two pats:
1. Trainning Phase:
At first the sensing network circuit collects data from the environment and undergoes preprocessing. The Clean Data so obtained is fed onto the Machine Learning Classifier which is responsible to segregate the raw data and classify them into classes of Dry, Excess Heat, Healthy or Unfavorable. Now these serve as the basis for classifying unknown data in future.

2. Testing Phase: 
As the name suggests, this phase is responsible for testing unknown data gathered at real time using the machine learning classifier that is already implemented. The Classifier segregates the data by evaluating the parametric features and assigns it a class which may be Dry, Excess Heat, Healthy or Unfavorable. 

