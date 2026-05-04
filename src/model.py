import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

def train_and_evaluate_model(csv_path):
    try:
        df = pd.read_csv(csv_path)
        
        # Features & Target
        # The 'Job Title' is now a string, so we must encode it.
        X_raw = df[['Job Title', 'Experience Level', 'Salary']]
        X = pd.get_dummies(X_raw, columns=['Job Title'])
        y = df['Location']
        
        # Split (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Decision Tree configuration with Hyperparameter Tuning
        param_grid = {
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 10, 20],
            'criterion': ['gini', 'entropy']
        }
        
        dt = DecisionTreeClassifier(random_state=42)
        grid_search = GridSearchCV(estimator=dt, param_grid=param_grid, cv=5, n_jobs=-1, scoring='accuracy')
        grid_search.fit(X_train, y_train)
        
        # Best model from GridSearch
        clf = grid_search.best_estimator_
        print("Best Hyperparameters:", grid_search.best_params_)
        
        # Predictions
        y_pred = clf.predict(X_test)
        
        # Evaluation Metrics
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Precision:", precision_score(y_test, y_pred, average='weighted', zero_division=0))
        print("Recall:", recall_score(y_test, y_pred, average='weighted', zero_division=0))
        print("F1 Score:", f1_score(y_test, y_pred, average='weighted', zero_division=0))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        
        return clf
    except FileNotFoundError:
        print(f"Dataset not found at {csv_path}. Please provide a valid dataset.")
        return None

if __name__ == "__main__":
    model = train_and_evaluate_model("../data/dataset.csv")
