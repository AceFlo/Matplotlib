import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

data = pd.read_csv("data.csv")
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()
for response in lang_responses:
    language_counter.update(response.split(";"))
# print(language_counter)
languages = [item[0] for item in language_counter.most_common(15)]
popularity = [item[1] for item in language_counter.most_common(15)]
# print(languages)
# print(popularity)

plt.barh(languages, popularity)
plt.xlabel('Number of Users')
plt.title('Top 15 Most Popular Programming Languages')
plt.show()