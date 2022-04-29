import pandas as pd

leagues=['NFL','MLB','NBA']
divisions={1:['AFC East','NFC East','AFC West','NFC West','AFC North', \
'NFC North ','AFC South','NFC South'],2:['* AL East ','NL East','AL Central', \
'NL Central','AL West','NL West'],3:['Atlantic','Pacific','Central', \
'Southwest','Southeast','Northwest']}

## to do: add divisions and teams in here
teams={3:{1:['BostonCeltics']}}


def main():
    for i,l in enumerate(leagues):
        print('{}. {}'.format(i+1,l))
    league=0
    while league not in divisions.keys():
        league=int(input('Please type what sport you would like to view:'))
    for i,d in enumerate(divisions[league]):
        print('{}. {}'.format(i+1,d))
    division=0
    while division not in teams[league].keys():
        division=int(input('Please type division you would like to view: '))
    for i,t in enumerate(teams[league][division]):
        print('{}. {}'.format(i+1,t))
    team=0
    while team not in range(1,len(teams[league][division])+1):
        team=int(input('Please type what sport you would like to view:'))
    print(pd.read_csv('Rosters/'+teams[league][division][team-1]+'_Roster.csv'))


if __name__=="__main__":
    main()
