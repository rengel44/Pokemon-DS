import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import warnings

#reading the data
pkm = pd.read_csv('All_Pokemon.csv')

#cleaning it up a bit
pkm = pkm[['Name', 'Type 1', 'Type 2', 'HP', 'Att', 'Def', 'Spa', 'Spd', 'Spe', 'Legendary']]
pkm = pkm.fillna("None")


#Testing and training the data
x=pkm[['HP', 'Att', 'Def', 'Spa', 'Spd', 'Spe']]
y=pkm['Legendary']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(x_train,y_train)
ypred=clf.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, ypred))

#gets rid of the warning, I am unsure what causes the error. But the predictions are accurate
warnings.filterwarnings(action='ignore', category=UserWarning)

#Counting the pokemon typings
tone =pkm['Type 1'].value_counts() 
ttwo = pkm['Type 2'].value_counts()
types = tone + ttwo
print((types).sort_values(ascending=False))

#creating the pie chart of the distribution of typings
labels = 'Water', 'Normal', 'Flying', 'Psychic', 'Grass', 'Bug', 'Fire', 'Ground', 'Poison','Rock','Fighting', 'Dark', 'Dragon', 'Steel', 'Electric', 'Ghost', 'Fairy', 'Ice'
sizes = [151,124,120,119,119,90,81,80,77,74,73,72,72,71,70,68,63,56]
colors = ['#6390F0', '#A8A77A', '#A98FF3', '#F95587', '#7AC74C', '#A6B91A', '#EE8130', '#E2BF65', '#A33EA1', '#B6A136', '#C22E28', '#705746', '#6F35FC', '#B7B7CE', '#F7D02C', '#735797', '#D685AD', '#96D9D6']
plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', shadow=False)
plt.axis('equal')
plt.title('Distribution of Pokemon typings')
plt.plot()
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.show()

#showing heatmap of all pokemon stats
stats = pkm[['HP', 'Att', 'Def', 'Spa', 'Spd', 'Spe']]
sns.heatmap(stats.corr(), linewidths=1, vmax=1, square=True, annot=True)
plt.title('Heatmap correlation of all Pokemon types')
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.plot()
plt.show()

#hist of all pokemon stats
pkm.hist(color='lightblue', ec='black')
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.plot()
plt.show()

#Scatter plot of Fairy vs Steel stats
ice = pkm[(pkm['Type 1'] =='Ice') | ((pkm['Type 2'] == 'Ice'))]
steel = pkm[(pkm['Type 1'] =='Steel') | ((pkm['Type 2'] =='Steel'))]
fight = pkm[(pkm['Type 1'] =='Fighting') | ((pkm['Type 2'] =='Fighting'))]
rock = pkm[(pkm['Type 1'] =='Rock') | ((pkm['Type 2'] =='Rock'))]
fire = pkm[(pkm['Type 1'] =='Fire') | ((pkm['Type 2'] =='Fire'))]
plt.scatter(ice.Att.head(20), ice.Def.head(20), color = '#96D9D6',label = 'Ice', marker='s')
plt.scatter(steel.Att.head(20), steel.Def.head(20), color = '#B7B7CE', label='Steel', marker='o')
plt.scatter(fight.Att.head(20), fight.Def.head(20), color = '#B6A136', label='Fighting', marker='D')
plt.scatter(rock.Att.head(20), rock.Def.head(20), color = '#A33EA1', label='Rock', marker='p')
plt.scatter(fire.Att.head(20), fire.Def.head(20), color = '#A6B91A', label='Fire', marker='^')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.legend()
plt.title('Super Effective Against Ice vs Ice Stats')
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.plot()
plt.show()

#scatter plot of Water vs Electric
water = pkm[(pkm['Type 1'] =='Water') | ((pkm['Type 2'] == 'Water'))]
elec = pkm[(pkm['Type 1'] =='Electric') | ((pkm['Type 2'] =='Electric'))]
grass = pkm[(pkm['Type 1'] =='Grass') | ((pkm['Type 2'] =='Grass'))]
plt.scatter(water.Att.head(20), water.Def.head(20), color = '#6390F0',label = 'Water', marker='s')
plt.scatter(elec.Att.head(20), elec.Def.head(20), color = '#F7D02C', label='Electric', marker='o')
plt.scatter(grass.Att.head(20), grass.Def.head(20), color = '#7AC74C', label='Grass', marker='p')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.legend()
plt.title('Water vs Electric Stats')
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.plot()
plt.show()

#showing stats of Legendary vs non
leg = pkm[(pkm['Legendary']==1.0)]
nleg = pkm[(pkm['Legendary']==0.0)]
plt.scatter(leg.Att.head(20), leg.Def.head(20), color = '#FFD700',label = 'Legendary', marker='s')
plt.scatter(nleg.Att.head(20), nleg.Def.head(20), color = '#C0C0C0', label='Non-Legendary', marker='o')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.legend()
plt.title('Legendary vs Non-Legendary Stats')
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.plot()
plt.show()


#showing the distribution of stats with legendaries via hist
lgd = pkm[pkm['Legendary']==1.0]
lgd.hist(color='lightblue', ec='black')
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.plot()
plt.show()

#user input to test
while True:
    try:
        test_HP = input('Enter Pokemon HP\n')
        test_Att = input('Enter Pokemon Attack\n')
        test_Def = input('Enter Pokemon Defense\n')
        test_SPA = input('Enter Pokemon Special Attack\n')
        test_SPD = input('Enter Pokemon Special Defense\n')
        test_SPE = input('Enter Pokemon Speed\n')
        result = clf.predict([[test_HP,test_Att,test_Def,test_SPA,test_SPD,test_SPE]])
    except:
        print('Please enter numerical values only')
        continue
    if result == [1.]:
        print('Your Pokemon is a Legendary')
    else:
        print('Your Pokemon is a Non-Legendary')
    print('Would you like to test another Pokemon? (Y/N)')
    cont = input()
    if cont == "N" or cont == "n":
        break