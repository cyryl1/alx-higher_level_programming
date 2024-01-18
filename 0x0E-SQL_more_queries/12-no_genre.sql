-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT t.title, IFNULL(g.genre_id, NULL)
        FROM tv_shows AS t
        LEFT JOIN tv_show_genres AS g
        ON g.show_id=t.id
	WHERE g.show_id IS NULL
ORDER BY t.title, g.genre_id ASC;
