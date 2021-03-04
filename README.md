

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
2. Create a new folder that will contain this python file and an empty excel file name "cryptos.csv" MAKE SURE IT IS SAVED AS CSV!
3. Open vscode and hit open workspace and open the folder with this file and the csv file
4. Open terminal within vscode (google this if you cant figure it out)
5. Type python3 crypto.py into the command line in the terminal, hit enter
6. Now the csv should contain values and the program should have ran if you get errors just send them to me Ill show you how to fix it 


## Changing the Coins 
Each URL has specific parameters within the line. The 'KEY=' section is the API key I received do not change that AT ALL.

The 'ids=' is the Coin ids so whatever the short form of the coins is that is the id ex. BTC, ETH etc ONE does not work!!!
In order to add more coins add a comma and then add the id DO NOT ADD AN & symbol it will break example below 
To pull bitcoin and etherium it will be ids=BTC,ETH for just bitcoin it is ids=BTC
There are more parameters but these are the ones you care about. 

Check the Nomics API documentation website and go to the currencies tab if you want to learn on your own and see the other query parameters. 

## Machine Learning Algorithm


