from sklearn.tree import DecisionTreeClassifier

# Sample SOC alert data (risk score)
X = [[90], [20], [85], [15], [70]]
y = ["High", "Low", "High", "Low", "Medium"]

model = DecisionTreeClassifier()
model.fit(X, y)

# Test prediction
print("Predicted Risk:", model.predict([[80]])[0])

