import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service



url = 'https://trendlyne.com/portfolio/superstar-shareholders/index/'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

options = webdriver.ChromeOptions()
options.headless = True




##Function to get the list of superstars of investing and their investested companies
def get_data(url,driver):
    #getting all data from first 2-3 col of superstars
    try:
        # sign_in(url,driver)
        # Now proceed with scraping
        driver.get(url)
        soup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="table-responsive"]')))
    
        data = {'SuperStar':[],'portfolio_value':[],'Number_stocks':[],'sector-prefernce':[],'top-holding':[],'recently_buy':[],'recently_sale':[]}
        star = soup.find_elements(By.XPATH,'//tr[@role="row"]')
        for index, row in enumerate(star):
            # Break the loop if 50 names have been retrieved
            name = row.find_elements(By.XPATH,'//a[@class="nolb titlecase"]')
            value = row.find_elements(By.XPATH,'//span[@class="cur-value"]')
            stocks = row.find_elements(By.XPATH,'//td[@class="sup-qty rightAlgn"]')
            sectors = row.find_elements(By.XPATH,'//td[@class="sector-data lAlign"]')
            stock_hold = row.find_elements(By.XPATH,'//td[@class="top-holding-data lAlign"]')
            stock_buy = row.find_elements(By.XPATH,'//td[@class="bought-data lAlign"]')
            stock_sale = row.find_elements(By.XPATH,'//td[@class="sold-data lAlign"]')
            for name_element,digit,num_stock,sector,holding,buy,sale  in zip(name,value,stocks,sectors,stock_hold,stock_buy,stock_sale):
                name_text = name_element.text
                if name_text not in data['SuperStar']:
                    data['SuperStar'].append(name_text)
                    data['portfolio_value'].append(digit.text)
                    data['Number_stocks'].append(num_stock.text)
                    data['sector-prefernce'].append(sector.text.replace('\n',''))
                    data['top-holding'].append(holding.text.replace('\n',''))
                    data['recently_buy'].append(buy.text.replace('\n',''))
                    data['recently_sale'].append(sale.text.replace('\n',''))
                    
                else:
                    pass
    finally:
    # Convert data to DataFrame
        df = pd.DataFrame(data)
            
            # Save DataFrame to Excel
        df.to_excel("fresh_data_new.xlsx", index=False)

        driver.quit()

    
# print(get_data(url,driver))



# Function to get the portfolio of these investors 
"""
By using this function you can get the investors full Portfolio
"""
def get_investortdata(links):
    data = {'Name': [], 'stocks': [],'tech data':[]}
    try:
        for url in links:
            driver.get(url)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//table[@class="superstar-shareholding table fs09rem tl-dataTable tableFetch portChildV1         JS_autoDataTables childrowDT dataTable no-footer"]')))

            soup = driver.find_element(By.XPATH, '//div[@class="table-responsive"]')
            col_odd = soup.find_elements(By.XPATH, '//table[@class="superstar-shareholding table fs09rem tl-dataTable tableFetch portChildV1         JS_autoDataTables childrowDT dataTable no-footer"]')
            tech = soup.find_elements(By.XPATH, '//tr[@role="row"]')
            names = driver.find_elements(By.XPATH, '//h1[@class="page-title-heading mb0"]')
            

            for odd in col_odd:
                    name = odd.find_elements(By.XPATH,'.//a[@class="nolb stockrow"]')
                    for odd_name in name:
                        data['stocks'].append(odd_name.text)
            for name in names:
                data['Name'].append(name.text)

            for row in tech:
                company_data = row.text.split('\n')[1:]  # Remove the company name from the data
                if company_data:  # Check if company_data is not empty
                    data['tech data'].append('\n'.join(company_data))


            max_length = max(len(data['Name']), len(data['stocks']), len(data['tech data']))
            data['Name'] += [''] * (max_length - len(data['Name']))
            data['stocks'] += [''] * (max_length - len(data['stocks']))
            data['tech data'] += [''] * (max_length - len(data['tech data']))
    except Exception as e:
        print(f"An error occurred: {e}") 
    
    df = pd.DataFrame(data)
    
    df['tech data'] = df['tech data'].apply(lambda x: x if isinstance(x, str) else '\n'.join(x))
    
    df.to_excel(f"portfolio_new.xlsx", index=False)




#getting the urls of every investors's portfolio
url = "https://trendlyne.com/portfolio/superstar-shareholders/index/"
def urls(url):
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        # Configure webdriver options with the desired user agent
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    service = Service(ChromeDriverManager().install())
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-gpu')  # Necessary if running on Windows
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    time.sleep(5)
    sign_in_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="login-signup-btn"]')))
    sign_in_button.click()

    # Find the username and password input fields and fill them with your credentials
    google_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='socialaccount_provider']")))
    google_field.click()
    
    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="email"]')))
    email_field.send_keys("") ## Enter Your email id
    time.sleep(3)

    next_button = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")))
    next_button.click()
    # time.sleep(5)
    password_field = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="password"]')))
    password_field.send_keys("") # enter your password
    # # Find the sign-in button and click it
    pass_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"]')))
    pass_button.click()
    time.sleep(120)
    no_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//option[@value="100"]')))
    no_button.click()
    time.sleep(3)
    data=[]
    
    while True:
        star = driver.find_elements(By.XPATH, '//tr[@role="row"]')
        for index, row in enumerate(star):
            # Break the loop if 50 names have been retrieved
            urls = row.find_elements(By.XPATH,'//a[@class="nolb titlecase"]')
            for star_url in urls:
                link = star_url.get_attribute('href')
                if link not in data:
                    data.append(link)

        return data
    

