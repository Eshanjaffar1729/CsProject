<h1 align="center"><u> Stock Trend Predictor</u></h1>

<h2>INTRODUCTION</h2>
<ul>
<li>Stock Trend Predictor is python program that utilizes data in a MySQL table to predict the general Stock Trend using moving averages
<li>The project is helpful for both long term and short-term investors for analyzing a stock before investing in it
<li>The Stock Trend Predictor in this project is based on the indicator moving averages, but the program can be modified to plot other indicators.
</ul>
## FUNCTION
*	It works on the basic principle of moving averages and uses python to handle the mathematics behind the same.
*	The python script will first read into the MySQL data base and store the Price of the stock for past n days in a list Y and the day number in another list X
*	Our predictions for a particular day will be the mean of the price of the stock on previous k days and these values will be stored in another list Y1.
*	We will plot Y and Y1 on y-axis and X on x-axis using the matplotlib library

## SOFTWARE REQUIREMENTS
*	Python 3
*	MySQL
*	Windows/mac OS/Linux
