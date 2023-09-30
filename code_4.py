import pandas as pd
filename = './big-mac-full-index.csv'
df = pd.read_csv(filename)

def get_big_mac_price_by_year(year, country_code):
   query_text = f"iso_a3 == '{country_code.upper()}' and date =='{year}'"
   df_result = df.query(query_text)
   mean_price = df_result['dollar_price'].mean()
   return round(mean_price, 2)
   

def get_big_mac_price_by_country(country_code):
    query_text = f"iso_a3 == '{country_code.upper()}'"
    df_result = df.query(query_text)
    mean_price = df_result['dollar_price'].mean()
    return round(mean_price, 2)


def get_the_cheapest_big_mac_price_by_year(year):
    query_text = f"date == '{year}'"
    df_result = df.query(query_text)
    cheapest_row = df_result.loc[df_result['dollar_price'].idxmin()]
    return f"{cheapest_row['name']}({cheapest_row['iso_a3']}): ${round(cheapest_row['dollar_price'], 2):.2f}"
    

def get_the_most_expensive_big_mac_price_by_year(year):
    query_text = f"date == '{year}'"
    df_result = df.query(query_text)
    expensive_row = df_result.loc[df_result['dollar_price'].idxmax()]
    return f"{expensive_row['name']}({expensive_row['iso_a3']}): ${round(expensive_row['dollar_price'], 2):.2f}"


    if __name__ == "__main__":  
       result_a = get_big_mac_price_by_year(2010, "arg")
       print(result_a) # 2.7

       result_b = get_big_mac_price_by_country("mex")
       print(result_b) # 2.68

       result_c = get_the_cheapest_big_mac_price_by_year(2008)
       print(result_c) # Malaysia(MYS): $1.7

       result_d = get_the_most_expensive_big_mac_price_by_year(2014)
       print(result_d) # Norway(NOR): $7.8

    