links= urls(url)
print(get_investortdata(links))
driver.quit()



#Function to get the all companies's finacial data
"""
By using this function you can get the all finacial data of a company
"""
url = 'https://www.screener.in/login/?'
def get_company_data(url):
    all_company_data = []
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    # Configure webdriver options with the desired user agent
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    service = Service(ChromeDriverManager().install())
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-gpu')  # Necessary if running on Windows
    driver = webdriver.Chrome(service=service, options=options)

    #define driver
    driver.get(url)
    #clicking on buttons
    button = driver.find_element(By.XPATH,'//span[@class="upper ink-900 letter-spacing strong"]')
    button.click()
    #Signin into a google account
    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='whsOnd zHQkBf']")))
    email_field.send_keys("") ## Enter Your Email id
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")))
    next_button.click()
    # Enter the password
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
    password_field.send_keys("") #Enter your password

    #Enter the next button
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")))
    next_button.click()

    #clicking the tool button to pass the quary and running the quary
    tool_button = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown-menu']")))
    tool_button.click()

    create_button = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='flex flex-align-center flex-gap-16']")))
    create_button.click()

    query_button = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@class='u-full-width']")))
    query_button.send_keys("Market Capitalization > 5000")

    run_query_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-primary']")))
    run_query_button.click()

    #Edit the colum to get the desire output
    column_edit = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button button-small button-secondary plausible-event-name=Edit+Columns plausible-event-user=free']")))
    column_edit.click()
    #clicking on the required metrix
    debt_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Earnings yield']")))
    if not debt_col.is_selected():
        debt_col.click()
    time.sleep(2)

    ebitda_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='EVEBITDA']")))
    if not ebitda_col.is_selected():
        ebitda_col.click()
    time.sleep(2)

    enterprise_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Enterprise Value']")))
    if not enterprise_col.is_selected():
        enterprise_col.click()
    time.sleep(2)
    #Profit after tax
    PAT_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Profit after tax']")))
    if not PAT_col.is_selected():
        PAT_col.click()
    time.sleep(2)
    #Debt to equity
    DTE_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Debt to equity']")))
    if not DTE_col.is_selected():
        DTE_col.click()
    time.sleep(2)
    #Promoter Holdings
    Promoter_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Promoter holding']")))
    if not Promoter_col.is_selected():
        Promoter_col.click()
    time.sleep(2)
    #Industry PE ratio
    indu_pe_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Industry PE']")))
    if not indu_pe_col.is_selected():
        indu_pe_col.click()
    time.sleep(2)
    #Sale growth 
    sale_gr_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Sales growth']")))
    if not sale_gr_col.is_selected():
        sale_gr_col.click()
    time.sleep(2)
    #Profit growth
    pro_gr_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Profit growth']")))
    if not pro_gr_col.is_selected():
        pro_gr_col.click()
    time.sleep(2)
    #PE Ratio
    pe_col = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Price to Earning']")))
    if not pe_col.is_selected():
    # Click on the element
        pe_col.click()

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(5)
    save_col = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button-primary"]')))
    save_col.click()
    
    clicked_buttons = set()
    company_data=[]
    
    while True:
        next_page_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="ink-900"]')))
        next_page_click = False
        
        for next_page_button in next_page_buttons:
                page_number = next_page_button.text
                if page_number not in clicked_buttons:  # Check if the button has not been clicked before
                    next_page_button.click()  # Click the button
                    clicked_buttons.add(page_number)  # Add the href to the set of clicked buttons
                    next_page_click = True
                    break
                      # Exit the loop to click the next button
        if next_page_click:
            # time.sleep(2)  
            data = driver.find_elements(By.XPATH,'//table')   
            # print(data)         
            for table in data:
                rows = table.find_elements(By.XPATH, './/tr')
                
                for row in rows:
                    cells = row.find_elements(By.XPATH, './/td')
                    company_list= []
                    for cell in cells:
                        company_list.append(cell.text if cell.text.strip() else None)            
                    
                    company_data.append(company_list)

        else:
            break
                   
    # return company_data

    df = pd.DataFrame(company_data, columns=["S.No.","Name",
                                             "CMP Rs.","Mar Cap Rs.Cr.","Div Yld %","NP Qtr Rs.Cr.","Qtr Profit Var %",
                                             "Sales Qtr Rs.Cr.","Qtr Sales Var %","ROCE %","Debt Rs.Cr.","P/E","Earnings Yield %","EV / EBITDA","EV Rs.Cr.",
                                             "PAT 12M Rs.Cr.","Debt / Eq","Prom. Hold. %"])

    # Save the DataFrame to an Excel file
    df.to_excel("fresh_company_data2.xlsx", index=False)

# print(get_company_data(url))