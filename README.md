
# Unofficial Google Lyrics API

An unofficial API that scrapes Google for music lyrics.



## Usage of API

#### Find lyrics of the song with given artist and name.

```http
  GET /api/{artist_name}/{song_name}
```

| Parametre | Tip     | Açıklama                       |
| :-------- | :------- | :-------------------------------- |
| `artist_name`      | `string` | **Required**. Name of the artist|
| `song_name`      | `string` | **Required**. Name of the song|


#### Find lyrics of the song that is currently playing on Spotify.

```http
  GET /api/current
```



  