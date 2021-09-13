# -*- coding: utf-8 -*-
"""SVM_Precision_Recall.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tizqq03lsOCERFgZ7x3drnUV1Jytjrvg
"""

import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import cv2
import numpy as np
from sklearn.decomposition import PCA

def plot_func(y,plt_file,plt_title,dim,jump,start):
  x =  range(start,dim+1,jump)
  plt.plot(x, y, color='red', marker='o', markerfacecolor='red', markersize=3)
  plt.xlabel('PCA Component')
  plt.ylabel(f'{plt_title}')
  plt.title(f'{plt_title}')
  plt.ylim(0, 1)
  plt.grid()
  plt.savefig(plt_file)
  plt.close()
  return

digits = datasets.load_digits()
n_samples = len(digits.images)
image = digits.images
data = digits.images.reshape((n_samples, -1))
dim = data.shape[1]
variance = np.zeros((dim-1))
pca = PCA(n_components=dim)
pca.fit(data)
var = pca.explained_variance_ratio_
variance[0] = var[0] + var[1]
for i in range(1,dim-1):
  variance[i] = variance[i-1] + var[i+1]
n = np.where(variance>0.99)[0][0]
print(f'For having at least 0.99 variance, We need n_component of PCA to be {n}.')

pca = PCA(n_components=n)
pca.fit(data)
pca_data = pca.transform(data)
x_train, x_test, y_train, y_test = train_test_split(pca_data, digits.target, test_size=0.3, shuffle=True)

clf = svm.SVC(kernel = 'rbf', gamma=0.001, C = 10)
clf.fit(x_train, y_train)
Predicted_Train = clf.predict(x_train)
Predicted_Test = clf.predict(x_test)
Precision_Score_Train = metrics.precision_score(y_train,Predicted_Train,average='macro')
Precision_Score_Test = metrics.precision_score(y_test,Predicted_Test,average='macro')
Recall_Score_Train = metrics.recall_score(y_train,Predicted_Train,average='macro')
Recall_Score_Test = metrics.recall_score(y_test,Predicted_Test,average='macro')
print('Precision: ')
print(f'Precision score for train data is {Precision_Score_Train}.')
print(f'Precision score for test data is {Precision_Score_Test}.')
print('recall: ')
print(f'recall score for train data is {Recall_Score_Train}.')
print(f'recall score for test data is {Recall_Score_Test}.')