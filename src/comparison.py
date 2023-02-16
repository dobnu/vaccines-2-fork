import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
import sys
import seaborn as sns

def fips_to_name(FIPS):
    map = defaultdict(lambda: FIPS)
    map.update({
        '44003': 'Kent County, RI',
        '01125': 'Tuscaloosa County, AL',
    })
    return map[FIPS]

def comparison(FIPS_1='44003', FIPS_2='01125'):
    months_df = pd.read_csv("months.csv")
    months_list = months_df.date.to_list()

    file_list = []
    for month in months_list:
        df = pd.read_csv('data/Merge/vaccinations-and-deaths-' + month +'.csv', converters={'FIPS' : str})
        df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
        df['Month'] = month
        file_list.append(df)


    merged_df = pd.concat(file_list)
    
    Kent = merged_df[ merged_df['FIPS'] == '44003']
    Kent_graph = Kent.loc[: , ['FIPS', "Deaths_Per_1e5", "Month"]]

    Tuscaloosa = merged_df[ merged_df['FIPS'] == '01125']
    Tuscaloosa_graph = Tuscaloosa.loc[: , ['FIPS', "Deaths_Per_1e5", "Month"]]


    graph_df = pd.concat([Kent_graph, Tuscaloosa_graph], ignore_index = True)
    plot = sns.catplot(x= "Month", y="Deaths_Per_1e5", hue = 'FIPS', data = graph_df, kind = 'bar', aspect = 2)
    plot.set_axis_labels("Months (May 2021 - Dec 2022)", "COVID Deaths (per 100k)")

    # new_labels = [(label.get_text()[:3] + label.get_text()[8:]) for label in plot.get_xticklabels()]
    new_labels = [month[:3] + month[8:] for month in months_list]
    plot.set_xticklabels(labels = new_labels)

    plot.savefig("img/comp.png")


    """
    cleaned_df = merged_df[merged_df['FIPS'].str.contains(FIPS_1+"|"+FIPS_2)]

    FIPS_1_name = fips_to_name(FIPS_1)
    FIPS_2_name = fips_to_name(FIPS_2)

    print("Comparing "+FIPS_1_name+" and "+FIPS_2_name)
    FIPS_1_vax = cleaned_df.loc[cleaned_df['FIPS']==FIPS_1]
    FIPS_1_vax = FIPS_1_vax["Series_Complete_18PlusPop_Pct"]
    FIPS_1_death = cleaned_df.loc[cleaned_df['FIPS']==FIPS_1]
    FIPS_1_death = FIPS_1_death['Deaths_Per_1e5']
    
    FIPS_2_vax = cleaned_df.loc[cleaned_df['FIPS']==FIPS_2]
    FIPS_2_vax = FIPS_2_vax["Series_Complete_18PlusPop_Pct"]
    FIPS_2_death = cleaned_df.loc[cleaned_df['FIPS']==FIPS_2]
    FIPS_2_death = FIPS_2_death['Deaths_Per_1e5']

    fig,ax1 = plt.subplots() 
    x = [0, 1, 2, 3, 4, 5, 6]
    labels = ['May', 'June', 'July', 'August', 'September', 'October', 'November']
    x = np.arange(len(labels))
    width = 0.35 
    ax1.set_xticks(x, labels)
    ax1.set_ylim(0, 100)
    ax1.set_xlim(0,6)
    ax1.set_title('18+ Vaccination Rates and Deaths in '+FIPS_1_name+" and "+FIPS_2_name, wrap=True)
    ax1.set_xlabel('Month 2021')
    ax1.set_ylabel('Percent Vaccinated') 
    ax1.bar(x - width/2, FIPS_1_vax, width, color='darkcyan', label = '% Vaccinated in '+FIPS_1_name)
    ax1.bar(x + width/2, FIPS_2_vax, width, color='indianred', label = '% Vaccinated in '+FIPS_2_name)
    ax2 = ax1.twinx()
    ax2.plot(x, FIPS_1_death, color='darkslategray', label = '# of Deaths in '+FIPS_1_name)
    ax2.plot(x, FIPS_2_death, color='firebrick', label = '# of Deaths in '+FIPS_2_name)
    ax2.set_ylabel('Deaths per 100k Population.')
    handles_1, _ = ax1.get_legend_handles_labels()
    handles_2, _ = ax2.get_legend_handles_labels()
    handles_2.extend(handles_1) # adds the list items from handles_1 to handles_2
    ax2.legend(handles = handles_2, loc='upper left')
    fig.savefig("img/comparison.png")
    """

def main(argv):
    comparison(argv[0], argv[1])

if __name__ == "__main__":
    argv = sys.argv[1:]
    if not (len(argv) == 2 or len(argv) == 0):
        print("Invalid number of arguments.")
    main(argv)
