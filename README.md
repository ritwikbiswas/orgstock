# orgstock

A virtual world with communities of digital organisms whose health is determined by the weighted alpha of high volume stocks. Statistics about the population are tweeted out using a connected API.

### Current Status
This project is connected to a Twitter api so the environment tweets out the most stable stocks to invest in based on organism performance and hierarchy. Eventually the whole system will be ported to a server and have a clean website to visualize the relationship between organisms and communities.

For now, the environment uses the 100 highest trading volume stocks to assign to each organism, but in the future it will be scraped from a database.

### Details

##### Community and World
Each world is comprised of ten communities each with ten organisms each. Each community has a certain ranking in the world corresponding to the health of the organism within. The communities have a basic heirarcy with an "alpha" organism which is the most fit organism in the community. Each organism is randomly assigned a stock. The performance of this stock determines the health of the organism over time.


##### Organisms
Each organism has five attributes:
* organsim_id (a randomly generated string of five characters functioning as its name)
* heirarcy (determining whether this organism is the alpha in its community or not)
* health (the general wellbeing of the organism, a number between 0 and 1)
* food (The stock name. The performance of this stock directly affects its health)
* social aptitude (A general indiction of the organisms tendency to interact with other, this will later be factored into the swapping process)
* old_price (a way to document the stock price change over time, this is currently unused) 

##### Organisms
Every 100 cycles, the communities exhange their best and worst organisms with each other. This way the good organisms have a way of sorting themselves to the top. A quick glance at the top community over a period of time should be the most stable organisms/stocks in the market.


Made in Python by Ritwik Biswas.
