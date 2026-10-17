# Titanic Dataset Cleaning Project

## 1. Project Overview

This project demonstrates data inspection and cleaning using Python and the pandas library. The dataset contains passenger information from the Titanic, including age, sex, passenger class, fare, cabin, and survival status.

The objective was to identify missing values, duplicate records, incorrect data types, and inconsistent values, then clean the dataset and save the results.

## 2. Dataset Source

The dataset was obtained from the Kaggle Titanic competition.

Source: https://www.kaggle.com/competitions/titanic/data

The original training dataset contains 891 rows and 12 columns.

## 3. Data Quality Issues Identified

- **Missing values:** Age contained 177 missing values, Cabin contained 687, and Embarked contained 2.
- **Duplicate records:** No exact duplicate rows were found.
- **Data types:** No non-numeric values were detected in the numeric columns checked.
- **Inconsistent formatting:** Two Name entries contained leading or trailing spaces.
- **Invalid values:** No negative ages, negative fares, invalid survival values, invalid passenger classes, or unexpected Embarked categories were detected by the checks performed.

## 4. Cleaning Methods

The following operations were performed using Python and pandas:

1. Removed unnecessary leading and trailing spaces from text fields.
2. Standardized Sex values to lowercase and Embarked values to uppercase.
3. Converted the expected numeric columns to numeric data types.
4. Removed exact duplicate rows, if present.
5. Filled missing Age values using the median for passengers in the same passenger class and sex, with the overall median as a fallback.
6. Filled missing Embarked values using the most frequent category.
7. Replaced missing Cabin values with `Unknown` to distinguish unavailable information from recorded cabin assignments.
8. Exported the cleaned dataset to CSV.

## 5. Results

| Metric | Before cleaning | After cleaning |
|---|---:|---:|
| Rows | 891 | 891 |
| Columns | 12 | 12 |
| Missing values | 866 | 0 |
| Exact duplicate rows | 0 | 0 |

The cleaned dataset retains all 891 passenger records and all 12 columns. The verification checks confirmed that no missing values or exact duplicate rows remained.

## 6. Files

- `train.csv` — original dataset.
- `clean_data.py` — Python script for inspection, cleaning, and verification.
- `cleaned_titanic.csv` — cleaned dataset.

## 7. Tools Used

- Python
- pandas
- PyCharm
- GitHub

## 8. Conclusion

This project demonstrates a basic data-cleaning workflow, from identifying data-quality issues to applying appropriate corrections and verifying the results. The cleaned dataset is ready for further exploratory data analysis, while the original dataset remains unchanged.

