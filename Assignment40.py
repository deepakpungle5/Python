import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score


# ============================================================
# 1. Load Dataset
# ============================================================

df = pd.read_csv("student_performance_ml.csv")

print("Dataset:")
print(df.head())


# ============================================================
# 2. Full Features
# ============================================================

features = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[features]
y = df["FinalResult"]


# ============================================================
# 3. Train Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ============================================================
# 4. Train Decision Tree
# ============================================================

model = DecisionTreeClassifier(
    random_state=42
)

model.fit(X_train, y_train)


# ============================================================
# 5. Feature Importance
# ============================================================

print("\n========== FEATURE IMPORTANCE ==========")

for feature, importance in zip(
    X.columns,
    model.feature_importances_
):

    print(
        feature,
        ":",
        importance
    )


print(
    "Most Important:",
    X.columns[
        model.feature_importances_.argmax()
    ]
)

print(
    "Least Important:",
    X.columns[
        model.feature_importances_.argmin()
    ]
)


# ============================================================
# 6. Original Accuracy
# ============================================================

y_pred = model.predict(X_test)

original_accuracy = accuracy_score(
    y_test,
    y_pred
)

print(
    "\nOriginal Testing Accuracy:",
    original_accuracy * 100,
    "%"
)


# ============================================================
# 7. Remove SleepHours
# ============================================================

X_without_sleep = df[
    [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted"
    ]
]

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X_without_sleep,
    y,
    test_size=0.2,
    random_state=42
)

model2 = DecisionTreeClassifier(
    random_state=42
)

model2.fit(
    X_train2,
    y_train2
)

pred2 = model2.predict(X_test2)

accuracy2 = accuracy_score(
    y_test2,
    pred2
)

print(
    "\nAccuracy without SleepHours:",
    accuracy2 * 100,
    "%"
)


# ============================================================
# 8. Only StudyHours + Attendance
# ============================================================

X_two = df[
    [
        "StudyHours",
        "Attendance"
    ]
]

X_train3, X_test3, y_train3, y_test3 = train_test_split(
    X_two,
    y,
    test_size=0.2,
    random_state=42
)

model3 = DecisionTreeClassifier(
    random_state=42
)

model3.fit(
    X_train3,
    y_train3
)

pred3 = model3.predict(X_test3)

accuracy3 = accuracy_score(
    y_test3,
    pred3
)

print(
    "Accuracy using StudyHours + Attendance:",
    accuracy3 * 100,
    "%"
)


# ============================================================
# 9. Five New Students
# ============================================================

new_students = pd.DataFrame({

    "StudyHours": [2, 4, 6, 8, 10],

    "Attendance": [60, 70, 85, 90, 95],

    "PreviousScore": [45, 55, 66, 75, 88],

    "AssignmentsCompleted": [3, 5, 7, 8, 10],

    "SleepHours": [5, 6, 7, 7, 8]
})

new_prediction = model.predict(
    new_students
)

new_students["Result"] = new_prediction

new_students["Result"] = new_students[
    "Result"
].map({
    0: "Fail",
    1: "Pass"
})

print("\n========== FIVE STUDENTS ==========")
print(new_students)


# ============================================================
# 10. Manual Accuracy
# ============================================================

correct = 0

for actual, predicted in zip(
    y_test,
    y_pred
):

    if actual == predicted:
        correct += 1

manual_accuracy = correct / len(y_test)

print(
    "\nManual Accuracy:",
    manual_accuracy * 100,
    "%"
)


# ============================================================
# 11. Misclassified Students
# ============================================================

comparison = X_test.copy()

comparison["Actual"] = y_test

comparison["Predicted"] = y_pred

misclassified = comparison[
    comparison["Actual"] != comparison["Predicted"]
]

print("\n========== MISCLASSIFIED ==========")
print(misclassified)

print(
    "Number of Misclassified:",
    len(misclassified)
)


# ============================================================
# 12. Random State Comparison
# ============================================================

print("\n========== RANDOM STATE ==========")

for state in [0, 10, 42]:

    Xtr, Xte, ytr, yte = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=state
    )

    tree = DecisionTreeClassifier(
        random_state=state
    )

    tree.fit(Xtr, ytr)

    pred = tree.predict(Xte)

    acc = accuracy_score(
        yte,
        pred
    )

    print(
        "random_state =",
        state,
        "Accuracy =",
        acc * 100,
        "%"
    )


# ============================================================
# 13. Decision Tree Visualization
# ============================================================

plt.figure(figsize=(18, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Fail", "Pass"],
    filled=True
)

plt.title(
    "Decision Tree Visualization"
)

plt.show()


# ============================================================
# 14. PerformanceIndex
# ============================================================

df["PerformanceIndex"] = (
    df["StudyHours"] * 2
) + df["Attendance"]

X_performance = df[
    [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours",
        "PerformanceIndex"
    ]
]

Xtr, Xte, ytr, yte = train_test_split(
    X_performance,
    y,
    test_size=0.2,
    random_state=42
)

performance_model = DecisionTreeClassifier(
    random_state=42
)

performance_model.fit(
    Xtr,
    ytr
)

performance_prediction = performance_model.predict(
    Xte
)

performance_accuracy = accuracy_score(
    yte,
    performance_prediction
)

print(
    "\nAccuracy with PerformanceIndex:",
    performance_accuracy * 100,
    "%"
)


# ============================================================
# 15. max_depth=None
# ============================================================

deep_model = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

deep_model.fit(
    X_train,
    y_train
)

train_pred = deep_model.predict(
    X_train
)

test_pred = deep_model.predict(
    X_test
)

train_accuracy = accuracy_score(
    y_train,
    train_pred
)

test_accuracy = accuracy_score(
    y_test,
    test_pred
)

print("\n========== MAX DEPTH NONE ==========")

print(
    "Training Accuracy:",
    train_accuracy * 100,
    "%"
)

print(
    "Testing Accuracy:",
    test_accuracy * 100,
    "%"
)


# ============================================================
# Final Conclusion
# ============================================================

print("\n========== CONCLUSION ==========")

if train_accuracy > test_accuracy:
    print(
        "Training accuracy is higher than testing accuracy."
    )

    print(
        "The model may be overfitting."
    )

else:
    print(
        "Training and testing performance are comparable."
    )