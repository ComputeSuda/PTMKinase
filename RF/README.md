## 1. Purpose

To predict kinase-PTM site using random forest method.

## 2. System requirements

Installation and running has been tested in Ubuntu 18.04.4 LST with python 3.7.7.

#### Package version

+ python = 3.7.7
+ numpy = 1.18.5
+ joblib = 0.16.0
+ sklearn = 0.22.2.post1
+ pandas = 1.2.0

#### You can install the dependent packages by the following commands:

+ pip install python==3.7.7
+ pip install numpy==1.18.5
+ pip install joblib==0.16.0
+ pip install sckit-learn==0.22.2.post1
+ pip install pandas==1.2.0

## 3. Predicting

+ To predict PTM site using all(seq+str+dyn) features, run the following command:

    python predict_rf.py [input_file] all

+ To predict PTM site using seq features, run the following command:

​    python predict_rf.py  [input_file] seq

+ To predict PTM site using str features, run the following command:

​    python predict_rf.py [input_file] str

+ To predict PTM site using dyn features, run the following command:

​    python predict_rf.py  [input_file] dyn

[input_file] is the user's test dataset, which is saved as an excel file. For standardization, the first column of excel represents Uniprot, the second column is the corresponding PDB, the third column is the residue type. The fourth to last column is the corresponding features.  The name and order of columns of input file should be consistent with the text_data_feature.xlsx in the demo folder of ./data.

The predicted probability and predicted label are added to the last two columns of the input file and save it as out_file.xlsx  in the current folder. The label 0 indicates that this data belongs to other class. The 1 means that the data belongs PTM class. The 2 indicates that this data belongs to Bind class.

### Training and testing data are provided in the folder of ./data.