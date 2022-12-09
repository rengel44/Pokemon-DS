# Data Science - Pokemon Analysis
## Introduction
My goal for this project was to analyze and visualize different information within the Pokemon games. I have played Pokemon for many years, and at one point I was playing in local and state competitions. What I wanted to see was the type descrpencies in the Pokemon games today, and how some types have 'better' stats over its counters. I also wanted to use Machine Learning to have my model be able to predict legendary Pokemon off of stats.

## Selection of Data
The data I selected was from Kaggle which can be found [here](https://www.kaggle.com/datasets/maca11/all-pokemon-dataset).

This data set has every Pokemon up until Calyrex Shadow Rider, the last Pokemon to be added in the previous generation. This data set includes regular pokemon, mega evolutions, legendary, and mythical pokemon. I originally wanted to add in the newest Pokemon, however, the games came out after I had started to work on this, and there was a lack of data on the 100+ newly added Pokemon.

Data preview:

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/data%20preview.PNG">

There are a lot of columns that are not needed, such as Ability, BMI, and Experience type. I selected only the columns that I needed, because there were far more that I didn't need.

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/cleaning%20it%20up%20a%20bit.PNG">
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/cleaned.PNG">

### Typings

Because some Pokemon have two types, a primary and a secondary, there were 2 columns for type. I wanted to graph how many Pokemon of each type there were, if I just counted the total Pokemon per type based off of one column, it would give me incorrect data. I used `.value_counts()` on the two type columns and added them together to get the total amount of Pokemon per type.

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/count%20type.PNG">
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/count%20results.PNG">

### Legendary

Next, I wanted to seperate the Legandary Pokemon from the Non-Legendary Pokemon. In this data set, Legendary Pokemon and Mythical Pokemon are counted as the same. Some people will say they are different, but I am not one of those people. The data set identifies if a Pokemon is Legendary with a 0 meaning Non-Legendary and 1 meaning Legendary. This is confusing, so I changed the data type using `.astype(bool)`. Then, I replaced True and False with Legendary and Non-Legendary using `.replace()`

<img src="https://github.com/rengel44/Pokemon-DS/blob/main/legendary%20count.PNG">
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/legendary%20counted.PNG">

## Methods
Tools:
* NumPy, Pandas, Scikit-Learn
*  VS Code

Materials:

## Results

With my data, I started to make graphs and charts. First, I made a pie chart showing the type distribution between all Pokemon.
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/type%20distribution.png">

Then, I made a histogram of six main stats for all Pokemon. These stats are HP, Attack, Defense, Special Attack, Special Defense, and Speed.
<img src="https://github.com/rengel44/Pokemon-DS/blob/main/all%20pokemon%20stats%20historgram.png">

I wanted to then compare the stats for different 
