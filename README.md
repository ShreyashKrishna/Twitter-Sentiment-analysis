# Twitter-Sentiment-analysis
Predicts the sentiment expressed in the given statement
Introduction
Description:  It analyzes the sentiments behind any piece of text. It takes text/sentences as input from the user and outputs the sentiments  of the text as either positive or negative.
How does it work?: The program learns from a large size of tweets that form the training data to the learning algorithm. First, the data was trained using a model (in this case using Gaussian Naive Bayes). Second, some input is fed from the user to the model. The model based on its trained data predicts the sentiment of the input data.

Motivation
Sentiment analysis is quite popular while analysing the success of any product. For example Flipkart categorizes the reviews as positive or negative and is able to ascertain the reaction consumers have to a product. Similarly, through tweets it becomes possible to infer the reaction/sentiments of people to certain events and issues (for e.g. demonetization)

Implementation & Progress
Methods used: We tried three different approaches to the problem:
Logistic Regression
Gaussian Naive Bayes
SVM
After analyzing the accuracies yielded at the end from all three methods (62%, 61% and 58% respectively) and the running time we decided to use Naive Bayes.
Used stop words to avoid occurrences of high probability words like “I”, “am”,etc. as these don't have any sentimental significance. 
Performed 10-fold cross validation to reduce overfitting.

Tools used: The Python libraries used in the project were :
Sklearn: data representation (eg. creating hierarchical folders for storing the tweets as individual files)
Numpy
Tkinter : frontend

Testing Strategy
Usage of 10-fold cross-validation: The training data was divided into 10 parts out of which 1 is used as the test data and the 9 parts were used as training data. The accuracy is taken out on this model and repeated again 10 times with different permutations of this division as train and test. Then the final average of the 10 individual accuracies is taken out to get a proper idea of the accuracy of the sample.

Interesting Bugs
Unidentifiable characters: Many tweets had alien characters which could not be converted into string using ASCII while reading them. Due to this, we filtered them out using regex which permitted only characters like: A to z/ 0 to 9 to be read from the tweet file. This may have led to losing out on key forms of sentiment expression like :) and other emoticons.
Data size problem: When we tried to run the program on a large dataset, it took extremely long to process. Due to this we had to test it on a small dataset and thereby lost out on good accuracy in prediction.
Input matrix size: While reading the input from the user and counting frequency, the matrix size of input did not match. We, with the help of professor, got to know that while vectorizing, it has to be mapped to data vocabularies.

