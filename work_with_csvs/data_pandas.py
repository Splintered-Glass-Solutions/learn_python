
#%% == Imports ==
import pandas as pd
import matplotlib.pyplot as plt

# %% #==== Basic Data Operations (pandas)====
# %% #_ region[green]
# * from a csv
# pandas is a vital package that allows you to work with data in row col format. Similar to excel...ish.

# be sure to paste in the correct file path to your csv
file_name = "OLYMPICS_athlete_events"
data_df = pd.read_csv(f"{file_name}.csv")

# %% #* usefull pandas functions
data_df.head(15)
data_df.tail(15)
data_df.describe()
len(data_df)
list(data_df)
# %% #* drop duplicates
data_df.drop_duplicates(subset=['Name', 'Team', 'Event', 'Games'], inplace=True)

# %% #* drop nulls (1st Attempt from memory) THIS WILL ERROR
cleaned_df = data_df.dropna(subset='Medal')
# %% #* drop nulls (after googling pd dropna)
cleaned_df = data_df.dropna(subset=['Medal'])

# %% #* sort_values (use inplace argument. I used to have ugly code like this)
cleaned_df.sort_values(by='Year',
                       inplace=True, ascending=False)

# %% #* saving data
cleaned_df.to_csv("my_cleaned_data.csv")

# %% #* convert to list of dictionaries
data = cleaned_df.to_dict(orient='records')
data[100:103]

# %% #* indexing
cleaned_df.set_index('ID', inplace=True)
cleaned_df.loc[93091]  # lookup by the index
cleaned_df.iloc[150]  # lookup by the row number
norus_f_gold_df = cleaned_df[(cleaned_df['Medal']=='Gold') & (cleaned_df['Sex']=='F') & (cleaned_df['NOC']!='RUS')] # by values

# %% #* easy plotting wiht pandas
ax1 = cleaned_df.plot.scatter(x='Height',
                              y='Weight',
                              c='Age',
                              colormap='viridis')
# %% #* add alpha
ax1 = cleaned_df.plot.scatter(x='Height',
                              y='Weight',
                              c='Age',
                              alpha=0.05,
                              colormap='viridis')

# %% #== Time to try it yourself!

#%% #* add x tick labels
# dont peak https://stackoverflow.com/questions/43578976/pandas-missing-x-tick-labels
fig, ax = plt.subplots()
cleaned_df.plot(kind='scatter', 
                x='Height', 
                y='Weight', 
                s=10,
                c='Age', 
                cmap='viridis',
                alpha=0.1,
                ax=ax)
#%% #* make a plot that only shows males
males_df = cleaned_df[cleaned_df['Sex']=='F']
fig1, ax = plt.subplots()
males_df.plot(kind='scatter', 
                x='Height', 
                y='Weight', 
                s=10,
                c='Age', 
                cmap='viridis',
                alpha=0.1,
                ax=ax)
#%% #* make a plot that only shows males from USA
males_df = cleaned_df[(cleaned_df['Sex']=='F') & (cleaned_df['NOC']=='USA')]
fig1, ax = plt.subplots()
males_df.plot(kind='scatter', 
                x='Height', 
                y='Weight', 
                s=10,
                c='Age', 
                cmap='viridis',
                alpha=0.1,
                ax=ax)
#%% #* color the plot by medal instead of age
colors = {'Gold':'gold', 'Silver':'silver', 'Bronze':'sienna'}

fig1, ax = plt.subplots()
males_df.plot(kind='scatter', 
                x='Height', 
                y='Weight', 
                s=30,
                c=males_df['Medal'].map(colors), 
                alpha=0.25,
                ax=ax)

#%% #* get a count of the gold medals by country in a table
gold_df = cleaned_df[cleaned_df['Medal']=='Gold']
team_golds = gold_df['Team'].value_counts()

#%% #* make a bar chart out of it ^
team_golds.iloc[:10].plot.bar(x='Team', y='Value')
#%% #* save this table to 
team_golds.to_csv("gold.csv")
# %%
# _ endregion