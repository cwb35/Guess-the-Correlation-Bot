# Guess-the-Correlation-Bot

## About

The code in this repository is a simple bot for the web game [Guess the Correlation](http://guessthecorrelation.com/), which I built to help a friend get extra credit in his statistics class.

The bot works by scanning the screen for the points, adding their coordinates to a list, fitting a model to the list of coordinates, calculating the r-squared value, and then outputting it to the game.

## Requirements

  * [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
  * [scipy](https://www.scipy.org/)

## How to Run

The code is run through the command line, like so:

```
python GuessCorrelationBot.py <n> <TL x-coord> <TL y-coord> <BR x-coord> <BR y-coord> -get_coords <True|False>
```

  * __n__ - How many times you want the code to loop for (integer)
  * __TL x-coordinate__ - Top Left x-coordinate of gameboard
  * __TL y-coordinate__ - Top Left y-coordinate of gameboard
  * __BR x-coordinate__ - Bottom Right x-coordinate of gameboard
  * __BR x-coordinate__ - Bottom Right y-coordinate of gameboard
  * __-get_coords__ - optional argument for getting coordinates on the screen, if set to True code doesn't run and instead coordinates of current mouse location is output to console instead
  
After running the script it sleeps for 5 seconds to give you enough time to click inside the Guess box for the game.
  
For a simple demonstration of how to run the code, look to the youtube video below.
  

## Demonstration

The following is a demonstration of the bot running for 10 iterations.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=mTJd5CriBSk
" target="_blank"><img src="http://img.youtube.com/vi/mTJd5CriBSk/0.jpg" 
alt="Click Here for Video Demonstration" width="240" height="180" border="10" /></a>
