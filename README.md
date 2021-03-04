

## Crypto Machine Learning and Data Curation
### Table of Contents
  * [Description](#description)
  * [How to Run](#how-to-run)
  * [Changing the Coins](#changing-the-coins)
  * [Machine Learning Algorithm](#machine-learning-algorithm)

## Description

Every single timeframe can have a corresponding dataframe if you want others lmk. The main one that is being outputted is the 1 day dataframe.
If you want to change that I can show you how to do that its simple. 
Each coin has a timestamp for when it is updated at 0:00 hours on that days beginning.

Deeper project description tbd blah blah super interesting project so fun loved it blah 

## How to Run
1. Download a text editor, vscode is probably the best one(you shouldnt have to download python if you get vscode)
2. Download Github desktop
3. When on the main page of the repository click the green code button and hit open in github desktop
4. This will pull every single file in the repository when you clone it 
5. Open github desktop
6. Change your editor preferences to Visual Studio Code and click "open in Visual Studio Code"
7. Within the Python file open a terminal window(google how to do this if you cannot figure it out)
8. Type into the terminal window "python3 cryptos.py"
9. Now your csv file should be updated with that days data
10. If you run into errors let me know I can help you with them


## Changing the Coins 
Each URL has specific parameters within the line. The 'KEY=' section is the API key I received do not change that AT ALL.

The 'ids=' is the Coin ids so whatever the short form of the coins is that is the id ex. BTC, ETH etc ONE does not work!!!
In order to add more coins add a comma and then add the id DO NOT ADD AN & symbol it will break example below 
To pull bitcoin and etherium it will be ids=BTC,ETH for just bitcoin it is ids=BTC
There are more parameters but these are the ones you care about. 

Check the Nomics API documentation website and go to the currencies tab if you want to learn on your own and see the other query parameters. 

## Machine Learning Algorithm


