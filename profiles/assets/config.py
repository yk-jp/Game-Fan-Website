import os

gameType = ['fps','pazzle','rpg']

games = {
        'fps':{
        'type':'fps',
        'img': os.path.join('img','gameType','fps.jpg'),
        'about':' fps \
                is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown '
        ,
        'rule':' fps rules \
                is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also'
        },
        'pazzle':{
        'type':'pazzle',
        'img': os.path.join('img','gameType','pazzle.png'),
        'about':' pazzle \
                is simply dummy text of the printing and typesetting industry. Lore'
        ,
        'rule':' pazzle rules \
                is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type a'
        },
        'rpg':{
        'type':'rpg',
        'img': os.path.join('img','gameType','rpg.jpg'),
        'about':' rpg \
                is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text unknown printer took a galley of type and scrambled it to make a type specimen book. It eets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'
        ,
        'rule':' pazzle rules \
                is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'
        }
}

notables = {
        'fps':[
                {
                'name': 'fps_player_1',
                'img':'',
                'about':'fps_player_1\
                         ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typeset'
                },
                {
                'name': 'fps_player_2',
                'img':'',
                'about':'fps_player_2 \
                        enturies, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'
                },
                {
                'name': 'fps_player_3',
                'img':'',
                'about':'fps_player_3 \
                         in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldu'
                }
        ],
        'pazzle':[
                {
                'name': 'pazzle_player_1',
                'img':'',
                'about':'pazzle_player_1\
                         ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only filease of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software live centuries, but also the leap into electronic typeset'
                },
                {
                'name': 'pazzle_player_2',
                'img':'',
                'about':'pazzle_player_2 \
                         ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survi the leap into electronic typeset'
                },
                {
                'name': 'pazzle_player_3',
                'img':'',
                'about':'pazzle_player_3 \
                         ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survi thand typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galleye leap into electronic typeset'
                }
        ],
        'rpg':[
                {
                'name': 'rpg_player_1',
                'img':'',
                'about':'rpg_player_1\
                         ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only filease of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software live centuries, but also the leap into electronic typeset'
                },
                {
                'name': 'rpg_player_2',
                'img':'',
                'about':'rpg_player_2\
                         ever since the 1500s, when an unknown printer took a ga'
                },
                {
                'name': 'rpg_player_3',
                'img':'',
                'about':'rpg_player_3\
                         ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived ne live centuries, but also the leap into electronic typeset'
                }
        ]
}
        


config = {
  'gameType':gameType,
  'games':games
}