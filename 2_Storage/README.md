# Storage and Files

SnowflakeDB includes a number of useful data import options:   
- Web UI has 100 MB file import limit
- SnowflakeDB cli (for AWS S3 and others) - example - https://docs.snowflake.com/en/user-guide/data-load-external-tutorial.html
- Snowpipe Streams - user guide - https://docs.snowflake.com/en/user-guide/data-load-snowpipe.html
- File Ingest - example loading Hacker News from @hoffa - https://medium.com/snowflake/loading-all-hacker-news-comments-into-snowflake-in-less-than-1-minute-728100f38272
- Understand differences between star and snowflake schemas - http://www.differencebetween.net/technology/difference-between-star-and-snowflake-schema/

## Detail Links

- Bulk loading and stage tables (one hour), includes warehousing for loading scenarios - https://www.youtube.com/watch?v=lI5OQPjuj-8
- Snowpipe streams in detail (30 minutes), includes understanding pipe costs - https://www.youtube.com/watch?v=PNK49SJvXjE
- Step-by-Step create external AWS S3 table (40 minutes), includes SQS notification process - https://www.youtube.com/watch?v=w9BQsOlJc5s

## Data Lifecycle

- SnowflakeDB data loading options summarized on one page - [link](https://docs.snowflake.com/en/user-guide/data-load-overview.html)
- Shown below, from SnowflakeDB documentation - [link](https://docs.snowflake.com/en/user-guide/data-lifecycle.html)

<img src="https://github.com/lynnlangit/learn-snowflakedb/blob/main/images/lifecycle.png" width=800>

## Table Types

In 2022 SnowflakeDB launched a series of new features. In this [linked blog post](https://medium.com/snowflake/4-new-table-types-in-2022-by-snowflake-a-summary-301fb4fcdf60) the author discusses the 4 new categories of tables that are now available.  These new table types are in addition to the following types: “Standard Tables”, “Temporary Tables”, “Transient Tables” & “External Tables”.  

New Types are these: "Iceberg Tables", "Dynamic Tables", "Hybrid Tables", & "Event Tables."  Shown below is a summary of newly-introduced tables types and associated use cases (from the blog linked above).

<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*h6EiPAQmU8T9p7Q1tK8Rng.png">
