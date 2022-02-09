from matplotlib import pyplot as plt
import seaborn as sns
import urllib.request
import json
import pandas as pd

web_res = urllib.request.urlopen("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json")
json_res = json.loads(web_res.read().decode('utf-8'))

pokedex = [ [el['id']
            , el['name']['english']
            , el['type']
            , el['base']['HP']
            , el['base']['Attack']
            , el['base']['Defense']
            , el['base']['Sp. Attack']
            , el['base']['Sp. Defense']
            , el['base']['Speed'] ] for el in json_res]
pokedex_df = pd.DataFrame(pokedex, columns=['id', 'name', 'type', 'HP', 'Attack', 'Defense', 'Sp. Attack', 'Sp. Defense', 'Speed'])
# drop column type
pokedex_main = pokedex_df.drop(columns=['type'])
pokedex_type = pokedex_df[['id', 'type']].explode('type')
# join pokedex_type and pokedex_main on id
pokedex_join = pokedex_main.merge(pokedex_type, on='id')

sns.set_theme(style="ticks", palette="pastel")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="type", y="HP", palette=["m", "g"],
            data=pokedex_join)
sns.despine(offset=10, trim=True)
plt.show()

sns.scatterplot(x="type", y="Attack",
                sizes=(1, 8), linewidth=0,
                data=pokedex_join)
plt.show()

sns.violinplot(data=pokedex_join, x="type", y="Attack", palette="Set3", bw=.2, cut=1, linewidth=1)
plt.show()
