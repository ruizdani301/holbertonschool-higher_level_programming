-- Import the database dump from hbtn_0d_tvshows

SELECT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id;
