import sys
import pandas as pd
import re
import time


def main():
    sms_df = pd.read_csv("Data/sms_df.csv", engine='python')
    # change epoch date to human readable date
    sms_df['date'] = pd.to_datetime(sms_df['date'], unit='ms') .dt.strftime('%d-%m-%Y')
    df_7494 = sms_df[sms_df['body'].str.contains('7494\s', na=False, regex=True)]
    df_7494 = sms_df[sms_df['body'].str.contains('5808\s', na=False, regex=True)]
    df_9418 = sms_df[sms_df['body'].str.contains('3509\s', na=False, regex=True)]
    df_7494 = sms_df[sms_df['body'].str.contains('7494\s', na=False, regex=True)]
    df_3509 = sms_df[sms_df['body'].str.contains('3509\s', na=False, regex=True)]

    df_3509['CrDr'] = df_3509['body'].apply(lambda row: 'Credit' if 'Credit' in row else ('Debit' if 'Debit' in row else 'Other'), axis=1)


if __name__ == '__main__':
    main()
