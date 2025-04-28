# 3 types of machine learning: regression, classification, recommendation
# recommendation gives us future likeable choices based on past experience
# no right/wrong, hard to find accuracy
# 3 types:
# simple - based on some score value (ex. top 10 trending)
# content - based on user's previous choices
# collaboration - grouping preferences based on shared characteristics/demographics

import pandas as pd

data = pd.read_csv("movies_metadata.csv")
print(data.head())
print(data.shape)

# weighted rating: 
    # (v / (v + m)) * r + (m / (v + m)) * c
    # v is the number of votes (vote_count)
    # m is the min. votes required to be listed in chart
    # r is the average rating for the movie (vote_average)
    # c is the mean vote across the whole report

c = data["vote_average"].mean()
print(c)

m = data["vote_count"].quantile(0.9)
print(m)

qMovies = data.copy().loc[data["vote_count"] >= m]
print(qMovies.shape)

def weightedRating(x):
    v = x["vote_count"]
    r = x["vote_average"]

    return (v/(v + m) * r) + (m / (m + v) * c)

qMovies["score"] = qMovies.apply(weightedRating, axis=1)
qMovies = qMovies.sort_values("score", ascending=False)

print(qMovies[["title", "vote_count", "vote_average", "score"]].head(20))