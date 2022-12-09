# Data Science - Pokemon Analysis
## Introduction
My goal for this project was to analyze and visualize different information within the Pokemon games. I have played Pokemon for many years, and at one point I was playing in local and state competitions. What I wanted to see was the type descrpencies in the Pokemon games today, and how some types have 'better' stats over its counters. I also wanted to use machine learning to use this dataset to predict if a Pokemon was Legendary or Non-Legendary based off of stats.

## Selection of Data
The data I selected was from Kaggle which can be found [here](https://www.kaggle.com/datasets/maca11/all-pokemon-dataset).

This data set has every Pokemon up until Calyrex Shadow Rider, the last Pokemon to be added in the previous generation. This data set includes regular pokemon, mega evolutions, legendary, and mythical pokemon. I originally wanted to add in the newest Pokemon, however, the games came out after I had started to work on this, and there was a lack of data on the 100+ newly added Pokemon.

Data preview:

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/data%20preview.PNG">

There are a lot of columns that are not needed, such as Ability, BMI, and Experience type. I selected only the columns that I needed, because there were far more that I didn't need. I also change the NaN values to 'None' for any Pokemon that did not have a secondary typing using `.fillna("None")`

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/cleaning%20it%20up%20a%20bit.PNG">
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/cleaned.PNG">

Every Pokemon has at least one typing, but some have two. The data set has two different columns for type to reflect this, Type 1 and Type 2. To get the total number of Pokemon per type, I added these two columns together and counted them using `.value_counts()`
 
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/count%20type.PNG">

Every Pokemon can also be categorized into Legendary or Non-Legendary. Legendary Pokemon can only be encountered and caught once, while most Non-Legendary Pokemon can be encountered and caught as long as you have enough space for them. In this data set, this distinction is made by Legendaries have the value of `1.0` and Non-Legendaries have the value of `0.0`.

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/horsea.PNG">
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/mew.PNG">
 
I used Random Forest Classifier for the Machine Learning portion. The reason why I chose this was because it could take inputs to predict a result. Random forest can combine lots of trees for an even more accurate result. There are over 1000 Pokemon in this data set. My features were the six columns that had the stats of all Pokemon, HP, attack, defense, special attack, special defense, and speed. My label was the Legendary column. I used a train/test split of 70% training and 30% test.

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/test%20and%20train.PNG">
  
## Methods
### Tools used
* NumPy, Pandas, Seaborn, Matplotlib, and SciKit
* VS Code
* Random Forest Classifier

### Resources
* Datacamp and Oracle blogs
* My frinds and innanimate objects who listened to me try to explain what I was doing
* Bulbapedia for Pokemon related information

## Results
### Graphs
The first thing I did was make graphs to visualize the data I was going to be using. What I wanted to first see was if my hypothesis of type descrepencies was true. With the results from `.value_counts()`. I gathered the totals and turned it into a pie chart to show the distribution of types.

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/type%20distribution%20code.PNG">
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/type%20distribution.png">

Ice had the type with the least amount of Pokemon. While Water had the most.

I wanted to see if there was a correlation between stats. Using Seaborn, I created a heatmap.
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/heatmap%20code.PNG">
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/heatmap%20of%20stats.png">
  
To see if stats were distrubuted  equally across all Pokemon. I created a histogram of all Pokemon stats to show this. 
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/histogram%20code.PNG">
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/all%20stats%20hist.png">
  
Next, I created another histogram of just Legendary Pokemon.
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/legendary%20hist.png">

I wanted to compare the stats between Ice type and what it is weak to. Ice has 4 weaknesses: Fighting, Fire, Rock, Steel.  Using a scatterplot, I compared the Attack and Defense stats of the five typings.
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/scatter%20plot%20code%201.PNG">
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/ice%20stats.png">

  
Then, I wanted to compare the stats between Water abd what it is weak to. Water has only 2 weaknesses: Grass and Electric. Again, I used a scatterplot to compare these.

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/water%20stats.png">

Next, I used this same comparsion to compare Legendary vs Non-Legendary stats.

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/legendary%20stats.png">
 
### Random Forest Results
 
After training, the model had an accuracy of around 91-93%. For my first time working with something like this, I think that is pretty good. To put this to use, I created a user input into the console that after a user inputs six different stats, it will tell you if your Pokemon is Legendary or Non-Legendary.

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/accuracy.PNG">

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/user%20input%20code.PNG">

I tested this by using some example Pokemon. I entered the stats of Mewtwo (Legendary), Meowth (Non-Legendary), Salamence (Non-Legendary), and Xurkitree (Legendary).
Mewtwo:

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/mewtwo.PNG">
Meowth:

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/Meowth.PNG">
Salamence:

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/salamence.PNG">
Xurkitree:

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/xurkitree.PNG">

## Discussion
  
Looking at the heatmap showed that there was no correlation between most stats. If I wanted to check correlation with stats, I could look at the weight of a pokemon vs its stats. Maybe heavier Pokemon have higher HP or higher Defense?
 
The histograms show that most stats are evenly distrubted across all Pokemon. The histogram of Legendary stats shows almost the same, but they tend to have more uneven dsitrbution in the HP, Defense, and Special Defense stats. A Pokemon with more HP and higher defenses is more difficult to beat. 
  
The scatter plots are interesting. Historically, Ice type Pokemon have been the least used. This is because they have poor stats, and a lot of weaknesses. The scatterplot shows that compared to its weaknesses, it is still very weak. These types would be less than ideal to use in competitive play due to this. 

The scatter plot of Water vs its weaknesses is also interesting. I had assumed that because there were so many Water types, it would have subpar stats. However, comparing the stats to its weaknesses shows that they are about equal. This would make water more difficult to counter.

Legendary Pokemon had higher stats compared to Non Legendary Pokemon. Legendary Pokemon may be better stat wise, which would mean that in a game they would be more sought out and used. But, typings play a major roll in Pokemon. Although a Pokemon may have good stats, if its typing is poor, it could have weaknesses that outweight its stats.
  
## Summary
  
I believe the most important findings are the type distribution as well as the stats of Legendaries. There is a stark difference in the stats from Non-Legendary and Legendary Pokemon. This can cause in unfair advantage in the game. If someone has a team of all Legendary Pokemon, they may be more difficult to beat. But, the point of the game is to win. So who wouldn't want to use stats to their advantage? I believe the typing distribution is importnat as well, because it shows that even if there is a small number of a certain type of Pokemon, it does not mean they have less weaknesses. Before this project, I had assumed that Water typing was weak and not viable in completitive play.
  
Although I had struggled with this project, I am happy with the results and I am even more informed about the game than before.
