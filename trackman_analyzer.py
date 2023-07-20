# %% [markdown]
# ### Lesson 5.4: Final Project - Part 1
# 
# Summary: This lesson is the first part of your final project. In this assignment, you will focus on importing, cleaning, preprocessing, and summarizing your baseball pitching data, as provided in a Trackman Report CSV file. 
# 
# Key Concepts:
# - Importing data using pandas
# - Cleaning and preprocessing data
# - Summarizing data using descriptive statistics
# 
# **The link to your assignment is [here](https://chat.openai.com/share/911fa90a-0d8a-45ee-a20f-a0822e327885)**
# 
# Assignment:
# 1. Importing and Cleaning the Data
#     - Use pandas to import your Trackman Report data into a DataFrame.
#     - Clean the data:
#         - Handle any missing values in the data. This could mean dropping rows or columns with missing values, or filling in missing values with a specified value.
#         - Rename columns for consistency and ease of understanding. You might not have exact matches for "velocity", "spin rate", "pitch type", and "result", so figure out which columns correspond to these descriptions and rename them accordingly.
#     - Preprocess the data:
#         - Create a smaller DataFrame that only includes the columns of interest ("velocity", "spin rate", "pitch type", and "result").
#         - Ensure the data types for these columns are appropriate for further analysis. For example, "velocity" and "spin rate" should be numeric, while "pitch type" and "result" should be categorical.
# 2. Summarizing the Data
#     - Use pandas methods to calculate basic descriptive statistics for your data, including mean, median, mode, range, and standard deviation.
#     - Identify any interesting initial observations from these statistics. For example, what is the average velocity or spin rate across all pitches?
#     - Use matplotlib to create simple visualizations of these statistics, such as a histogram for velocity or a bar plot for pitch type frequency.

# %%
import os
import pandas as pd
df = pd.read_csv('/Users/mitchellsparks/Downloads/finaltrackman.csv')
df.head()
### MOVE EVERYTHING UNDER THIS LINE INTO THE NEXT CELL BELOW; YOUR FIRST CELL SHOULD JUST BE SETTING UP IMPORTS AND DF_COPY






# %%
pd.read_csv('/Users/mitchellsparks/Downloads/finaltrackman.csv', sep=';')
df = pd.read_csv('/Users/mitchellsparks/Downloads/finaltrackman.csv', skiprows=1)
# This changed the rows to get the actual ones I needed at the top 
print(df.columns)


# %%
df = df[[ 'Pitcher', 'TaggedPitchType', 'PitcherThrows', 'SpinRate']]
#made a smaller df of the certain categories I needed 
df.index = df.index.astype(str).str.upper() # turned all columns uppercase
df = df.rename(columns={'TaggedPitchType' : 'TaggedPitchAs', 'PitcherThrows' : 'PitcherHand'}) # renamed a few columns 
df.head()


# %%
df['SpinRate'] = pd.to_numeric(df['SpinRate'], errors='coerce') # to make sure spin rate came across as numeric 
df['Pitcher'] = df['Pitcher'].astype('category') # to make sure that pitcher came across as a category 
df['TaggedPitchAs'] = df['TaggedPitchAs'].astype('category') 
df['PitcherHand'] = df['PitcherHand'].astype('category')
df.head()

# %%
mean_df = df.select_dtypes(include=['float64', 'int64']).mean() # Get the mean for the spin rate 
print("Mean:\n", mean_df)
median_df = df.select_dtypes(include=['float64', 'int64']).median() # to get the median for spin rate 
print("\nMedian:\n", median_df)
mode_df = df.mode().iloc[0]  # find mode for spin rate 
print("\nMode:\n", mode_df)
range_df = df.select_dtypes(include=['float64', 'int64']).max() - df.select_dtypes(include=['float64', 'int64']).min() # Find the range of spin rate 
print("Range:\n", range_df)
std_dev_df = df.select_dtypes(include=['float64', 'int64']).std() # find standard deviation for spin rate 
print("\nStandard Deviation:\n", std_dev_df)


# %%
average_spin_rate = df['SpinRate'].mean()
print("Average Spin Rate:", average_spin_rate)   # finding average an highest spin rate 
highest_spin_rate = df['SpinRate'].max()
print("Highest Spin Rate:", highest_spin_rate)

# %%
import matplotlib.pyplot as plt

plt.hist(df['SpinRate'].dropna(), bins=30, edgecolor='black')  # dropna() to exclude NaN values

plt.title('Histogram of Spin Rates')
plt.xlabel('Spin Rate')
plt.ylabel('Frequency')

plt.show()

# %% [markdown]
# ### Lesson 5.5: Final Project - Part 2
# 
# Summary: This lesson is the second part of your final project. In this assignment, you will focus on analyzing, grouping, and visualizing your preprocessed pitching data to uncover deeper insights.
# 
# Key Concepts:
# - Analyzing and grouping data using pandas
# - Visualizing data with matplotlib
# 
# **The link to your assignment is [here](https://chat.openai.com/share/f22706e8-3f48-4032-8e1b-a476123f9507)**
# 
# Assignment:
# 1. Analyzing the Data
#     - Dive deeper into the data to uncover trends or insights. Here are a few suggestions:
#         - Analyze the relationships between variables. For instance, is there a correlation between velocity and spin rate? How does the result of the pitch change with different pitch types?
#         - Group the data by certain variables and calculate summary statistics for these groups. For example, group by "pitch type" and calculate the average "velocity" and "spin rate" for each type.
# 2. Visualizing the Data
#     - Use matplotlib to create detailed visualizations of your insights. This could include scatter plots to show relationships between variables, or grouped bar plots to compare summary statistics across different pitch types.
#     - Remember to label your plots with titles, x and y axis labels, and legends where necessary.

# %%
import os
import pandas as pd
df = pd.read_csv('/Users/mitchellsparks/Downloads/finaltrackman.csv') #imported and created df 
df.head()

# %%
pd.read_csv('/Users/mitchellsparks/Downloads/finaltrackman.csv', sep=';')
df = pd.read_csv('/Users/mitchellsparks/Downloads/finaltrackman.csv', skiprows=1)
# needed tp set up the columns the right way again to get eveything to work
correlation = df['RelSpeed'].corr(df['SpinRate']) # to find the correlation between the speed and spin rate
print("Correlation between RelSpeed and SpinRate:", correlation)


# %%
import matplotlib.pyplot as plt

plt.scatter(df['RelSpeed'], df['SpinRate']) #start to create scatte plot of 2 variables 
plt.title('Scatter plot of RelSpeed and SpinRate') 
plt.xlabel('RelSpeed')
plt.ylabel('SpinRate')
plt.show()

# %%
df['TaggedPitchType'] = df['TaggedPitchType'].astype('category') # making sure pitch type is categorized so I get all the Pitches


average_values = df.groupby('TaggedPitchType')[['RelSpeed', 'SpinRate']].mean() # finding the average speed and spin for each type of pitch 

print(average_values)


# %%
import seaborn as sns # imported to help with the graph interface and categorizing everything 
import matplotlib.pyplot as plt # to create the graph 

sns.scatterplot(data=df, x='RelSpeed', y='SpinRate', hue='TaggedPitchType') # basics for the scatter plot
plt.title('Scatter plot of RelSpeed vs SpinRate for each TaggedPitchType') # 
plt.xlabel('RelSpeed')
plt.ylabel('SpinRate')


