import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# 1. Load the dataset
# 2. Data exploration
# 3. Train/Test Split
# 4. Train models: Decision Tree, Random Forest
# 5. Evaluate using Accuracy, Confusion Matrix, ROC-AUC
# 6. Visualize results
# 7. Feature Importance

LINE = "*" * 80

def load_and_preprocess_data():
    # Load the dataset, treat '?' as NaN
    data = pd.read_csv('breast-cancer-wisconsin.csv', na_values='?')

    # Drop rows with missing values
    data = data.dropna()

    x = data.drop(columns=['CancerType', 'CodeNumber'], axis=1)
    y = data['CancerType']
    
    # Convert target labels: 2 (Benign) -> 0, 4 (Malignant) -> 1
    y = y.map({2: 0, 4: 1})
    
    print(f"Dataset shape: {data.shape}")
    print(f"Features: {x.shape[1]}")
    print(f"Target classes: {np.unique(y)}")
    print(f"Class distribution:")
    print(f"  - Benign (0): {np.sum(y == 0)} samples")
    print(f"  - Malignant (1): {np.sum(y == 1)} samples")
    print()

    return data, x, y

def explore_data(data, x, y):
    # Basic statistics
    print("Dataset Info:")
    print(data.info())
    print("\nFirst 5 rows:")
    print(data.head())
    print("\nBasic statistics:")
    print(data.describe())

    # Visualize important metrics and evaluate model effectiveness
    visualize_metrics_and_model_effectiveness(data, x, y)

    return data

def prepare_data(x, y, test_size=0.2, random_state=42):
    # Split the data
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    # Scale the features
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    
    print(f"Training set size: {x_train.shape[0]} samples")
    print(f"Test set size: {x_test.shape[0]} samples")
    print(f"Training set shape: {x_train.shape}")
    print(f"Test set shape: {x_test.shape}")
    print()
    
    return x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled

def visualize_metrics_and_model_effectiveness(data, x, y):
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Breast Cancer Dataset Exploration', fontsize=16, fontweight='bold')

    # 1. Target distribution
    target_counts = y.value_counts()
    axes[0, 0].pie(target_counts.values, labels=['Benign', 'Malignant'], 
                  autopct='%1.1f%%', startangle=90, colors=['#4ecdc4', '#ff6b6b'])
    axes[0, 0].set_title('Target Distribution')

    # 2. Feature correlation heatmap (top 10 features)
    correlation_matrix = data.corr(numeric_only=True)
    top_features = correlation_matrix['CancerType'].abs().sort_values(ascending=False)[1:11].index
    sns.heatmap(correlation_matrix.loc[top_features, top_features], 
                annot=True, cmap='coolwarm', center=0, ax=axes[0, 1])
    axes[0, 1].set_title('Feature Correlation Heatmap (Top 10)')

    # 3. Distribution of ClumpThickness by target
    sns.boxplot(data=data, x='CancerType', y='ClumpThickness', ax=axes[1, 0])
    axes[1, 0].set_title('Clump Thickness Distribution by Target')
    axes[1, 0].set_xlabel('CancerType (0=Benign, 1=Malignant)')

    # 4. Distribution of UniformityCellSize by target
    sns.boxplot(data=data, x='CancerType', y='UniformityCellSize', ax=axes[1, 1])
    axes[1, 1].set_title('UniformityCellSize Distribution by Target')
    axes[1, 1].set_xlabel('CancerType (0=Benign, 1=Malignant)')

    plt.tight_layout()
    plt.savefig('breast_cancer_exploration.png', dpi=300, bbox_inches='tight')
    plt.show()

# Build models using ensemble algorithms (Random Forest and Gradient Boosting).
def train_models(x_train, y_train, x_train_scaled):
    models = {
        'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
    }

    for name, model in models.items():
        print(f"Training {name}...")
        if name == 'Decision Tree':
            model.fit(x_train, y_train)
        else:
            model.fit(x_train_scaled, y_train)

    return models

