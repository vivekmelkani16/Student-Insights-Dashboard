# import pandas as pd
# import numpy as np

# # Set a seed for reproducibility
# np.random.seed(42)

# # Define the number of students
# num_students = 100

# # Generate sample data
# data = {
#     'StudentID': range(1, num_students + 1),
#     'Subject': np.random.choice(['Math', 'Science', 'English'], num_students),
#     'Attendance_Rate': np.random.uniform(70, 100, num_students).round(2),
#     'Extracurriculars': np.random.choice(['Sports', 'Music', 'Debate', 'None'], num_students),
#     'Academic_Score': np.random.uniform(50, 100, num_students).round(2)
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Save the DataFrame to a CSV file
# df.to_csv('student_data.csv', index=False)

# print("Sample dataset created successfully!")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('student_data.csv')

# --- 1. Data Cleaning and Preparation (if needed) ---
# Check for missing values (our synthetic data has none, but it's good practice)
print("Missing values in the dataset:")
print(df.isnull().sum())

# --- 2. Data Analysis ---
print("\nDescriptive statistics for Academic Score:")
print(df['Academic_Score'].describe())

# Analyze academic score by subject
subject_scores = df.groupby('Subject')['Academic_Score'].mean().reset_index()
print("\nAverage Academic Score by Subject:")
print(subject_scores)

# Analyze academic score by extracurriculars
extracurricular_scores = df.groupby('Extracurriculars')['Academic_Score'].mean().reset_index()
print("\nAverage Academic Score by Extracurriculars:")
print(extracurricular_scores)

# --- 3. Data Visualization ---

# Set a professional style for plots
plt.style.use('seaborn-v0_8-whitegrid')

# Visualization 1: Histogram of Academic Scores
plt.figure(figsize=(10, 6))
plt.hist(df['Academic_Score'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Academic Scores', fontsize=16)
plt.xlabel('Academic Score', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.show()

# Visualization 2: Bar plot of Average Score by Subject
plt.figure(figsize=(10, 6))
plt.bar(subject_scores['Subject'], subject_scores['Academic_Score'], color=['coral', 'lightgreen', 'gold'])
plt.title('Average Academic Score by Subject', fontsize=16)
plt.xlabel('Subject', fontsize=12)
plt.ylabel('Average Academic Score', fontsize=12)
plt.show()

# Visualization 3: Box plot of Scores by Extracurriculars
plt.figure(figsize=(12, 7))
df.boxplot(column='Academic_Score', by='Extracurriculars', grid=False, rot=0)
plt.title('Academic Score Distribution by Extracurricular Activities', fontsize=16)
plt.suptitle('')  # Suppress default title
plt.xlabel('Extracurricular Activities', fontsize=12)
plt.ylabel('Academic Score', fontsize=12)
plt.show()

# Visualization 4: Scatter plot of Attendance vs. Academic Score
plt.figure(figsize=(10, 6))
plt.scatter(df['Attendance_Rate'], df['Academic_Score'], alpha=0.6, color='purple')
plt.title('Correlation between Attendance Rate and Academic Score', fontsize=16)
plt.xlabel('Attendance Rate (%)', fontsize=12)
plt.ylabel('Academic Score', fontsize=12)
plt.show()