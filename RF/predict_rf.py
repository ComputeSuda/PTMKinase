from keras.utils import np_utils
import joblib
import numpy as np 
import sys


def get_data_label(fea):
	if fea == 'all':
		fea = 'seq+str+dyn'

	data = np.load('data/' + fea + '/test_data.npy', allow_pickle=True).astype(float)
	label = np.load('data/' + fea + '/test_label.npy').astype(float)

	label = np_utils.to_categorical(label)

	return data, label


def predict(data,fea):
	if fea == 'all':
		fea = 'seq+str+dyn'
		
	# Get the model and predict
	rf_model = joblib.load(fea + '/rf.pkl')
	pred_prob = rf_model.predict_proba(data)
	
	return pred_prob


if __name__ == '__main__':
	# Get feature 
	fea = sys.argv[1]

	# Get the data and labels corresponding to the feature
	data, label = get_data_label(fea)

	# Get predicting probability
	pred_prob = predict(data, fea)

	# Get predicting label
	pred_label = np.argmax(pred_prob, axis=1)

	with open('result.txt', 'w') as f:
		f.write('probability\tlabel\n')
		for i in range(len(pred_prob)):
			f.write(str(pred_prob[i]) + '\t' + str(pred_label[i]) + '\n')

