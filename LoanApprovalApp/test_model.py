print("Step 1")

import pickle

print("Step 2")

with open("loan_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Step 3")

print(type(model))
    
if hasattr(model, "feature_names_in_"):
    print(model.feature_names_in_)