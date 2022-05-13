from mailbox import Mailbox
import pandas as pd

leagues=['NFL','MLB','NBA']
divisions={1:['AFC East','NFC East','AFC West','NFC West','AFC North', \
'NFC North ','AFC South','NFC South'],2:['AL East ','NL East','AL Central', \
'NL Central','AL West','NL West'],3:['Atlantic','Pacific','Central', \
'Southwest','Southeast','Northwest']}

## to do: add divisions and teams in here
teams={1:{1:['BuffaloBills', 'NewEnglandPatriots', 'MiamiDolphins', 'NewYorkJets'],2:['DallasCowboys','PhiladelphiaEagles', 'WashingtonCommanders', 'NewYorkGiants'],3:['KansasCityChiefs', 'LasVegasRaiders', 'LosAngelesChargers', 'DenverBroncos'], 4:['LosAngelesRams', 'ArizonaCardinals', 'SanFrancisco49ers', 'SeattleSeahawks'], 5:['CincinnatiBengals', 'PittaburghSteelers', 'ClevelandBrowns', 'BaltimoreRavens'], 6:['GreenBayPackers', 'MinnesotaVikings', 'ChicagoBears', 'DetroitLions'], 7:['TennesseeTitans', 'IndianapolisColts', 'HoustonTexans', 'JacksonvilleJaguars'], 8:['TampaBayBuccaneers', 'NewOrleansSaints', 'AtlantaFalcons', 'CarolinaPanthers']}, 2:{1:['NewYorkYankees', 'TampaBayRays', 'TorontoBlueJays', 'BaltimoreOrioles', 'BostonRedSox'],2:['NewYorkMets', 'AtlantaBraves', 'MiamiMarlins', 'PhiladelphiaPhillies', 'WashingtonNationals'],3:['ChicagoWhiteSox', 'ClevelandGuardians', 'KansasCityRoyals', 'MinnesotaTwins', 'MilwaukeeBrewers', 'DetroitTigers'], 4:['ChicagoCubs', 'CincinnatiReds', 'StLouisCardinals', 'PittsburghPirates', 'HoustonAstros'], 5:['LosAngelesAngels', 'OaklandAthletics', 'TexasRangers', 'SeattleMariners', 'HoustonAstros'], 6:['LosAngelesDodgers', 'SanFranciscoGiants', 'SanDiegoPadres', 'ColoradoRockies', 'ArizonaDiamondbacks']}, 3:{1:['BostonCeltics', 'Philadelphia76ers', 'TorontoRaptors', 'BrooklynNets', 'NewYorkKnicks'], 2:['PhoenixSuns', 'GoldenStateWarriors', 'LosAngelesClippers', 'SacramentoKings'], 3:['MilwaukeeBucks', 'ChicagoBulls', 'ClevelandCavaliers', 'IndianaPacers', 'DetroitPistons'], 4:['MemphisGrizzlies', 'DallasMavericks', 'NewOrleansPelicans', 'SanAntonioSpurs', 'HoustonRockets'], 5:['MiamiHeat', 'AtlantaHawks', 'CharlotteHornets', 'WashingtonWizards', 'OrlandoMagic'], 6:['UtahJazz', 'DenverNuggets', 'MinnesotaTimberwolves', 'PortlandTrailBlazers', 'OklahomaCityThhunder']}}

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
        team=int(input('Please type what team you would like to view:'))
    print(pd.read_csv('Rosters/'+teams[league][division][team-1]+'_Roster.csv'))


if __name__=="__main__":
    main()





