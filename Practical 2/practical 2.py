#!/usr/bin/env python
# coding: utf-8

# In[66]:
import pandas as pd
import matplotlib.pyplot as plt
import ruleset
import numpy as np

# In[67]:
dataset = pd.read_csv("dirty_iris.csv")

# In[68]:
dataset.head(10)

# In[69]:
new_n = dataset.dropna().shape[0]
n = dataset.shape[0]
print(f"Number of complete records:{new_n}")
print("Percentage of complete records:{:.2f}%".format(float(new_n*100/n)))

# In[70]:
dataset.dropna(inplace=True)
dataset.reset_index(inplace=True)
dataset.replace(['?',np.inf], 'NA',inplace=True)

# In[71]:
dataset.head(5)

# In[72]:
rules = []

# In[73]:
rules.append(ruleset.check_species)
rules.append(ruleset.check_positive)
rules.append(ruleset.check_petal_length)
rules.append(ruleset.check_sepal_length)
rules.append(ruleset.check_sepal_length2)

# In[74]:
violations = []
rule = list(map(lambda x: "rule"+str(x), range(1,len(rules)+1)))
for i in range(len(rules)):
    violation,desc = rules[i](dataset)
    print(f"{rule[i]}: {desc}\nviolations:{violation}")
    violations.append(violation)

# In[75]:
fig = plt.figure()
fig.patch.set_facecolor('white')
ax = fig.add_subplot()
ax.bar(rule,violations,0.3,color = 'blue')
plt.ylabel("Number of violations")
plt.xlabel("rules")
plt.title("Plotting violation in rules")
plt.show()

# In[76]:
fig = plt.figure()
fig.patch.set_facecolor('white')
ax = fig.add_subplot()
ax.boxplot(dataset["Sepal.Length"][dataset["Sepal.Length"]!='NA'])
plt.show()
