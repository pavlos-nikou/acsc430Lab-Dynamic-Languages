distanceStr = input("Enter Distance (example : 6'1\"): ")
# distanceStr = "20'10\"2000"

distance = distanceStr.split("'")
feetPart = float(distance[0])
inchesPart = float(distance[1][0:-1])

convFeet = feetPart + inchesPart/12
convYards = convFeet/3
convFurlongs = convYards/220
convMiles = convFurlongs/8
convLeague = convMiles/3

print(f'\tFeet: {convFeet:>18.2f} feet')
print(f'\tYards: {convYards:>17.2f} yards')
print(f'\tFurlongs: {convFurlongs:>14.2f} furlongs')
print(f'\tMiles: {convMiles:>17.2f} miles')
print(f'\tLeagues: {convLeague:>15.2f} leagues')