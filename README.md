# Real-Estate-Appraiser

Real Estate Appraiser is an application that will help you value an apartment based on the number of rooms and area in the city of Bielsko-Biała. 

`main.py` serves as a script to scrape current data about flats in Bielsko-Biała.
It takes data like area, number of rooms, floor and price.
As the scraping has been done, data is storing to file `estates.csv`

After this process, we are importing `estates.csv` to our file `main.ipynb` in which we have model that will learn out of our `estates.csv`. Data is imported, read and modified in pandas library in progression to get valuation. Model is based on sklearn and it learns based on linear regression
which is the most accurate algorithm in this case.

$\textcolor{red}{\textsf{The accuracy of the application is not the best. Accuracy depends on the quality of the data, which is not ideal in our case because of what the website}}$
$\textcolor{red}{\textsf{offers. What I mean is that the website doesn't create separate information about what year the flat is, what the standard is, etc. The site focuses on}}$
$\textcolor{red}{\textsf{descriptions of people who offer flats, like a lot of other sites, which makes the valuation task much more difficult. The most accurate valuation that}}$ 
$\textcolor{red}{\textsf{can be obtained is in the case of valuing a flat that is of medium standard.}}$ 
