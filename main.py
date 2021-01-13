import requests
import plotly.graph_objects as go


movieList = ['1726-iron-man', '1724-the-incredible-hulk', '10138-iron-man-2', '10195-thor', '1771-captain-america-the-first-avenger', '24428-the-avengers','68721-iron-man-3' '76338-thor-the-dark-world', '100402-captain-america-the-winter-soldier', '118340-guardians-of-the-galaxy', '99861-avengers-age-of-ultron', '102899-ant-man', '271110-captain-america-civil-war', '284052-doctor-strange', '283995-guardians-of-the-galaxy-2', '315635-spider-man-homecoming', '284053-thor-ragnarok', '284054-black-panther', '299536-avengers-infinity-war', '363088-ant-man-and-the-wasp', '299537-captain-marvel', '299534-avengers-endgame',]
movie = "";
ratingsList = []
apikey = "85dc8339429fa743fb99f73db9e29777"
graphList = []
max = 0;
maxIndex = 0;

for entry in movieList:
    movie = entry
    url = "https://api.themoviedb.org/3/movie/" + movie + "?api_key=" + apikey + "&language=en-US"
    response = requests.request("GET", url)
    voteAverage = response.text.find("vote_average")
    currRating = response.text[voteAverage + 14] + response.text[voteAverage + 15] + response.text[voteAverage + 16]
    title = response.text.find("original_title")
    endTitle = response.text.find("overview")
    tempTitle = endTitle - title;
    currTitle = ""
    for x in range(title + 17, title + tempTitle - 3):
        currTitle = currTitle + response.text[x]
    currRating = float(currRating)
    ratingsList.append(currRating)
    graphList.append(currTitle)
    if currRating > max:
        maxIndex = len(ratingsList)
        max = currRating

colors = ['lightslategray',] * len(ratingsList)
colors[maxIndex - 1] = 'crimson'
fig = go.Figure([go.Bar(x=graphList, y=ratingsList, marker_color=colors)])
fig.update_yaxes(range=[0, 10])
fig.show()


