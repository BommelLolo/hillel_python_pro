import sqlite3


if __name__ == '__main__':
    query_1 = """SELECT t.Name FROM tracks t 
INNER JOIN genres g ON t.GenreId = g.GenreId
INNER JOIN media_types mt ON t.MediaTypeId = mt.MediaTypeId 
WHERE mt.Name = 'AAC audio file' and g.Name LIKE 'R%';"""
    with sqlite3.connect('chinook.db') as cursor:
        res = cursor.execute(query_1).fetchall()
    print(res)

    query_2 = """SELECT t.Name, MAX(t.Bytes) FROM tracks t
WHERE t.Milliseconds > 200 """
    with sqlite3.connect('chinook.db') as cursor:
        res = cursor.execute(query_2).fetchall()
    print(f"Name '{res[0][0]}', {res[0][1]} bytes")

    query_3 = """SELECT t.Name, a.Title FROM tracks t
INNER JOIN albums a ON t.AlbumId = a.AlbumId
JOIN playlist_track pt ON t.TrackId = pt.TrackId 
JOIN playlists p ON pt.PlaylistId = p.PlaylistId 
WHERE p.Name = 'TV Shows'"""
    with sqlite3.connect('chinook.db') as cursor:
        res = cursor.execute(query_3).fetchall()
    print(res)
