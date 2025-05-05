import pandas as pd

data = pd.read_csv("san_francisco.txt", header=None)
data.columns = ["sessionID", "entryPoint", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15", "r16", "r17", "r18", "endPoint"]

endPointCounts = data["endPoint"].value_counts()
c = endPointCounts.mean()
m = endPointCounts.quantile(0.9)

topRestaurants = endPointCounts[endPointCounts >= m].copy()

def weightedRating(x):
    v = x
    r = 5
    return (v / (v + m) * r) + (m / (m + v) * c)

topRestaurants = topRestaurants.apply(weightedRating)
topRestaurants = topRestaurants.sort_values(ascending=False)

print(topRestaurants.head(20))