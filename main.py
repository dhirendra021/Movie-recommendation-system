import pandas as pd

movies = pd.read_csv("datasetmovies/movie.csv")
ratings = pd.read_csv("datasetmovies/rating.csv")

# #print(movies.head())
# #print(ratings.head())

# #print(movies.columns)            # print all columns
# #print(ratings.columns)


                        #make a matrix of userID, matrixId, ratings

    #METHOD 1 (use on jupyter)
# final_datasetmovies = ratings.pivot(index="movieId", columns="userId", values="rating")
# print(final_datasetmovies.head())


    #METHOD 2
#keep users with at least 50 ratings
# user_counts = ratings["userId"].value_counts()
# active_users = user_counts[user_counts >= 50].index
# ratings = ratings[ratings["userId"].isin(active_users)]
#
# # keep movies with at least 50 ratings
# movie_counts = ratings["movieId"].value_counts()
# popular_movies = movie_counts[movie_counts >= 50].index
# ratings = ratings[ratings["movieId"].isin(popular_movies)]
#
# final_datasetmovies = ratings.pivot_table(
#     index="movieId",
#     columns="userId",
#     values="rating"
# )
# print(final_datasetmovies.head())

                #convert naN to 0 in datasetmovies
# final_datasetmovies = final_datasetmovies.fillna(0)
# print(final_datasetmovies.head())


               ##Colaborative filtering use hear ##

                #removing noise from datasetmovies

no_user_voted = ratings.groupby("userId")['rating'].agg('count')            #lest take example- im watching a action movies like Action Hero, i'm watching 20 max to max movies in 1 year, and i gave rating to all movies like 30 ratings
no_movies_voted = ratings.groupby("movieId")['rating'].agg('count')             #same way one of my friend watch 150 movies in a year, and gave 100 ratings so
#                                                                                     #what i mean to say that is- no of vote for that movei and how many users alike me vote for movies
#
# print(no_user_voted)
# print(no_movies_voted)



            #This use to virtualize on graph using scatter plot(al explanation in folder inside sem 4)

import matplotlib.pyplot as plt

plt.style.use("ggplot")
fig, axes = plt.subplots(1,1, figsize=(16,4))

        #scatter plot graph
plt.scatter(no_user_voted.index, no_user_voted, color="hotpink")
plt.axhline(y=10, color='green')

plt.xlabel("movieId")
plt.ylabel("No of users voted")

plt.show()

        #bar graph
# plt.bar(no_user_voted.index, no_user_voted)
# plt.xlabel("movieId")
# plt.ylabel("No of users voted")
# plt.show()

        #Line graph
# plt.plot(no_user_voted.index, no_user_voted)
# plt.xlabel("movieId")
# plt.ylabel("No of users voted")
# plt.show()

        #Histogram
# plt.hist(no_user_voted, bins=30)
# plt.xlabel("movieId")
# plt.ylabel("No of users voted")
# plt.show()

        #Show two graphs together
# fig, axes = plt.subplots(1, 2, figsize=(14,5))
#
# axes[0].scatter(no_user_voted.index, no_user_voted)
# axes[0].set_title("User Ratings")
# plt.ylabel("No of users voted")
# plt.xlabel("movieId")
#
# axes[1].scatter(no_movies_voted.index, no_movies_voted)
# axes[1].set_title("Movie Ratings")
# plt.ylabel("No of movies voted")
# plt.xlabel("userId")
#
# plt.show()









            #simple basic methods

#print(movies.head(10))        # stating 10 rows includes 0
#print(ratings.head(10))
#print(movies.info())         # data type int, float ..etc
#print(movies.describe())      # standard derivation like mean values, mini values, count, max...etc
#print(movies.isnull().sum())         # chechking null value or not in our dataset



# feature selection engineering part, First we take main columns we want for feature engineering (id, title, genres, imbd_ratings, cast, tagline, original language, revenue, status)

#movies=data[['id','title','status','genres','revenue','original_language','tagline','cast','imdb_rating']]
#print(movies.columns)       #print all selected feature engineering columns
#print(movies.head(10))