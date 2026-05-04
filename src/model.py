import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

def train_and_evaluate_model(csv_path):
    # This is a template function since the exact dataset isn't provided
    try:
        df = pd.read_csv(csv_path)
        
        # Features: Job Title, Experience Level, Salary
        X = df[['Job Title', 'Experience Level', 'Salary']]
        # Target: Location
        y = df['Location']
        
        # Split (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Decision Tree configuration
        clf = DecisionTreeClassifier(random_state=42)
        clf.fit(X_train, y_train)
        
        # Predictions
        y_pred = clf.predict(X_test)
        
        # Evaluation
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
    # Placeholder for running the script directly
    model = train_and_evaluate_model("../data/dataset.csv")
