# Guess-the-Correlation-Bot

## About

The code in this repository is a simple bot for the web game [Guess the Correlation](http://guessthecorrelation.com/), which I built to help a friend get extra credit in his statistics class.

The bot works by scanning the screen for the points, adding their coordinates to a list, fitting a model to the list of coordinates, and then calculating the r-squared value.

## Requirements

pyautogui, and scipy

## How to Run

The code is run through the command line, like so:

```python GuessCorrelationBot.py <num iterations> <topleft x-coordinate> <topleft y-coordinate> <bottomright x-coordinate>     <bottomright y-coordinate> -get_coords <True|False>
```

  * __num iterations__ - How many times you want the code to loop for (integer)
  * __topleft x-coordinate__ - Top Left x-coordinate of gameboard
  * __topleft y-coordinate__ - Top Left y-coordinate of gameboard
  * __bottomright x-coordinate__ - Bottom Right x-coordinate of gameboard
  * __bottomright x-coordinate__ - Bottom Right y-coordinate of gameboard
  * __-get_coords__ - optional argument for getting coordinates on the screen, if set to True code doesn't run and instead coordinates of current mouse location is output to console instead
  
For a simple demonstration of how to run the code, look to the youtube video below.
  

## Demonstration

The following is a demonstration of the bot running for 10 iterations.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=mTJd5CriBSk
" target="_blank"><img src="http://img.youtube.com/vi/mTJd5CriBSk/0.jpg" 
alt="Click Here for Video Demonstration" width="240" height="180" border="10" /></a>
