import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
import sys
import seaborn as sns
import calendar as cal


def comparison(FIPS_list):
    
    months_df = pd.read_csv("months.csv")


    df_list = []
    for month in months_df.date:
        df = pd.read_csv('data/Merge/vaccinations-and-deaths-' + month +'.csv', converters={'FIPS' : str})
        df['Date'] = month
        df_list.append(df[df['FIPS'].isin(FIPS_list)])

    
    final_df = pd.concat(df_list)
    final_df['Deaths_per_10k'] = final_df['Deaths']/final_df['Census2019_18PlusPop']*10000

    fig, ax1 = plt.subplots()

    ax1 = sns.barplot(data = final_df, x = 'Date', y = 'Deaths_per_10k', hue = 'Recip_County')
    ax2 = ax1.twinx()
    sns.lineplot(data= final_df, x = 'Date', y = 'Series_Complete_18PlusPop_Pct', hue = 'Recip_County', legend = False)
    #customize
    new_labels = [cal.month_abbr[int(label.get_text()[:2])] + " '" + label.get_text()[8:] for label in ax1.get_xticklabels()]
    ax1.set_xticks(range(len(new_labels)), labels = new_labels)
    # ax1.set_aspect(1.5)
    ax1.legend(title = "County")
    ax1.set_ylabel("Deaths (per 10k)")
    ax2.set_ylabel("Vaccination Rate (%)")

    
    fig.set_size_inches(18.5, 10.5)
    plt.savefig("img/fig2.png", dpi = 100)

    

def main(argv):
    comparison([argv[0], argv[1]])

if __name__ == "__main__":
    argv = sys.argv[1:]
    if not (len(argv) == 2 or len(argv) == 0):
        print("Invalid number of arguments.")
    main(argv)
