You are given diagnostic data to determine whether a tumor is malignant (cancerous) or benign (noncancerous) based on various features extracted from breast mass images.

Your goal is to:
• Build models using ensemble algorithms (Random Forest and Gradient Boosting).
• Compare their performance with a single Decision Tree classifier.
• Visualize important metrics and evaluate model effectiveness.

Dataset Information:
We will use the Breast Cancer Wisconsin Dataset, available in sklearn.datasets.
Features:
• mean radius, mean texture, mean perimeter, mean area, etc. (30 features)
• Target:
◦ 0 → Malignant (Cancerous)
◦ 1 → Benign (Non-cancerous)

Steps:
1. Load the dataset
2. Data exploration
3. Train/Test Split
4. Train models: Decision Tree, Random Forest
5. Evaluate using Accuracy, Confusion Matrix, ROC-AUC
6. Visualize results
7. Feature Importance
