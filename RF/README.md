#### Purpose

To predict kinase-PTM site using random forest method.

#### Package

python = 3.7

numpy = 1.19.4

Keras = 2.4.3

joblib = 0.16.0

sklearn = 0.23.1

#### Predict

1. To predict PTM site using all(seq+str+dyn) features, run the following command:

   python predict_rf.py all

2. To predict PTM site using seq features, run the following command:

   python predict_rf.py seq

3. To predict PTM site using str features, run the following command:

   python predict_rf.py str

4. To predict PTM site using dyn features, run the following command:

   python predict_rf.py dyn