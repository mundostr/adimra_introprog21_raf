import requests as req

URL = "http://ergast.com/api/f1/current/driverStandings.json"

solicitud = req.get(URL)

if (solicitud.status_code == 200):
	solicitudJson = solicitud.json()
	rankingPilotos = solicitudJson["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
	mVerstappen = rankingPilotos[0]
	print(rankingPilotos)
