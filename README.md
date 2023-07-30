# Real-Estate-Appraiser

Real Estate Appraiser is an application that will help you value an apartment based on the number of rooms and area in the city of Bielsko-Biała.

File `main.py` serves as a script to scrape current data about flats in Bielsko-Biała. It takes data like area, number of rooms, floor, and price. As the scraping has been done, the data is stored in a file `estates.csv`.

After this process, we are importing `estates.csv` to our file `main.ipynb` in which we have a model that will learn from our `estates.csv`. Data is imported, read, and modified in the Pandas library in order to get a valuation. The model is based on Sklearn, and it learns based on linear regression, which is the most accurate algorithm in this case.

$\textcolor{red}{\textsf{The accuracy of the application is not the best. Accuracy depends on the quality of the data, which is not ideal in our case }}$
$\textcolor{red}{\textsf{because of what the website offers. What I mean is that the website doesn't create separate information about what year the }}$
$\textcolor{red}{\textsf{flat is, what the standard is, etc. The site focuses on descriptions of people who offer flats, like a lot of other sites, }}$ 
$\textcolor{red}{\textsf{which makes the valuation task much more difficult. The most accurate valuation that can be obtained is in the case of valuing }}$ 
$\textcolor{red}{\textsf{a flat that is of medium standard. }}$ 
