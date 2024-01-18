-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshow.
SELECT t.title, IFNULL(g.name, NULL) AS name
  FROM tv_shows AS t
  LEFT JOIN tv_show_genres
  ON tv_show_genres.show_id = t.id
  LEFT JOIN tv_genres AS g
  ON tv_show_genres.genre_id = g.id
ORDER BY title, name;
