# Query Processing

SnowflakeDB uses one or more virtual data warehouses to process query workloads.  Properly configuring these VWHs is key to TCO. Considerations include the following:  

- Optimizing for SQL Query workloads
- Using SQL UDFs - [link to example](https://docs.snowflake.com/en/sql-reference/udf-overview.html#overloading-function-names) 
- Useing SQL Stored Procs - [when to use StoredProc vs UDF](https://docs.snowflake.com/en/sql-reference/stored-procedures-overview.html)
- Using tools, such as caching and others
- Scenario: Understand and Optimize SQL Queries

## Query Links

- Article: Top 3 Query Performance improvement Tips - https://medium.com/@jryan999/top-3-snowflake-performance-tuning-tactics-894c573731d2
- Article: SnowflakeDB data types explained - https://hevodata.com/learn/snowflake-data-types/
- 5 hours YouTube playlist - SQL context functions for SnowflakeDB - https://www.youtube.com/playlist?list=PLba2xJ7yxHB6LbOdzpqRB0WQE7IPWbbSy

# Virtual Warehouse Links

- Warehouse Considerations - https://docs.snowflake.com/en/user-guide/warehouses-considerations.html
- Tool: Snoptimizer, evaluates virtual warehouse usage patterns - https://snowflakesolutions.net/what-is-snoptimizer/
- YouTube playlist - see session #10 on using VWH - https://www.youtube.com/playlist?list=PLba2xJ7yxHB7SWc4Sm-Sp3uGN74ulI4pS
