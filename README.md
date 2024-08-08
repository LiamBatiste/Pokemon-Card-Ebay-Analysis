# Pokemon-Card-Ebay-Analysis
Analysis of Pokemon Card Ebay sold listings obtained through Automated Web Scraping. 

The main Goal of this Project was to Scrape recent Ebay Sales for Listed Pokemon cards. By leveraging the scraped data and analysis process would help identify arbitrage opportunities in the Pokémon card market. The main aims were as follows:
<br></br>
#### - Identifying underpriced items 
#### - Montoring Card Sale Prices (particularly auction items)
#### - Evaluate card condition and rarity
#### - Opportunities for higher resale of cards (Auction vs Buy it Now)
<br></br>

It was important for the sales volume of the cards chosen to be high in order for the analysis to be of value.  This would ensure that the analysis would be more reliable and valid when visualised as a dashboard in Power Bi. Further, a larger dataset would be crucial for later time series analysis as the data would be more representative of the current Pokemon card market. The Pokemon card market is and has been in high demand since their release back in 1999, therefore not only are the cards in high demand but cards that meet specific criteria can sell for very high prices, which could lead to a spike in average sale prices for a particular card (so we should be mindful of this). Given the high demand this provides great oportunity to resell items quickly, but can also cause market volitility.

<br></br>
The cards chosen were the following: 
### ***Charizard 2/102 Base Set***
![image](https://github.com/user-attachments/assets/233bbe53-0ef1-48ab-bfed-f9ac46c71821)

### ***Blastoise 4/102 Base Set***
![image](https://github.com/user-attachments/assets/3391ebd4-5d6c-4f38-9bfd-a46b577eacb0)

### ***Venusaur 15/102 Base set***
![image](https://github.com/user-attachments/assets/3806d4cb-8654-4a18-b6c7-2d34aa9cbf60)
<br></br>

# The ETL Process
The transactional sales data Was Scraped from <b>Ebay.co.uk</b> using a custom Python script, utitlising specifically the Selenium Library to extract the data of interest such as BIN/Bid Sale Prices, Sale Date, Item Condition, Sale Type etc. 

The data was formatted as CSV file so it could then be brought into Power BI for transformation of data types, duplicate removal and cleansing of the sale types. 

The now transformed data was then visualised within Power BI, allowing for insight into:
#### - Card Price Trends Over Time by Card
#### - Average Card Price by Condition 
#### - Sales Volume by Card
#### - Sales Volume by Sale Type (BIN/Auction)
#### - Card Price by Location
#### - Influence of Bid Count on Average Price by Card

<br></br>

[Pokemon Card Ebay Analysis.pdf](https://github.com/user-attachments/files/16195697/Pokemon.Card.Ebay.Analysis.pdf)
![image](https://github.com/user-attachments/assets/b6b5a60d-8127-4ba0-b716-d76d65cf33b5)

# Potential Leveraging of Data-Driven Strategies

### Market Timing and Price Fluctuations:
Pokémon card prices vary based on factors such as seasonality, events, and media releases. By identifying these patterns through time series analysis, this allows for strategical purchasing of cards during low-price periods and resale during peak demand. To optimise buying and selling times for maximum profitability, it’s essential to monitor and analyse these price trends.

### Condition, Rarity, and Grading Impact:
The unqiueness of certain cards when coupled with high condition quality can command much higher prices, particularly after being graded. Therefore meaning more opportunity for acquiring high-quality cards which are 'underpriced' compared to the general market, thus leading to more opportunities to resell the cards at a premium (particularly after grading).

### Auction vs. Buy It Now (BIN) Dynamics:
Auctions can lead to lower final sale prices, especially if bidding activity is minimal, while Buy It Now (BIN) listings may be inconsistently priced relative to market value. This presents opportunities to acquire cards through auctions at a lower cost, which can then be resold at higher prices using the BIN option. Alternatively, undervalued BIN listings can be immediately capitalized on for a quick flip.

### Sales Volume and Quick Turnover:
High sales volume, particularly for iconic cards like Charizard, reflects strong and consistent market demand, facilitating quicker resales. By focusing on cards with high turnover rates, you can achieve faster sales, thereby reducing the time spent holding inventory and mitigating associated risks.

### Predictive Analysis and Long-Term Investment:
Time series analysis provides the ability to forecast future price trends, while certain cards, due to their nostalgia and rarity, possess significant long-term appreciation potential. Leveraging predictive modeling allows for strategic timing in purchasing and selling, while identifying cards with long-term investment value can help maximize financial returns over time.

# Lessons Learnt/Future Improvements
- The Process I followed is 'stepped' and requires human intervention when bringing the data into Power BI and then to transform the data so it can be visualised. To improve the ETL pipeline I could use Power Automate to automatically load the data into Power BI and trigger a data refresh each time new data is brought in, which will also update the visuals to reflect said new data. Additionally, I could use industry standard practices such as AWS along with services such as S3, Lambda, and Glue for seamless data ingestion, transformation, and querying. <b> 
Therefore it would be benefit to myself to gain a greater understanding of AWS services and possibly become AWS certified.</b>

- The data that can be extracted from Ebay with respect to condition is either 'new (other)' or 'pre-owned' and so there is lack of classification given that the condition is measured nominally. This nominal classification of condition lacks the granularity that would allow for more nuanced analysis and possibly reduced risk of buying cards that have been associated with a misleading condition. Therefore extracting specific grades (particulary PSA grading) of the listing title using text mining or natural language processing would be useful to provide more condition categories (e.g., "Mint," "Near Mint," "Good," "Fair," "Poor").
