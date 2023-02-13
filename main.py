import pandas as pd
import numpy as np
import os

path = 'data/definition.csv'
all_provinces = ""
sea_provinces = ""
lake_provinces = ""
text = ""

def writef(path, con):
    f = open(path, 'w')
    f.write(con)
    f.close

df = pd.read_csv(path,sep=";",header=None)

for item in df.loc[:,[0]].values:
    all_provinces += str(item[0]) + " "
for item in df[df[5] == 'Sea'][0].values:
    sea_provinces += str(item) + " "
for item in (df[df[5] == 'Lake'][0].values):
    lake_provinces += str(item) + " "

os.makedirs('out/map', exist_ok=True)

writef('out/map/default.map', "width = 5632 \nheight = 2048 \nmax_provinces =" + str(len(df) + 1) + "\nsea_starts = {" + sea_provinces +"} \nonly_used_for_random = {} \nlakes = {" + lake_provinces + "} \nforce_coastal = {} \ntree = {}" + '\ndefinitions = "definition.csv" \nprovinces = "provinces.bmp" \npositions = "positions.txt" \nterrain = "terrain.bmp" \nrivers = "rivers.bmp" \nterrain_definition = "terrain.txt" \nheightmap = "heightmap.bmp" \ntree_definition = "trees.bmp" \ncontinent = "continent.txt" \nadjacencies = "adjacencies.csv" \nclimate = "climate.txt" \nregion = "region.txt" \nsuperregion = "superregion.txt" \narea = "area.txt" \nprovincegroup = "provincegroup.txt" \nambient_object = "ambient_object.txt" \nseasons = "seasons.txt" \ntrade_winds = "trade_winds.txt"')
writef('out/map/area.txt', "black_sea_area = {" + all_provinces + "}") #一時的に全プロビを黒海地域に入れる
writef('out/map/climate.txt', "tropical = {" + all_provinces + "}") #一時的に全プロビを熱帯に
writef('out/map/continent.txt', "europe = {" + all_provinces + "}") #一時的に全プロビをヨーロッパに
writef('out/map/region.txt', "france_region = {black_sea_area}") #一時的に地域をフランスに
writef('out/map/superregion.txt', "india_superregion = {france_region}") #一時的にｚ全リージョンをインドに

for item in df.loc[:,[0]].values:
    text += str(item[0]) + " = {position={0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000} \nrotation={0.000 0.000 0.000 0.000 0.000 0.000 0.000} \nheight={0.000 0.000 0.000 0.000 0.000 0.000 0.000}}\n"
writef('out/map/positions.txt',text) 