# 5. Evaluate using Accuracy, Confusion Matrix, ROC-AUC
def evaluate_models(models, x_test, y_test, x_test_scaled):
    results = {}
    for name, model in models.items():
        print(f"\n{'-' * 20} {name} {'-' * 20}")
        
        # Get predictions and probabilities
        if name == 'Decision Tree':
            y_pred = model.predict(x_test)
            y_pred_proba = model.predict_proba(x_test)[:, 1]
        else:
            y_pred = model.predict(x_test_scaled)
            y_pred_proba = model.predict_proba(x_test_scaled)[:, 1]

        # Calculate metrics
        accuracy = accuracy_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        conf_matrix = confusion_matrix(y_test, y_pred)
        
        results[name] = {
            'accuracy': accuracy,
            'roc_auc': roc_auc,
            'confusion_matrix': conf_matrix,
            'predictions': y_pred,
            'probabilities': y_pred_proba
        }
        
        # Print results
        print(f"Accuracy: {accuracy:.4f}")
        print(f"ROC-AUC Score: {roc_auc:.4f}")
        print(f"Confusion Matrix:")
        print(conf_matrix)

    return results

# 6. Visualize results
def visualize_results(results, models, x, y_test):
    fig = plt.figure(figsize=(18, 12))
    fig.suptitle('Model Evaluation Metrics', fontsize=16, fontweight='bold')

    # 1. Accuracy Bar Plot
    ax1 = plt.subplot(3, 3, 1)
    accuracies = [result['accuracy'] for result in results.values()]
    model_names = list(results.keys())
    sns.barplot(x=model_names, y=accuracies, palette='viridis', ax=ax1)
    ax1.set_title('Model Accuracy')
    ax1.set_ylabel('Accuracy')
    ax1.set_ylim(0, 1)

    # 2. Confusion Matrices
    for i, (name, result) in enumerate(results.items()):
        ax = plt.subplot(3, 3, i + 2)
        sns.heatmap(result['confusion_matrix'], annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax)
        ax.set_title(f'{name} Confusion Matrix')
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')

    # 3. ROC Curves
    ax3 = plt.subplot(3, 3, 3)
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
    for i, (name, result) in enumerate(results.items()):
        fpr, tpr, _ = roc_curve(y_test, result['probabilities'])
        plt.plot(fpr, tpr, color=colors[i], lw=2, label=f'{name} (AUC = {result["roc_auc"]:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--')
    plt.title('ROC Curves')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc='lower right')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('model_evaluation_metrics.png', dpi=300)
    plt.show()

# 7. Feature Importance
def analyze_feature_importance(models, feature_names):
    for name, model in models.items():
        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
            indices = np.argsort(importances)[::-1]

            plt.figure(figsize=(10, 6))
            sns.barplot(x=importances[indices], y=np.array(feature_names)[indices], palette='magma')
            plt.title(f'Feature Importances - {name}')
            plt.xlabel('Importance Score')
            plt.ylabel('Features')
            plt.tight_layout()
            plt.savefig(f'{name.lower().replace(" ", "_")}_feature_importance.png', dpi=300)
            plt.show()
        else:
            print(f"{name} does not provide feature importances.")

def main():
    # Step 1: Load and preprocess data
    print(LINE)
    print("Step 1: Load and preprocess data")
    print(LINE)
    # x_train, x_test, y_train, y_test, feature_names = load_and_preprocess_data()
    data, x, y = load_and_preprocess_data()
    explore_data(data, x, y)
    x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = prepare_data(x, y)

    # Step 2: Train models
    print(LINE)
    print("Step 2: Train models")
    print(LINE)
    models = train_models(x_train, y_train, x_train_scaled)

    # Step 3: Evaluate models
    print(LINE)
    print("Step 3: Evaluate models")
    print(LINE)
    results = evaluate_models(models, x_test, y_test, x_test_scaled)  # Assuming no scaling needed for tree-based models

    # Step 4: Visualize results
    print(LINE)
    print("Step 4: Visualize results")
    print(LINE)
    visualize_results(results, models, x.columns, y_test)

    # Step 5: Feature importance analysis
    print(LINE) 
    print("Step 5: Feature importance analysis")
    print(LINE)
    analyze_feature_importance(models, x.columns)

    # Step 6: Print best model details
    print(LINE)
    print("Step 6: Print best model details")
    print(LINE)
    # best_model = max(results.items(), key=lambda item: item[1]['roc_auc'])
    # print(f"\nBest Model: {best_model[0]}")

if __name__ == "__main__":
    main()