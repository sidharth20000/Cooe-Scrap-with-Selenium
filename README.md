# Cooe.in Web Scraper and Machine Learning Project

This project involves web scraping data from cooe.in, performing data analysis, and applying machine learning techniques to predict color outcomes.

## Features

- Web scraping using Selenium and BeautifulSoup
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA) with matplotlib and seaborn
- Machine Learning using Random Forest Classifier

## Requirements

- Python 3.x
- pandas
- selenium
- beautifulsoup4
- matplotlib
- seaborn
- scikit-learn
- webdriver_manager

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/cooe-scraper-ml.git
   cd cooe-scraper-ml
   ```

2. Install the required packages:
   ```
   pip install pandas selenium beautifulsoup4 matplotlib seaborn scikit-learn webdriver_manager
   ```

3. Ensure you have Chrome browser installed as the script uses ChromeDriver.

## Usage

1. Update the login credentials in the script:
   ```python
   username_input.send_keys('YOUR_USERNAME')
   password_input.send_keys('YOUR_PASSWORD')
   ```

2. Run the script:
   ```
   python main.py
   ```

## Project Structure

1. Web Scraping: The script logs into cooe.in and scrapes data from multiple pages.
2. Data Processing: Extracted data is cleaned and structured into a pandas DataFrame.
3. Exploratory Data Analysis: Visualizations are created using matplotlib and seaborn.
4. Machine Learning: A Random Forest Classifier is trained to predict color outcomes.

## Note

This script is for educational purposes only. Ensure you have permission to scrape data from cooe.in and comply with their terms of service.
