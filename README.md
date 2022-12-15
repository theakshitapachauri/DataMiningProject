# DataMiningProject

Author : Akshita Pachauri
ID : 01978422
Email : akshita_pachauri@student.uml.edu

Project Description:

***************************************************************************************************************

Data_Preprocessing1.ipynb : It is the .ipynb file which includes the implementation of the data preprocessing, including :

- Conversion of the original dataset to a format that fits our NN’s input form. 

- Handling all '?' or NaN values by replacing them based upon the percentage of existing categorical values, grouped by classes column. 

- Transforming original dataset’s records into into a set of binary variables.

- Spliting the converted dataset into 3 files: training.txt for network training, val.txt for validation, and testing.txt for network testing (80:20:20).


***************************************************************************************************************

The implementation of 3 files: 

- formulas.py : Implemented the logistic funtion as the activation function, derivative of logistic function, squared error function and derivative of the squared error fucntion. 

- models.py: Implemented Evaluation and backpropagation and 

- proj_test.py : Implementation and evaluation of first layer, second layer and error part of all training, validation testing part.  

-- Since the above provided code files had the python support of python2, I have made following changes in order to convert it to python3:
1) In file model.py : file() method is replaced with open() since file() was only available in python2. 
2) In proj_text.py : changed raw_input() to input(), because in python3, raw_input() has been replaced with input() method.

************************************************************************************************************

-- To run the Data_Preprocessing1.ipynb you can simply say run all, at the top, or you can run individual cells, and it will create the training.txt, val.txt and testing.txt files.

To run the project : python proj_test.py

This will calculate the training error and will create a training_err.txt

You would be required to press enter to start the validation process. This will result in validation error and will create a val_err.txt

You would be required to press enter to start the testing process. This will result in testing error and will create a texting_err.txt.



 
