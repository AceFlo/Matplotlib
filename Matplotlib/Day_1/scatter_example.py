from matplotlib import pyplot as plt
import pandas as pd
plt.style.use("_classic_test_patch")
data = pd.read_csv("2019-05-31-data.csv")
views = data["view_count"]
likes = data["likes"]
ratio = data["ratio"]
plt.scatter(views, likes, c=ratio, cmap="summer")
color = plt.colorbar()
color.set_label("like/dislike ratio")
plt.xlabel("Views")
plt.ylabel("Likes")
plt.title("Youtube trending videos")
plt.xscale("log")
plt.yscale("log")
plt.tight_layout()
plt.grid()
plt.show()
