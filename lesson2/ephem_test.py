import ephem
mars = ephem.Moon('2016/09/23')
mars = getattr(ephem, 'Mars')
mars = mars('2016/09/23')

planet = ephem.constellation(mars)
print(planet)