import folium
import pandas

data = pandas.read_excel('list_of_latitudelongitude_of_cities_of_india.xlsx')

lat = list(data['Latitude'])
lon = list(data['Longitude'])
stat = list(data['States'])

def colorShow(lt):
    if lt < 15:
        return 'red'
    elif 15 <= lt < 30:
        return 'orange'
    else:
        return 'green'
map = folium.Map(location=[23.011513, 72.516938], zoom_start=5, tiles='OpenStreetMap')

fg = folium.FeatureGroup(name="My Map")
# add change circle view
for lt, lo, st in zip(lat,lon, stat):
    fg.add_child(folium.CircleMarker(location=[lt, lo], popup=st, fill_color=colorShow(lt), radius=7, color='grey', fill_opacity=0.7, fill=True))
# for lt, lo, st in zip(lat,lon, stat):
#     fg.add_child(folium.CircleMarker(location=[lt, lo], popup=st, icon=folium.Icon(color=colorShow(lt))))

map.add_child(fg)

map.save("mapping.html")