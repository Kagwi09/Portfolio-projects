CREATE DATABASE world_layoffs;
USE world_layoffs;
SELECT * FROM layoffs_raw;

-- 1. Load data into staging area --
CREATE TABLE layoffs_staging
LIKE layoffs_raw;

INSERT layoffs_staging
SELECT *
FROM layoffs_raw;

SELECT * FROM layoffs_staging;

-- 2. Remove Duplicates
-- If index is greater than one, then the entry is a duplicate
WITH duplicate_cte AS
(
SELECT *, ROW_NUMBER() OVER(
PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions)
AS `index`
FROM layoffs_staging)

SELECT * FROM duplicate_cte
WHERE `index` > 1;

-- CREATE AN EMPTY SECOND STAGING TABLE WITH A ROW NUMBER COLUMN
CREATE TABLE `layoffs_staging2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SELECT * FROM layoffs_staging2;

-- INSERT DATA FROM layoffs_staging

INSERT INTO layoffs_staging2
SELECT *, ROW_NUMBER() OVER(
PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions)
AS `index`
FROM layoffs_staging;

-- DELETE DUPLICATE ITEMS FROM TABLE (row_num > 1)

SELECT * FROM layoffs_staging2
WHERE row_num > 1;

DELETE FROM layoffs_staging2
WHERE row_num > 1;

-- 3. Standardize the data
-- REMOVE WHITEPACES, YOU SHOULD DO IT FOR ALL COLUMNS WHERE APPLICABLE 

SELECT company, TRIM(company)
FROM layoffs_staging2;

UPDATE layoffs_staging2
SET company = TRIM(company);

-- CHECK FOR CASES WHERE ITEMS MAY BE DOUBLE BOOKED UNDER DIFFERENT NAMES
-- SELECT DISTINCT ITEMS IN COLUMNS AND GO THROUGH THEM TO ENSURE THAT THE THERE ARE NO DOUBLE BOOKINGS OR MISPELLING

SELECT * FROM layoffs_staging2
WHERE industry LIKE 'Crypto%';

UPDATE layoffs_staging2
SET industry = 'Crypto'
WHERE industry LIKE 'Crypto%';

UPDATE layoffs_staging2
SET country = 'United States'
WHERE country LIKE 'United States%';

SELECT DISTINCT country FROM layoffs_staging2
ORDER BY 1;

-- 4. Fill in null values or blanks
-- 5. Remove unnecessary columns