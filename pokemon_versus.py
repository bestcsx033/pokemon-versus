# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:17:30 2021

@author: ChrisX
"""

import pandas as pd
pokemon_data=pd.read_excel('pokemon.xlsx')
list_name=[]
list_attack=[]
list_defense=[]
list_hp=[]
list_spattack=[]
list_spdefense=[]
list_speed=[]
list_type1=[]
for i in range(800):
    list_name.append(pokemon_data.loc[i][1])
    list_hp.append(pokemon_data.loc[i][5])    
    list_attack.append(pokemon_data.loc[i][6])    
    list_defense.append(pokemon_data.loc[i][7])
    list_spattack.append(pokemon_data.loc[i][8])    
    list_spdefense.append(pokemon_data.loc[i][9])
    list_speed.append(pokemon_data.loc[i][10])
    list_type1.append(pokemon_data.loc[i][2])

pokemon_dic={}
for i in range(800):
    pokemon_dic[list_name[i]]=[list_hp[i],
                               list_attack[i],
                               list_defense[i],
                               list_spattack[i],
                               list_spdefense[i],
                               list_speed[i],
                               list_type1[i]]


    
pokemon_kz_chart=pd.read_excel('pokemon_kz.xlsx') 
shuxing=[]
for i in range(18):
    shuxing.append(pokemon_kz_chart['属性'][i])
    
import random as r
def versus(pokemon_1,pokemon_2):
    if pokemon_dic[pokemon_2][5]>pokemon_dic[pokemon_1][5]:
        pokemon1,pokemon2=pokemon_2,pokemon_1
    else:
        pokemon1,pokemon2=pokemon_1,pokemon_2
    hp1=pokemon_dic[pokemon1][0]
    attack1=pokemon_dic[pokemon1][1]
    defense1=pokemon_dic[pokemon1][2]
    spattack1=pokemon_dic[pokemon1][3]
    spdefense1=pokemon_dic[pokemon1][4]
    type1=pokemon_dic[pokemon1][6]
    hp2=pokemon_dic[pokemon2][0]
    attack2=pokemon_dic[pokemon2][1]
    defense2=pokemon_dic[pokemon2][2]
    spattack2=pokemon_dic[pokemon2][3]
    spdefense2=pokemon_dic[pokemon2][4]
    type2=pokemon_dic[pokemon2][6]    
    kz1=pokemon_kz_chart[type2][shuxing.index(type1)]
    kz2=pokemon_kz_chart[type1][shuxing.index(type2)]            
    Round=0
    while hp1 >0 and hp2 >0:
        if Round//2 ==0:
            if r.choice(['attack','superattack'])=='attack':
                attack1_=attack1*kz1*(r.choices([1,0.5,2],[0.8,0.1,0.1])[0])
                if attack1_>defense2:
                    hp2=hp2-(attack1_-defense2)
            else:
                spattack1_=spattack1*kz1*(r.choices([1,0.5,2],[0.8,0.1,0.1])[0])
                if spattack1_>spdefense2:
                    hp2=hp2-(spattack1_-spdefense2)
            Round=Round+1
        else:
            if r.choice(['attack','superattack'])=='attack':
                attack2_=attack2*kz2*(r.choices([1,0.5,2],[0.8,0.1,0.1])[0])
                if attack2_>defense1:
                    hp1=hp1-(attack2_-defense1)
            else:
                spattack2_=spattack2*kz2*(r.choices([1,0.5,2],[0.8,0.1,0.1])[0])
                if spattack2_>spdefense1:
                    hp1=hp1-(spattack2_-spdefense1)
            Round=Round+1
        if Round>=300:
            break
    if hp1<=0:
        print(f'The winner is {pokemon2}')
        return pokemon2
    elif hp2<=0:
        print(f'The winner is {pokemon1}')
        return pokemon1
    else:
        print('draw')
        return 0.5
            
def auto_versus(pokemon,times):
    win=0
    lose=0
    draw=0
    for i in range(times):
        pokemon_r=list_name[r.randint(0, 799)]
        if versus(pokemon, pokemon_r)==pokemon:
            win=win+1
        elif versus(pokemon, pokemon_r)==pokemon_r:
            lose=lose+1
        else: 
            draw=draw+1
    return(win,draw,lose)
    
pokemon_versus_data={}
for i in range(800):
    pokemon_versus_data[list_name[i]]=auto_versus(list_name[i], 100)
    

            
        

            
    
