-- Sélectionne le nom du genre et le nombre de shows associés
SELECT
  tv_genres.name AS genre,               -- Le nom du genre
  COUNT(tv_show_genres.show_id) AS number_of_shows -- Le nombre de shows liés à ce genre
FROM
  tv_genres                              -- Table des genres
JOIN
  tv_show_genres ON tv_genres.id = tv_show_genres.genre_id  -- Jointure pour associer les shows aux genres
GROUP BY
  tv_genres.id
HAVING
	number_of_shows > 0                          -- Regroupe les résultats par genre
ORDER BY
  number_of_shows DESC;                          -- Trie les résultats par nombre de shows décroissant
