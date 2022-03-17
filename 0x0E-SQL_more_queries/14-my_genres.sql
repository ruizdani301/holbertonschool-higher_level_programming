-- Import the database dump from hbtn_0d_tvshows to your MySQL server

SELECT tv_genres.name
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name ASC;
