# ============================================================
# Student Performance ML Dataset
# Machine Learning using Decision Tree Classifier
# ============================================================

# ------------------------------------------------------------
# 1. Import Required Libraries
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# ------------------------------------------------------------
# 2. Load Dataset
# ------------------------------------------------------------

file_path = "student_performance_ml.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("STUDENT PERFORMANCE ML DATASET")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())


# ------------------------------------------------------------
# 3. Data Analysis
# ------------------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# ------------------------------------------------------------
# 4. Separate Input Features and Target Variable
# ------------------------------------------------------------

X = df[
    [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
]

y = df["FinalResult"]


# ------------------------------------------------------------
# 5. Visualization
# ------------------------------------------------------------

# Distribution of Final Result

plt.figure(figsize=(6, 4))

df["FinalResult"].value_counts().sort_index().plot(
    kind="bar"
)

plt.title("Pass / Fail Distribution")
plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 6. Train-Test Split
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data Size:", X_train.shape)
print("Testing Data Size :", X_test.shape)


# ------------------------------------------------------------
# 7. Create and Train Decision Tree Classifier
# ------------------------------------------------------------

model = DecisionTreeClassifier(
    random_state=42
)

model.fit(X_train, y_train)

print("\nDecision Tree Model Trained Successfully!")


# ------------------------------------------------------------
# 8. Prediction on X_test
# ------------------------------------------------------------

y_pred = model.predict(X_test)

print("\nPredicted Results:")
print(y_pred)


# ------------------------------------------------------------
# 9. Accuracy Calculation
# ------------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nTesting Accuracy:")
print(f"{accuracy * 100:.2f}%")


# ------------------------------------------------------------
# 10. Confusion Matrix
# ------------------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# Display Confusion Matrix

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)

disp.plot()

plt.title("Confusion Matrix")
plt.show()


# ------------------------------------------------------------
# 11. Explain TP, TN, FP and FN
# ------------------------------------------------------------

tn, fp, fn, tp = cm.ravel()

print("\nConfusion Matrix Components:")
print("True Negative  (TN):", tn)
print("False Positive (FP):", fp)
print("False Negative (FN):", fn)
print("True Positive  (TP):", tp)


# ------------------------------------------------------------
# 12. Training Accuracy
# ------------------------------------------------------------

train_pred = model.predict(X_train)

training_accuracy = accuracy_score(
    y_train,
    train_pred
)

print("\nTraining Accuracy:")
print(f"{training_accuracy * 100:.2f}%")


# ------------------------------------------------------------
# 13. Testing Accuracy
# ------------------------------------------------------------

testing_accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nTesting Accuracy:")
print(f"{testing_accuracy * 100:.2f}%")


# ------------------------------------------------------------
# 14. Check Overfitting / Underfitting
# ------------------------------------------------------------

print("\nModel Evaluation:")

difference = training_accuracy - testing_accuracy

if training_accuracy > 0.95 and difference > 0.10:

    print("The model may be OVERFITTING.")

elif training_accuracy < 0.75 and testing_accuracy < 0.75:

    print("The model may be UNDERFITTING.")

else:

    print("The model appears to have reasonable generalization.")


# ------------------------------------------------------------
# 15. Decision Tree with max_depth = 1
# ------------------------------------------------------------

model_depth_1 = DecisionTreeClassifier(
    max_depth=1,
    random_state=42
)

model_depth_1.fit(X_train, y_train)

pred_depth_1 = model_depth_1.predict(X_test)

accuracy_depth_1 = accuracy_score(
    y_test,
    pred_depth_1
)


# ------------------------------------------------------------
# 16. Decision Tree with max_depth = 3
# ------------------------------------------------------------

model_depth_3 = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model_depth_3.fit(X_train, y_train)

pred_depth_3 = model_depth_3.predict(X_test)

accuracy_depth_3 = accuracy_score(
    y_test,
    pred_depth_3
)


# ------------------------------------------------------------
# 17. Decision Tree with max_depth = None
# ------------------------------------------------------------

model_depth_none = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

model_depth_none.fit(X_train, y_train)

pred_depth_none = model_depth_none.predict(X_test)

accuracy_depth_none = accuracy_score(
    y_test,
    pred_depth_none
)


# ------------------------------------------------------------
# 18. Compare Three Decision Tree Models
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DECISION TREE DEPTH COMPARISON")
print("=" * 60)

print(
    f"max_depth = 1    : {accuracy_depth_1 * 100:.2f}%"
)

print(
    f"max_depth = 3    : {accuracy_depth_3 * 100:.2f}%"
)

print(
    f"max_depth = None : {accuracy_depth_none * 100:.2f}%"
)


# ------------------------------------------------------------
# 19. Prediction for New Student
# ------------------------------------------------------------

# Student details:
# StudyHours = 6
# Attendance = 85
# PreviousScore = 66
# AssignmentsCompleted = 7
# SleepHours = 7

new_student = pd.DataFrame(
    [[6, 85, 66, 7, 7]],
    columns=[
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]
)


prediction = model.predict(new_student)

print("\n" + "=" * 60)
print("NEW STUDENT PREDICTION")
print("=" * 60)

if prediction[0] == 1:

    print("Predicted Result: PASS")

else:

    print("Predicted Result: FAIL")


# ------------------------------------------------------------
# 20. Prediction Probability
# ------------------------------------------------------------

probability = model.predict_proba(new_student)

print("\nPrediction Probability:")

print(
    f"Fail Probability : {probability[0][0] * 100:.2f}%"
)

print(
    f"Pass Probability : {probability[0][1] * 100:.2f}%"
)


# ------------------------------------------------------------
# 21. Final Conclusion
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FINAL CONCLUSION")
print("=" * 60)

print("""
The Student Performance dataset was analyzed using
a Decision Tree Classifier.

The model was trained using student academic and
behavioral features such as StudyHours, Attendance,
PreviousScore, AssignmentsCompleted and SleepHours.

Training and testing accuracy were calculated.
A confusion matrix was generated to evaluate the
classification performance.

Three Decision Tree models with different maximum
depths were also compared.

Finally, the trained model was used to predict whether
a new student would Pass or Fail.
""")