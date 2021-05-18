import sys

import numpy as np
import pandas as pd
from keras.models import load_model


"""
This script first obtains the data and the deep learn model based on the selected features, 
and then uses the deep learning method to make predictions.
"""


def get_data(input_file, fea):
    """
    Get the corresponding data according to the input file.
    """

    data = pd.read_excel(input_file)
    
    res_mapping = {'A':1,'R':2,'N':3,'D':4,'C':5,'G':6,'Q':7,'E':8,'H':9,'I':10,'L':11,
                   'K':12,'M':13,'P':14, 'F':15,'S':16,'T':17,'Y':18,'W':19,'V':20}
    data['res'] = data['res'].map(res_mapping)

    data = data.fillna(0)
    data = data.replace(np.inf, 1)
    data = data.replace(-np.inf, 0)
    
    dataset = []
    for indexs in data.index:   
        if fea == 'all' or fea == 'seq':    
            content = np.array(data.loc[indexs].values[2:])
        else:
            content = np.array(data.loc[indexs].values[3:])         
        dataset.append(content)
    
    dataset = np.array(dataset).astype(float)

    return dataset


def predict(data,fea):
    """
    Get the corressponding deep learning model and make predictions.
    """

    print('......start predicting......')

    if fea == 'all':
        fea = 'seq_str_dyn'

    model_num = 5
    pred_prob = None

    # Get the model and predict
    for i in range(model_num):
        model = load_model(fea + '/fnn_3class_' + str(i) + '.h5', compile=False)
        if i == 0:
            pred_prob = model.predict(data)
        else:
            pred_prob += model.predict(data)

    pred_prob /= 5

    return pred_prob


def write_output_file(input_file, pred_prob, pred_label):
    """
    Write the predicted probability and predicted label to the last two columns of the original file.
    And save it as out_file.xlsx in the current folder.
    """

    output_file = pd.read_excel(input_file)
    pred_prob = pred_prob.tolist()
    for i in range(len(pred_prob)):
    	for j in range(3):
    		pred_prob[i][j] = round(pred_prob[i][j], 2)
    output_file['pred_prob'] = pred_prob
    output_file['pred_label'] = pred_label.tolist()
    output_file.to_excel('output_file.xlsx', index=False)

    print('done')


if __name__ == '__main__':
    # Get input file
    input_file = sys.argv[1]

    # Get feature 
    fea = sys.argv[2]

    # Get the data from input file.
    data = get_data(input_file, fea)

    # Get predicting probability
    pred_prob = predict(data, fea)

    # Get predicting label
    pred_label = np.argmax(pred_prob, axis=1)

    # write the predicted result to output file
    write_output_file(input_file, pred_prob, pred_label)
