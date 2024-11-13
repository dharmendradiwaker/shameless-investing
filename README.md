# 📊 Investor Portfolio and Company Financial Data Analysis

This project integrates two major sources of financial data:
1. **Indian Companies Financial Data** 🏢
2. **Indian Big Investors Portfolio** 💼

The purpose of this integration is to analyze and combine the financial details of companies with the investment portfolios of top investors to gain insights into their stock predictions.

## 🛠️ Project Files

### 1. **`trendzline.py`** 📉
   This file contains the functions for:
   - **Fetching company financial data** 💰
   - **Getting the list of top investors and the companies they've invested in** 📈
   - **Retrieving the full portfolio of these investors** 📑

   #### Available Functions:
   - `get_data()`: Fetches the list of **superstar investors** and their **invested companies**.
   - `get_investor_data()`: Retrieves the full portfolio of the selected investors, including all the companies they are invested in.
   - `get_company_data()`: Fetches detailed financial data of companies, including key metrics like revenue, profit, stock performance, etc.

### 2. **`combined_files.py`** 🔗
   This file combines the financial data of **Indian companies** with the investment portfolios of **big Indian investors**. This allows you to compare the financial performance of companies with the investment decisions of top investors.

   #### Integration:
   - By merging both datasets (company financials and investor portfolios), you can analyze which companies are attracting successful investors and whether these investors' predictions align with the companies' financial health.

## 🚀 Project Features

- **Investor Portfolio Scraper** 💼:
   - Extracts **superstar investors** and the **companies they have invested in**.
   - Provides a complete **portfolio** of each investor, detailing the companies they have funded.

- **Company Financial Data Scraper** 🏢:
   - Fetches detailed **financial data** for companies in India.
   - Key financial metrics are included for analysis.

- **Data Integration** 🔗:
   - Combines **investor portfolio data** and **company financial data** to provide insights into which companies are favored by top investors, and evaluates the financial health of these companies.

## 📁 Project Structure

- **`trendzline.py`**: 
   - Contains functions to retrieve financial data of companies and the investment portfolios of investors.
  
- **`combined_files.py`**:
   - Merges both the investor data and company financial data to analyze stocks from both perspectives.

## 📝 Function Details

### **1. `get_data()` - List of Investors and Their Invested Companies** 💼

This function retrieves the list of prominent **superstar investors** and identifies the **companies** they have invested in. It helps to track successful investors and their stock picks.

- **Output**: List of investors and companies they have invested in.

### **2. `get_investor_data()` - Investor Full Portfolio** 📑

This function allows you to get the **full portfolio** of an investor, providing insights into their investment strategy and their selected companies.

- **Input**: Investor name (can loop through a list of investors).
- **Output**: Portfolio of the investor with the companies they are invested in.

### **3. `get_company_data()` - Financial Data of Companies** 🏢

This function fetches the **financial data** of a company, which may include revenue, profit, stock performance, and more.

- **Input**: Company name or stock symbol.
- **Output**: Financial data of the company.

### **4. Combining Data in `combined_files.py`** 🔗

This file combines the data from `trendzline.py`:
- Merges **investor portfolio data** with **company financial data**.
- Analyzes which companies attract the most successful investors and how their financials support these investment choices.

## 📊 Data Analysis

- Once both datasets (investor portfolios and company financials) are merged, you can analyze:
  - **Investor behavior**: What companies are top investors betting on?
  - **Company financial health**: Do companies with strong financials attract more investors?

This combination provides powerful insights into both company performance and investor strategies.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Investor-Portfolio-Company-Data.git
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
