I created a database based on a dataset that showed the number of layoffs in 2023 for a number of companies around the world
This dataset contained both incomplete data and duplicate values that needed to be cleaned
The folloing is a documentation of the process i used for cleaning the data
  1. I created a duplicate table and copied  data into it from the source files.This was done to avoid contamining data from the source file.
  2. I queried for duplicate values using the windows function (PARTITION BY).
  3. This data was then loaded to another staging area and all the duplicate values removed
  4. I standardized the data by removing trailing whitespaces with the TRIM function and checked for cases of doublebooking
  5. I changed a date column from string to DATE type to streamline the process of analysis
  6. I filled in blank and null values \
  7. I removed unnecessary rows and columns
