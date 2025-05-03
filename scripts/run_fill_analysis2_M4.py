import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('math1604_quiz_cleaned.csv')  # use your actual cleaned file

# Calculate mean score per question per group
group_question_summary = df.groupby('Group').mean(numeric_only=True)

# Plot heatmap of group performance
plt.figure(figsize=(10, 6))
sns.heatmap(group_question_summary, annot=True, cmap='Blues', fmt=".2f")
plt.title('Average Performance per Group per Question')
plt.xlabel('Question')
plt.ylabel('Group')
plt.tight_layout()
plt.show()