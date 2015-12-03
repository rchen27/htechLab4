from TwitterSearch import *

def printUser(username):
    try:
        tuo = TwitterUserOrder(username) # create a TwitterUserOrder

        ts = TwitterSearch(
            consumer_key = '1kj4GBRevJITV4S40kLXGHVG2',
            consumer_secret = 'c80dJF41IwQV2G4ynR8VYblMQU15M4bc8OFg3aG6l8Y0aoSFhU',
            access_token = '1708110452-e3unR8gR7WRMGDoCh3aZutMPL3bFBLFlqHz8tzy',
            access_token_secret = 'kkiZDDp8KXLB8cRDwsMqBDc5IxqiaVXSmbQ2XtZEij0tl'
        )

        def my_callback_closure(current_ts_instance):
            queries, tweets_seen = current_ts_instance.get_statistics()
            #print queries, tweets_seen
            if queries > 0 and (queries % 5) == 0: # trigger delay every 5th query
                time.sleep(60) # sleep for 60 seconds
        
        i = 0
        # start asking Twitter about the timeline
        for tweet in ts.search_tweets_iterable(tuo, callback=my_callback_closure):
            if i > 50:
                break
            #print tweet['user']['screen_name']
            content =  tweet['text'].encode('utf-8')
            print content

            #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'].encode('utf-8') ) )
            i += 1
        return 1

    except TwitterSearchException as e: # catch all those ugly errors
        print(e)
        return 0

usernames = []
for line in open ('final.txt'):
    if 'username:' in line:
        usernames.append(line.split(' ')[1].rstrip())
print usernames
new = []
for line in open ('users.txt'):
    new.append(line.rstrip())
print new

