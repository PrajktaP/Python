import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier

# 1. Load the dataset
# 2. Data exploration
# 3. Train/Test Split
# 4. Train models: Decision Tree, Random Forest, Gradient Boosting
# 5. Evaluate using Accuracy, Confusion Matrix, ROC-AUC
# 6. Visualize results
# 7. Feature Importance

LINE = "*" * 80

def load_and_preprocess_data():
    """Load the dataset and preprocess it."""
    print(LINE)
    print("LOADING BREAST CANCER WISCONSIN DATASET")
    print(LINE)
    
    # Load the dataset, treat '?' as NaN
    data = pd.read_csv('breast-cancer-wisconsin.csv', na_values='?')

    # Drop rows with missing values
    data = data.dropna()

    X = data.drop(columns=['CancerType', 'CodeNumber'], axis=1)
    y = data['CancerType']
    
    print(f"Dataset shape: {data.shape}")
    print(f"Features: {X.shape[1]}")
    print(f"Target classes: {np.unique(y)}")
    print(f"Class distribution:")
    print(f"  - Benign (0): {np.sum(y == 0)} samples")
    print(f"  - Malignant (1): {np.sum(y == 1)} samples")
    print()

    return data, X, y

def explore_data(data, X, y):
    """Perform exploratory data analysis."""
    print(LINE)
    print("EXPLORATORY DATA ANALYSIS")
    print(LINE)
    
    # Basic statistics
    print("Dataset Info:")
    print(data.info())
    print("\nFirst 5 rows:")
    print(data.head())
    print("\nBasic statistics:")
    print(data.describe())

    # Visualize important metrics and evaluate model effectiveness
    visualize_metrics_and_model_effectiveness(data, X, y)

    return data

def visualize_metrics_and_model_effectiveness(data, X, y):
    """Create exploratory data visualization plots."""
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

def prepare_data(X, y, test_size=0.2, random_state=42):
    """Prepare data for training by splitting and scaling."""
    print(LINE)
    print("DATA PREPARATION")
    print(LINE)
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Training set size: {X_train.shape[0]} samples")
    print(f"Test set size: {X_test.shape[0]} samples")
    print(f"Training set shape: {X_train.shape}")
    print(f"Test set shape: {X_test.shape}")
    print()
    
    return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler

def train_models(X_train, y_train, X_train_scaled):
    """Train Decision Tree, Random Forest, and Gradient Boosting models."""
    print(LINE)
    print("TRAINING MODELS")
    print(LINE)
    
    # Initialize models
    models = {
        'Decision Tree': DecisionTreeClassifier(
            max_depth=5, 
            random_state=42,
            criterion='gini'
        ),
        'Random Forest': RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        ),
        'Gradient Boosting': GradientBoostingClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            random_state=42
        )
    }
    
    # Train models
    for name, model in models.items():
        print(f"Training {name}...")
        if name == 'Decision Tree':
            model.fit(X_train, y_train)
        else:
            model.fit(X_train_scaled, y_train)
        print(f"✓ {name} training completed")
    
    print("\nAll models trained successfully!")
    return models

def evaluate_models(models, X_test, y_test, X_test_scaled):
    """Evaluate all models using various metrics."""
    print(LINE)
    print("MODEL EVALUATION")
    print(LINE)
    
    results = {}
    
    for name, model in models.items():
        print(f"\n{'-' * 20} {name} {'-' * 20}")
        
        # Get predictions and probabilities
        if name == 'Decision Tree':
            y_pred = model.predict(X_test)
            y_pred_proba = model.predict_proba(X_test)[:, 1]
        else:
            y_pred = model.predict(X_test_scaled)
            y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
        
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
        print(f"\nClassification Report:")
        print(classification_report(y_test, y_pred, 
                                  target_names=['Benign', 'Malignant']))
    
    return results

