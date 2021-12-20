# HW4: Eigenfaces & Music Genre Identification

Homework problem available at
https://faculty.washington.edu/kutz/582hw4.pdf

## Preview

### Part 1: Eigenface analysis on Yale Faces B

![eigenface](https://github.com/yeewantung/AMATH-582---public/blob/master/hw4/images/crop_eigenface.png)
![eigenface2](https://github.com/yeewantung/AMATH-582---public/blob/master/hw4/images/crop_reconst.png)

### Part 2: Music genre classification

#### What becomes possible? The genre of a song can be determined by a ***5-second clip*** of the song! 

Prediction versus true class of 5-sec-music-clips by Naive Bayes

![gnbpredict](https://github.com/yeewantung/AMATH-582---public/blob/master/hw4/images/gnb_predict.png)

The accuracy of Naive Bayes with cross validation is 0.9953703703703702. 

The accuracy of predicting test set by Naive Bayes is 0.9861111111111112. 

(I have a typo in hw4.ipynb so be careful while reading. )

## Specification on files
* Report
  - [hw4.pdf](https://github.com/yeewantung/AMATH-582---public/blob/master/hw4/hw4.pdf): Report on the project
* Source code
  - [hw4.ipynb](https://github.com/yeewantung/AMATH-582---public/blob/master/hw4/hw4.ipynb): Jupyter notebook version of the code
* Datasets
  - Yale Faces B: Available at <https://faculty.washington.edu/kutz/KutzBook/KutzBook.html>
  - Music Dataset: Not available for public use
* Images
  - crop_sinval.png: Singular values of cropped images
  - crop_eigenface.png: Eigenfaces of cropped images
  - crop_weight.png: Right singular vectors of cropped images / Weights of faces projection into eigenface
  - crop_reconst.png: Original versus reconstructed faces of cropped images via low rank approximation
  - uncrop_sinval.png: Singular values of uncropped images
  - uncrop_eigenface.png: Eigenfaces of uncropped images
  - uncrop_weight.png: Right singular vectors of uncropped images / Weights of faces projection into eigenface
  - uncrop_reconst1.png, uncrop_reconst2.png, uncrop_reconst3.png: Original versus reconstructed faces of uncropped images via low rank approximation
  - test1_sinval.png: Singular values of music clips in Test 1
  - test2_sinval.png: Singular values of music clips in Test 2
  - test3_sinval.png: Singular values of music clips in Test 3
  - gnb_predict.png: Prediction versus true class of test set by Naive Bayes in Test 3
  - knn_k.png: Effect of # of nearest neighbors on classification accuracy in KNN, Test 3
  - knn_num_fea.png: Effect of # of features selected on classification accuracy in KNN, Test 3
  - svm_num_fea.png: Effect of # of features selected on classification accuracy in SVM, Test 2
  - svm_num_fea3.png: Effect of # of features selected on classification accuracy in SVM, Test 3
