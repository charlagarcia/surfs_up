# surfs_up

### Purpose
A client wants to open a "Surf N Shake" shop in Hawaii, but needs investor backing.  A potential investor likes the idea, but is concerned about the weather after a previous investment shop was rained out of existance.  We are running weather analytics on Oahu for this client, so the potential investor can make an informed decision.

### Overview
1. Explain the structures, interactions, and types of data of a provided dataset.
2. Differentiate between SQLite and PostgreSQL databases.
3. Use SQLAlchemy to connect to and query a SQLite database.
4. Use statistics like minimum, maximum, and average to analyze data.
5. Design a Flask application using data.

## Summary
### Results
- The average temperature for June is 75 degrees, with low of 64, and a high of 85.

![jun_temp](https://github.com/charlagarcia/surfs_up/blob/main/June%20Temps.png)

- The average temperature for December is 71 degrees, with a low of 56, and a high of 83.

![dec_temp](https://github.com/charlagarcia/surfs_up/blob/main/December%20Temps.png)

- The temperature seems to be similar year-round, without many major discrepencies.

### Suggestions
- The client did not ask for precipitation stats for June or December, but I ran those numbers anyway.
- The average rainfall for June is .14", and .22" for December.

![junerain](https://github.com/charlagarcia/surfs_up/blob/main/Screenshot%20(58).png) ![decrain](https://github.com/charlagarcia/surfs_up/blob/main/Screenshot%20(59).png)

- I would suggest running an analysis of the average NUMBER of rainy days per year rather than the average inches.
- Since misty weather or sprinkles are unlikely to affect the store's busioness, another way to analyze the data would be to find out how many days per year have rainfall of 1" or more.
