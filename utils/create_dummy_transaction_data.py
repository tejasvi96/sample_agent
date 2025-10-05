import pandas as pd
import datetime 
sample_transaction_data = [] 
import numpy as np
TRANSACTION_LIMIT = 10000
for i in range(100):
    transaction_id = i
    transaction_date = datetime.datetime.now()
    transaction_amount = np.random.randint(5000,500000)
    row_dict = {'transaction_id':transaction_id,'transaction_date':transaction_date,'transaction_amount':transaction_amount}
    sample_transaction_data.append(row_dict)
sample_transaction_data_df = pd.DataFrame.from_dict(sample_transaction_data)
sample_transaction_data_df[sample_transaction_data_df['transaction_amount']>TRANSACTION_LIMIT]

sample_transaction_data_df.to_csv('./high_net_worth_statement.csv')

import datetime 
sample_transaction_data = [] 
import numpy as np

for i in range(100):
    transaction_id = i
    transaction_date = datetime.datetime.now()
    transaction_amount = np.random.randint(5000,8000)
    row_dict = {'transaction_id':transaction_id,'transaction_date':transaction_date,'transaction_amount':transaction_amount}
    sample_transaction_data.append(row_dict)
sample_transaction_data_df = pd.DataFrame.from_dict(sample_transaction_data)
sample_transaction_data_df[sample_transaction_data_df['transaction_amount']>TRANSACTION_LIMIT]

sample_transaction_data_df.to_csv('./low_net_worth_statement.csv')