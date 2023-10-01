import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('./big-mac-full-index.csv')
#YYY-MM-DD
year = '2010'
country_code = 'mys'
dollar_price = '1.7'


def get_big_mac_price_by_year(year, country_code):
   query_text = f"date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3.str.lower() == '{country_code.lower()}'"
   df_result = df.query(query_text)
   mean_dollar_price = df_result['dollar_price'].mean()
   return round(mean_dollar_price, 2)
   

def get_big_mac_price_by_country(country_code):
    query_text = f"iso_a3.str.upper() == '{country_code.upper()}'"
    df_result = df.query(query_text)
    filtered_data = df[df['iso_a3'] == country_code.upper()]
    mean_dollar_price = filtered_data['dollar_price'].mean()
    return round(mean_dollar_price, 2)


def get_the_cheapest_big_mac_price_by_year(year):
    query_text = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_result = df.query(query_text)                    
    cheapest_row = df_result.loc[df_result['dollar_price'].idxmin()]
    return f"{cheapest_row['name']}({cheapest_row['iso_a3']}): ${'%.1f' %cheapest_row['dollar_price']}"


def get_the_most_expensive_big_mac_price_by_year(year):
    query_text = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    df_result = df.query(query_text)  
    expensive_row = df_result.loc[df_result['dollar_price'].idxmax()]
    return f"{expensive_row['name']}({expensive_row['iso_a3']}): ${'%.1f' %expensive_row['dollar_price']}"

    

if __name__ == "__main__":  
       result_a = get_big_mac_price_by_year(2010, "arg")
       print(result_a) 

       result_b = get_big_mac_price_by_country("mex")
       print(result_b) 

       result_c = get_the_cheapest_big_mac_price_by_year(2008)
       print(result_c) 
       
       result_d = get_the_most_expensive_big_mac_price_by_year(2014)
       print(result_d) 

    