def visualize_results(results, models, feature_names, y_test):
    """Create comprehensive visualization of model results."""
    print(LINE)
    print("CREATING VISUALIZATIONS")
    print(LINE)
    
    # Create a large figure with multiple subplots
    fig = plt.figure(figsize=(20, 15))
    
    # 1. Accuracy Comparison
    ax1 = plt.subplot(3, 3, 1)
    accuracies = [results[name]['accuracy'] for name in results.keys()]
    plt.bar(results.keys(), accuracies, color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
    plt.title('Model Accuracy Comparison', fontweight='bold')
    plt.ylabel('Accuracy')
    plt.xticks(rotation=45)
    for i, v in enumerate(accuracies):
        plt.text(i, v + 0.01, f'{v:.3f}', ha='center', fontweight='bold')
    
    # 2. ROC-AUC Comparison
    ax2 = plt.subplot(3, 3, 2)
    roc_aucs = [results[name]['roc_auc'] for name in results.keys()]
    plt.bar(results.keys(), roc_aucs, color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
    plt.title('Model ROC-AUC Comparison', fontweight='bold')
    plt.ylabel('ROC-AUC Score')
    plt.xticks(rotation=45)
    for i, v in enumerate(roc_aucs):
        plt.text(i, v + 0.01, f'{v:.3f}', ha='center', fontweight='bold')
    
    # 3. ROC Curves
    ax3 = plt.subplot(3, 3, 3)
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
    for i, (name, result) in enumerate(results.items()):
        fpr, tpr, _ = roc_curve(y_test, result['probabilities'])
        plt.plot(fpr, tpr, color=colors[i], lw=2, 
                label=f'{name} (AUC = {result["roc_auc"]:.3f})')
    plt.plot([0, 1], [0, 1], 'k--', lw=1)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves', fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 4-6. Confusion Matrices
    for i, (name, result) in enumerate(results.items()):
        ax = plt.subplot(3, 3, 4 + i)
        sns.heatmap(result['confusion_matrix'], annot=True, fmt='d', 
                   cmap='Blues', cbar=False, ax=ax)
        ax.set_title(f'{name} - Confusion Matrix', fontweight='bold')
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        ax.set_xticklabels(['Benign', 'Malignant'])
        ax.set_yticklabels(['Benign', 'Malignant'])
    
    # 7. Feature Importance (Random Forest)
    ax7 = plt.subplot(3, 3, 7)
    rf_model = models['Random Forest']
    feature_importance = rf_model.feature_importances_
    top_features_idx = np.argsort(feature_importance)[-10:]  # Top 10 features
    top_features = [feature_names[i] for i in top_features_idx]
    top_importance = feature_importance[top_features_idx]
    
    plt.barh(range(len(top_features)), top_importance, color='#4ecdc4')
    plt.yticks(range(len(top_features)), top_features)
    plt.xlabel('Feature Importance')
    plt.title('Top 10 Feature Importance (Random Forest)', fontweight='bold')
    
    # 8. Model Performance Summary
    ax8 = plt.subplot(3, 3, 8)
    ax8.axis('off')
    
    # Create a summary table
    summary_data = []
    for name, result in results.items():
        summary_data.append([
            name,
            f"{result['accuracy']:.3f}",
            f"{result['roc_auc']:.3f}"
        ])
    
    table = ax8.table(cellText=summary_data,
                     colLabels=['Model', 'Accuracy', 'ROC-AUC'],
                     cellLoc='center',
                     loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    ax8.set_title('Model Performance Summary', fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('breast_cancer_model_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

def analyze_feature_importance(models, feature_names):
    """Analyze and visualize feature importance across all models."""
    print(LINE)
    print("FEATURE IMPORTANCE ANALYSIS")
    print(LINE)
    
    # Get feature importance from all models
    importance_data = {}
    
    # Decision Tree feature importance
    dt_model = models['Decision Tree']
    importance_data['Decision Tree'] = dt_model.feature_importances_
    
    # Random Forest feature importance
    rf_model = models['Random Forest']
    importance_data['Random Forest'] = rf_model.feature_importances_
    
    # Gradient Boosting feature importance
    gb_model = models['Gradient Boosting']
    importance_data['Gradient Boosting'] = gb_model.feature_importances_
    
    # Create visualization
    fig, axes = plt.subplots(1, 3, figsize=(20, 8))
    fig.suptitle('Feature Importance Comparison Across Models', fontsize=16, fontweight='bold')
    
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
    
    for i, (model_name, importance) in enumerate(importance_data.items()):
        # Get top 10 features
        top_features_idx = np.argsort(importance)[-10:]
        top_features = [feature_names[j] for j in top_features_idx]
        top_importance = importance[top_features_idx]
        
        axes[i].barh(range(len(top_features)), top_importance, color=colors[i])
        axes[i].set_yticks(range(len(top_features)))
        axes[i].set_yticklabels(top_features)
        axes[i].set_xlabel('Feature Importance')
        axes[i].set_title(f'{model_name} - Top 10 Features', fontweight='bold')
        axes[i].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('feature_importance_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print top 5 features for each model
    print("\nTop 5 Most Important Features by Model:")
    for model_name, importance in importance_data.items():
        top_5_idx = np.argsort(importance)[-5:][::-1]
        print(f"\n{model_name}:")
        for j, idx in enumerate(top_5_idx, 1):
            print(f"  {j}. {feature_names[idx]}: {importance[idx]:.4f}")

def main():
    """Main function to run the breast cancer classification analysis."""
    print("🚀 STARTING BREAST CANCER CLASSIFICATION ANALYSIS")
    print(LINE)
    
    # Step 1: Load the dataset
    data, X, y = load_and_preprocess_data()
    
    # Step 2: Data exploration
    explore_data(data, X, y)
    
    # Step 3: Prepare data (train/test split)
    X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler = prepare_data(X, y)
    
    # Step 4: Train models
    models = train_models(X_train, y_train, X_train_scaled)
    
    # Step 5: Evaluate models
    results = evaluate_models(models, X_test, y_test, X_test_scaled)
    
    # Step 6: Visualize results
    visualize_results(results, models, X.columns, y_test)
    
    # Step 7: Feature importance analysis
    analyze_feature_importance(models, X.columns)
    
    # Print final summary
    print("\n" + LINE)
    print("FINAL MODEL PERFORMANCE SUMMARY")
    print(LINE)
    
    best_model = max(results.items(), key=lambda x: x[1]['accuracy'])
    print(f"Best performing model: {best_model[0]}")
    print(f"Best accuracy: {best_model[1]['accuracy']:.4f}")
    print(f"Best ROC-AUC: {best_model[1]['roc_auc']:.4f}")
    
    print("\n" + LINE)
    print("✅ ANALYSIS COMPLETED SUCCESSFULLY!")
    print(LINE)
    print("\nGenerated files:")
    print("- breast_cancer_exploration.png")
    print("- breast_cancer_model_comparison.png")
    print("- feature_importance_comparison.png")
    print("\n" + LINE)
    print("ANALYSIS COMPLETE!")
    print(LINE)

if __name__ == "__main__":
    main()