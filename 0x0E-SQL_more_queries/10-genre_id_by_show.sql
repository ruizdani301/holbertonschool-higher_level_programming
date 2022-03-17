-- Import the database dump from hbtn_0d_tvshows
-- your MySQL server:

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_show
ON tv_show.id = tv_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
