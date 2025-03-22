# prompt: write code irirs dataset and visualize and train data using dtreeviz

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from dtreeviz.trees import dtreeviz
#write code irirs dataset and visualize and train data using dtreeviz

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

# Train a decision tree classifier
tree_classifier = DecisionTreeClassifier(random_state=42)
tree_classifier.fit(X_train, y_train)

# Visualize the decision tree using dtreeviz
viz = dtreeviz(tree_classifier,
              X_train,
              y_train,
              target_name='Species',
              feature_names=feature_names,
              class_names=list(target_names))

# To see the visualization, run this:
viz
