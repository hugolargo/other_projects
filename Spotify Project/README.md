### Spotify Project Process

This document details the various steps I undertook while working on the project, from data import and cleaning to visual analysis. Check out the Jupyter Notebooks to see the code.

# 1. Exploring the dataset + general data cleaning

- cleaning the artists column from special characters
- changing and renaming the duration column from seconds to minutes
- checking the datatypes, changing date column to datetime type, extracting month and year as new columns
- turning country column into ISO-3 country codes for map plotting
- filtering data and creating separate data frames for global and national charts
- exploring the data for specific genres, artists, chart positions
- joining the data with my own listening history: how does my taste match with the Spotify charts?

# 2. Analyzing most popular songs & artists

- aggregating the songs with most streams worldwide
- finding the most popular artists for each country
- saving data frame to csv file
- plotting data to world map with plotly express


# 3. General Analysis - Evolution of Artist and Genre over the years

- filtering for Drake and aggregating streaming numbers for each year
- filtering and aggregating streaming numbers for different genres per year to see changes in popularity


# 4. Pulling release dates from Spotify API

- extracting unique trackIDs from global charts data frame into a list, then creating 6 id_sets with 1000 track_ids each
- installing spotipy library to connect with the Spotify API
- building loops which fetch 1 release date per second in order to stay within the request limit of the API
- repeat for each id_set, save the release dates in lists
- concatenate release_date_lists, create a new data frame and map track_ids to release_dates, save data frame to csv
- merge release_dates_dataframe with general dataframe on track_id


# 5. Release Dates - Data Wrangling and exploratory analysis

- sorting data by release date, changing datatype to datetime 
- extracting release year as separate column, renaming columns
- filtering for songs released before 2010 - my broad definition of „old“ songs
- fetching the unique artists in the dataset, sorting by release year, aggregating for artist and song titles
- creating plotly scatterplot to see old songs entering the Spotify charts
- obvious first result: most songs are Christmas songs
- next step: filtering out Christmas songs: songs that did not chart in November or December, no „Christmas“ or „Snow“ in title
- plotting the chart performance of „Running up that Hill“


# 6. Old vs. new songs - Further analysis and statistics

- once more exploring the statistics of old vs. new songs and the proportion of Christmas songs
- trying to find special songs and chart appearances, patterns and explanations
- finding out which songs made the most weekly streams ever


# Final analysis and visualization took place in Tableau. Have a look at the plot folder or final presentation slides for the results.