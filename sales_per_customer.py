import pandas as pd

customer_df = pd.read_csv('C:\TestPython\Test\customers.csv')

sales_df = pd.read_csv('C:\TestPython\Test\sales.csv')

customer_sales_df = customer_df.merge(sales_df, on = 'customer_id')

customer_sales_sum_df = customer_sales_df1 = pd.DataFrame(customer_sales_df, ).groupby(['name', 'email', 'address'], as_index =  False).sum()


customer_sales_rename_col_df = customer_sales_sum_df['sum(quantity)'] = customer_sales_sum_df['quantity']


customer_sales_final_df = customer_sales_sum_df.drop(['quantity', 'customer_id', 'product_id', 'date'], axis = 'columns')


customer_sales_final_df.to_csv('C:\TestPython\Test\sales_per_customer.csv', index=False)