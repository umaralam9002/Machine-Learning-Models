# Machine Learning and Deep Learning Portfolio

> A practical collection of machine learning and deep learning concepts, experiments, and implementations.

## Overview

This repository covers machine learning and deep learning model concepts together with their practical implementations. It demonstrates how to inspect and prepare datasets, select suitable algorithms, train models, evaluate performance, and interpret results through metrics and visualizations.

All projects and implementations in this repository were built by **Muhammad Umar Alam**.

## Machine Learning

The root of this repository contains practical notebooks and Python scripts covering a wide range of machine learning techniques.

### Supervised Learning

- **Linear Regression** for continuous-value prediction
- **Multiple Linear Regression** using multiple input features
- **Polynomial Regression** for modeling non-linear relationships
- **Logistic Regression** for binary classification
- **K-Nearest Neighbors (KNN)** for instance-based classification
- **Naive Bayes** classification
- **Decision Trees** for interpretable classification
- **Random Forest** ensemble learning
- **Support Vector Machines (SVM)**
- **Voting Classifier** and ensemble learning

### Unsupervised Learning

- **K-Means Clustering** for grouping similar observations
- **DBSCAN Clustering** for density-based clustering and outlier discovery
- **Agglomerative Hierarchical Clustering** with dendrogram analysis

### Data Analysis and Evaluation

The implementations also demonstrate how to:

- Load and inspect structured datasets
- Clean and preprocess data
- Handle categorical values and missing data
- Scale and normalize features
- Split data into training and testing sets
- Select useful features
- Train and generate predictions from models
- Measure accuracy and regression performance
- Analyze confusion matrices and classification reports
- Compare model behavior and results
- Visualize relationships, decision boundaries, clusters, trends, and predictions with graphs

Common evaluation techniques include accuracy, precision, recall, F1-score, confusion matrices, R² score, mean absolute error, mean squared error, and cross-validation.

## Deep Learning and Natural Language Processing

The [`Neural Network`](Neural%20Network) folder contains implementations and experiments in deep learning, neural networks, and natural language processing.

### Deep Learning Models

- **Artificial Neural Networks (ANN)** for predictive modeling
- **Convolutional Neural Networks (CNN)** for image classification
- **Long Short-Term Memory (LSTM)** networks for sequence-based text classification

### NLP Concepts and Projects

- Text tokenization
- Sentence and word tokenization
- Stemming and lemmatization
- Named Entity Recognition
- Word embeddings and **Word2Vec**
- Sequence preparation and padding
- Text classification with an LSTM model
- A small **hate speech detection** project
- Transformer-based language-model experiments

These examples show how text is transformed into usable features, how neural networks are trained on sequential data, and how predictions can be evaluated for classification tasks.

## Repository Structure

```text
.
├── *.ipynb                  # Machine learning notebooks
├── *.py                     # Supporting Python scripts
├── *.csv                    # Datasets used by the notebooks
├── Neural Network/
│   ├── ANN.ipynb            # Artificial neural network
│   ├── CNN.IPYNB            # Convolutional neural network
│   ├── Hate_Speech_*.ipynb  # LSTM hate speech detection
│   ├── Tokenizattion.ipynb  # NLP tokenization exercises
│   ├── word2vec.ipynb       # Word embedding experiments
│   ├── NamedEntityRecognition.ipynb
│   └── *.py                 # Deep learning and NLP scripts
└── core/                    # Separate Django application
```

## Learning Workflow

The projects generally follow this workflow:

1. Understand the dataset and the problem statement.
2. Explore the data using statistics, tables, and graphs.
3. Clean and preprocess the features.
4. Select and configure a suitable model.
5. Train the model using training data.
6. Generate predictions on unseen data.
7. Evaluate accuracy or other relevant performance metrics.
8. Interpret the results through reports and visualizations.

## Environment Setup

The notebooks can be installed in an isolated Python environment using `uv`:

```powershell
uv venv .venv --python 3.12
.\.venv\Scripts\Activate.ps1
uv pip install -r requirements.txt
```

The machine learning and deep learning dependencies should be listed in `requirements.txt`. Some projects also require downloaded resources, such as NLTK datasets, spaCy language models, pretrained Word2Vec vectors, or Hugging Face models.

## Author

**Muhammad Umar Alam**

Machine learning and deep learning implementations, experiments, datasets, and supporting scripts in this repository were built by Muhammad Umar Alam.
