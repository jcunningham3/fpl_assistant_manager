
jersey_list = [
    {
        'id': 1,
        'name': 'Arsenal',
        'jersey': '\static\img\jerseys\shirt_3-66_ars.webp',
        'jersey_goal': '\static\img\jerseys\arsg.webp'
    },
    {
        'id': 2,
        'name': 'Aston Villa',
        'jersey': '\static\img\jerseys\shirt_7-66_avl.webp',
        'jersey_goal': '\static\img\jerseys\avlg.webp'
    },
    {
        'id': 3,
        'name': 'Brenton',
        'jersey': '\static\img\jerseys\bre.webp',
        'jersey_goal': '\static\img\jerseys\breg.webp'
    },
    {
        'id': 4,
        'name': 'Brigton Hove Albion',
        'jersey': '\static\img\jerseys\shirt_36-66_bha.webp',
        'jersey_goal': '\static\img\jerseys\shirt_90_1-66_bur_g.webp'
    },
    {
        'id': 5,
        'name': 'Burnley',
        'jersey': '\static\img\jerseys\shirt_90-66_bur.webp',
        'jersey_goal': '\static\img\jerseys\shirt_90_1-66_burg.webp'
    },
    {
        'id': 6,
        'name': 'Chelsea',
        'jersey': '\static\img\jerseys\che.webp',
        'jersey_goal': '\static\img\jerseys\cheg.webp'
    },
    {
        'id': 7,
        'name': 'Crystal Palace',
        'jersey': '\static\img\jerseys\cry.webp',
        'jersey_goal': '\static\img\jerseys\cryg.webp'
    },
    {
        'id': 8,
        'name': 'Everton',
        'jersey': '\static\img\jerseys\eve.webp',
        'jersey_goal': '\static\img\jerseys\eveg.webp'
    },
    {
        'id': 9,
        'name': 'Leicester City',
        'jersey': '\static\img\jerseys\lei.webp',
        'jersey_goal': '\static\img\jerseys\leig.webp'
    },
    {
        'id': 10,
        'name': 'Leeds United',
        'jersey': '\static\img\jerseys\lee.webp',
        'jersey_goal': '\static\img\jerseys\leeg.webp'
    },
    {
        'id': 11,
        'name': 'Liverpool',
        'jersey': '\static\img\jerseys\liv.webp',
        'jersey_goal': '\static\img\jerseys\livg.webp'
    },
    {
        'id': 12,
        'name': 'Manchester City',
        'jersey': '\static\img\jerseys\mci.webp',
        'jersey_goal': '\static\img\jerseys\mcig.webp'
    },
    {
        'id': 13,
        'name': 'Manchester United',
        'jersey': '\static\img\jerseys\mun.webp',
        'jersey_goal': '\static\img\jerseys\mung.webp'
    },
    {
        'id': 14,
        'name': 'Newcastle United',
        'jersey': '\static\img\jerseys\shirt_4-66_new.webp',
        'jersey_goal': '\static\img\jerseys\newg.webp'
    },
    {
        'id': 15,
        'name': 'Norwich City',
        'jersey': '\static\img\jerseys\nor.webp',
        'jersey_goal': '\static\img\jerseys\norg.webp'
    },
    {
        'id': 16,
        'name': 'Southampton',
        'jersey': '\static\img\jerseys\sou.webp',
        'jersey_goal': '\static\img\jerseys\soug.webp'
    },
    {
        'id': 17,
        'name': 'Tottenham',
        'jersey': '\static\img\jerseys\shirt_6-66_tot.webp',
        'jersey_goal': '\static\img\jerseys\totg.webp'
    },
    {
        'id': 18,
        'name': 'Watford',
        'jersey': '\static\img\jerseys\wat.webp',
        'jersey_goal': '\static\img\jerseys\watg.webp'
    },
    {
        'id': 19,
        'name': 'West Ham United',
        'jersey': '\static\img\jerseys\whu.webp',
        'jersey_goal': '\static\img\jerseys\whug.webp'
    },
    {
        'id': 20,
        'name': 'Wolverhampton',
        'jersey': '\static\img\jerseys\wol.webp',
        'jersey_goal': '\static\img\jerseys\wolg.webp'
    }
]

def my_jersey():
    me = 6
    for jersey in jersey_list:
        if jersey['id'] == me:
            print(jersey['jersey'])

# my_jersey()
