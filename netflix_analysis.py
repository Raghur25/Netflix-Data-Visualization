#s-1 import the libraries
import pandas as pd                  # For data loading, cleaning, and analysis
import matplotlib.pyplot as plt      # For creating visualizations 

#load the data
df = pd.read_csv('netflix_data.csv')  # Reads the CSV file into a pandas DataFrame

# Clean the data by removing rows with missing values in important columns
df = df.dropna(subset=['type','release year','rating','country','duration'])

#Count how many 'Movie' and 'TV Show' entries are in the dataset
type_counts = df['type'].value_counts()

plt.figure(figsize=(6,4))   #to set the size of the plot(6 wide, 4 tall)
plt.bar(type_counts.index, type_counts.values, color=['skyblue','Orange'])
plt.title('Number of Movies vs TV shows on netflix')
plt.xlabel('type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Content Ratings')
plt.tight_layout()
plt.savefig('content_Ratings_pie.png')
plt.show()

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie duration')
plt.xlabel('duration(minutes)')
plt.ylabel('Number of movies')
plt.tight_layout()
plt.savefig('movies_duration_histogram.png')
plt.show()

release_counts = df['release year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color='red')
plt.title('Release year vs Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('number of shows')
plt.tight_layout()
plt.savefig('release_year_Scatter.png')
plt.show()

country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 countries by number of shows')
plt.xlabel('Number of shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10_countries.png')
plt.show()

content_by_year = df.groupby(['release year','type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2, figsize=(12,5))

#first subplot:movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='Blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('year')
ax[0].set_ylabel('Number of Movies')

#second subplot:TV shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='Orange')
ax[1].set_title('TV shows released per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of Tv shows')

fig.suptitle('Comparison of Movies and TV shows Released Over Years')

plt.tight_layout()
plt.savefig('movies_Tv_shows_comparison.png')
plt.show()