overlap = [val for val in usernames if val in new]
print overlap
#usernames = ['HeiYeaSoul', 'VinnyBabyMomma', 'Spezzing', 'MariaYenD', 'corinnekaaay', 'WHATISAPLANET', 
#    'lachiebrapps']
'''
usernames = ['kojodm3', 'baabypriyaa', '_Herbie', 'faz4rbi', 'The_Sassy_Madam', 'JustinAmagoh', 
'akhaipatel56', '_alexis_ikia', 'camilahoyos681', '2ELENA0Miranda3', 'ally_amelia', 'JUNGKOCKLE', 
'yzmaj', 'RachelCameron15', 'DreasUsername', 'Imlairagtrrz', 'kkstupider', 'cXOntrolled', 'MijaelMosquera', 'Biggoon310', '_scarlettepaige', 'sneaker_fever_', 'cannibalpuns', 'Xythar', 'Your_Lexii', 'KayHemmings96', 'HaStyleTweets', '_KennaCakes', 'tori_glenn2299', 'censorednewsnow', 'jdbalani', 'm4MBJ7G', 'marissaa_silvaa', 'brOKen1217', 'jaylise4178', 'christine_mba', 'Sir_Hari_K', 'devonnesmadness', 'STDMessiah', 'shellysrambles', 'AnalCigars', 'Brandon_Winning', 'laurenswontons', 'sha_tohr_ee', 'T_Mac202', 'MayorGalvan713', 'EU_FIFA16', 'Hey_Its_Sam_22', 'MadelineWickel', 'EU_FIFA16', 'bewitchednarry', 'b4byrae', 'mHealthGlobal', 'EU_FIFA16', 'lewdfire', 'EU_FIFA16', 'corkfishh', 'olzanskislynch', 'kvngg_LolaB', 'thisgirlConnie', 'april_marie', 'isasaherrera', 'lima_bean3', 'Since1994_', 'KarenSitkakkp', 'psychotato', 'ThatNiggaLiban', 'megggggm', 'briansj13', 'hapababee', 'sleeepycurtis', 'fuckalzheimers', 'mattytalks', 'jenbabeeey', 'sabrinamelodies', 'Tinder23', 'carinabizarro', 'Mason_Complains', 'moonlightsfroot', 'beaninabeanie', 'SchomerSierra', 'reedenstein', 'Rememberandhope', 'nickhankes16', '_aaaariel', 'NotCecilio', 'jull17nna', 'IKUWA6_2016', 'hesborn94andi98', 'gabby2k18', 'danceadaisy', 'namelessvenussa', 'arturoclingan', 'AmigosInDanger', 'Maria_2793', 'adamTwright', 'saxahoya', 'PIZZAxGREASE', 'DustinFisher4', 'shanecareyy', 'ItsBeeForBells', 'taranicholle97', 'pr3ttyj_', 'al_moosy111', '_kybearr', 'stephg1996', 'Lex_Zimmy', 'HAROLDRUINEDME2', 'KissMyTashy', '_SimonSaid_', 'kojodm3', 'YupItsJamil', 'jaassssm', 'sm0landcurly', 'thatzmarcosb', 'bagchinirmalya', 'stephen_minnow', 'L_R_Bauer', '_followMYpaige', 'SharpTusk', 'triciawarren_', 'missaxmoon', 'kaitlan4', 'JanoMichelle', 'iamchuyyyy', 'twdismyfamliy', 'paige_shearer', 'dauzataddict', 'jane_stahl', 'Grey280', 'lukecalmikeashx', 'angelaplusradar', 'ID0ntGivaFuck', 'LickMyFairyDust', 'atlcasxy', 'the_tola', 'LadyHawkins', 'asmilecanlie', 'alia_rex1', 'pdsballtrainer', 'broodybullshit', 'hellahellakat_', 'McaCeo', 'serpicojones', 'kiyyyya', 'Naxer358', 'annmarkk', 'AStateWB', 'Deathbyfuego', 'adaliaaaa', 'xobriiiiii_', 'Caaaae_', 'legendarylovers', 'Natattack1310', 'NikkiB1391', '__therealyonna', 'AllyIrwin1994', 'HidingKala', 'alanislo', 'BestieBessie', 'AshleyCaliel', 'cmxaguilar', 'Imnicoler_', 'C_Wallis94', 'SeeSmiley', 'treannanicole', 'kemumm', 'Nick_Astalos', 'XxScrapyXx', 'emknott7', 'shereenzink', 'bacicchetti', 'Kennethmd', 'deionsbae', 'abbiiiie_', '_keishlaNicole_', 'hellaolzanski', '5th_HarmonyPH', 'SheltonS_', 'tjgonzales31', 'CollierMcKenzie', 'pxtriciaclaire', 'HiItsBritani', 'MrDimBri2U', 'BeardHallahan', 'brightsthgil', 'SugarNSpiceEmma', 'k95taylor', 'cvictoriaaaa_', 'Amarief10', 'TimonLow', 'Mardigroan', 'lenaisabelxo', 'Trendy_FLACKO', 'ishC27', 'DelonteHarrell', 'Urichinan', 'LewLewSmyles', 'divinadanikey', 'mackenziexrusso', 'BrianasNicoles', 'lady_worm', 'Alison_Renee16', 'DayraAceituno', 'bewitchednarry', 'dradiolampung', 'httpxkaren', 'DeathspeakSA', 'gabolgar', 'OhLowe', 'staystills', 'SheDJXMafia', 'MONhawk', 'EthanGassman', 'Kelsie_LeeAnne', 'SteveLemongello', 'WhitneyAndrus', 'Laura_Joner', 'NoviaDeJustin_B', 'hesborn94andi98', 'mboomhower', 'vanesarobles9', 's1s887', 'deliaxcor', 'Time_Consumer28', 'Mr_EmpireMinded', 'LoLoPhunnySingh', 'Lomzi89', 'jenb8675', 'aleman__b', 'sammenchetti', 'boostedbry', 'williamsbnn24', 'MakiahImani', 'bman432', 'JustinWonkaDots', '_Jeg_', 'CarlaLyoness', 'PongoMan88', 'MPCaraturo', 'blissfulester', 'lindseynalley26', 'AlexandraAnna17', 'lilhambotshelly', 'Tielurbame', 'Musics_Thoughts', 'tashalynnx333', '__BitchSHUTUP', 'QueenOfTHEplebs', 'mckennakoenig', 'mcshuttera', 'BobbieCRIES', 'Mahi_The_Giant', 'I_BN_The_CLOUDS', 'TcTheGrave', 'MaccaRace_', 'A_gligs', 'megangendron14', 'sconstantinoo', 'avonstae', 'brittneyliner8', 'Amiralynn', 'Twin_nicki', 'JonnySmith904', 'joewillij', 'jaylj__', '_AshleyMarie22', 'JckDvd', 'Ainin_Afezan', 'bbygingerbread', 'JCal_88', 'zuckerbitch', 'ayoKENfolk', 'JamieKilpack', 'csismyendgame', 'Rivera_300', 'fatalitiess', 'JJStankevitz', 'gpacheco1230', 'GetiganLoranel', 'SunithaNahar', 'mmicchheelleee', 'emmapepperall', 'TheReal_Beal', 'Kandi_Kouture_', 'ScottDahm', 'moshlyfe', 'misswavy__', 'HellcatPerez', 'TheResilientEzi', 'courtne53652006', 'mintrisgi', 'Im_Noizzy', 'MrErfortCMS205', 'LaBoo_', 'queenjunwhore', 'ZefronsNinja', 'Ewnoleave', 'uhhhbel', 'melissafayad']
'''
usernames = ['hapababee', 'sleeepycurtis', 'fuckalzheimers', 'mattytalks', 'jenbabeeey', 'sabrinamelodies', 'Tinder23', 'carinabizarro', 'Mason_Complains', 'moonlightsfroot', 'beaninabeanie', 'SchomerSierra', 'reedenstein', 'Rememberandhope', 'nickhankes16', '_aaaariel', 'NotCecilio', 'jull17nna', 'IKUWA6_2016', 'hesborn94andi98', 'gabby2k18', 'danceadaisy', 'namelessvenussa', 'arturoclingan', 'AmigosInDanger', 'Maria_2793', 'adamTwright', 'saxahoya', 'PIZZAxGREASE', 'DustinFisher4', 'shanecareyy', 'ItsBeeForBells', 'taranicholle97', 'pr3ttyj_', 'al_moosy111', '_kybearr', 'stephg1996', 'Lex_Zimmy', 'HAROLDRUINEDME2', 'KissMyTashy', '_SimonSaid_', 'kojodm3', 'YupItsJamil', 'jaassssm', 'sm0landcurly', 'thatzmarcosb', 'bagchinirmalya', 'stephen_minnow', 'L_R_Bauer', '_followMYpaige', 'SharpTusk', 'triciawarren_', 'missaxmoon', 'kaitlan4', 'JanoMichelle', 'iamchuyyyy', 'twdismyfamliy', 'paige_shearer', 'dauzataddict', 'jane_stahl', 'Grey280', 'lukecalmikeashx', 'angelaplusradar', 'ID0ntGivaFuck', 'LickMyFairyDust', 'atlcasxy', 'the_tola', 'LadyHawkins', 'asmilecanlie', 'alia_rex1', 'pdsballtrainer', 'broodybullshit', 'hellahellakat_', 'McaCeo', 'serpicojones', 'kiyyyya', 'Naxer358', 'annmarkk', 'AStateWB', 'Deathbyfuego', 'adaliaaaa', 'xobriiiiii_', 'Caaaae_', 'legendarylovers', 'Natattack1310', 'NikkiB1391', '__therealyonna', 'AllyIrwin1994', 'HidingKala', 'alanislo', 'BestieBessie', 'AshleyCaliel', 'cmxaguilar', 'Imnicoler_', 'C_Wallis94', 'SeeSmiley', 'treannanicole', 'kemumm', 'Nick_Astalos', 'XxScrapyXx', 'emknott7', 'shereenzink', 'bacicchetti', 'Kennethmd', 'deionsbae', 'abbiiiie_', '_keishlaNicole_', 'hellaolzanski', '5th_HarmonyPH', 'SheltonS_', 'tjgonzales31', 'CollierMcKenzie', 'pxtriciaclaire', 'HiItsBritani', 'MrDimBri2U', 'BeardHallahan', 'brightsthgil', 'SugarNSpiceEmma', 'k95taylor', 'cvictoriaaaa_', 'Amarief10', 'TimonLow', 'Mardigroan', 'lenaisabelxo', 'Trendy_FLACKO', 'ishC27', 'DelonteHarrell', 'Urichinan', 'LewLewSmyles', 'divinadanikey', 'mackenziexrusso', 'BrianasNicoles', 'lady_worm', 'Alison_Renee16', 'DayraAceituno', 'bewitchednarry', 'dradiolampung', 'httpxkaren', 'DeathspeakSA', 'gabolgar', 'OhLowe', 'staystills', 'SheDJXMafia', 'MONhawk', 'EthanGassman', 'Kelsie_LeeAnne', 'SteveLemongello', 'WhitneyAndrus', 'Laura_Joner', 'NoviaDeJustin_B', 'hesborn94andi98', 'mboomhower', 'vanesarobles9', 's1s887', 'deliaxcor', 'Time_Consumer28', 'Mr_EmpireMinded', 'LoLoPhunnySingh', 'Lomzi89', 'jenb8675', 'aleman__b', 'sammenchetti', 'boostedbry', 'williamsbnn24', 'MakiahImani', 'bman432', 'JustinWonkaDots', '_Jeg_', 'CarlaLyoness', 'PongoMan88', 'MPCaraturo', 'blissfulester', 'lindseynalley26', 'AlexandraAnna17', 'lilhambotshelly', 'Tielurbame', 'Musics_Thoughts', 'tashalynnx333', '__BitchSHUTUP', 'QueenOfTHEplebs', 'mckennakoenig', 'mcshuttera', 'BobbieCRIES', 'Mahi_The_Giant', 'I_BN_The_CLOUDS', 'TcTheGrave', 'MaccaRace_', 'A_gligs', 'megangendron14', 'sconstantinoo', 'avonstae', 'brittneyliner8', 'Amiralynn', 'Twin_nicki', 'JonnySmith904', 'joewillij', 'jaylj__', '_AshleyMarie22', 'JckDvd', 'Ainin_Afezan', 'bbygingerbread', 'JCal_88', 'zuckerbitch', 'ayoKENfolk', 'JamieKilpack', 'csismyendgame', 'Rivera_300', 'fatalitiess', 'JJStankevitz', 'gpacheco1230', 'GetiganLoranel', 'SunithaNahar', 'mmicchheelleee', 'emmapepperall', 'TheReal_Beal', 'Kandi_Kouture_', 'ScottDahm', 'moshlyfe', 'misswavy__', 'HellcatPerez', 'TheResilientEzi', 'courtne53652006', 'mintrisgi', 'Im_Noizzy', 'MrErfortCMS205', 'LaBoo_', 'queenjunwhore', 'ZefronsNinja', 'Ewnoleave', 'uhhhbel', 'melissafayad']

for user in usernames:
    print user
    a = printUser(user)
    if a == 0:
        break
    print '\n================== \n'

    