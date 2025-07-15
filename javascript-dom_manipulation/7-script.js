// On utilise fetch pour récupérer les données de l'API SWAPI (films)
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  // Quand on reçoit une réponse, on la transforme en JSON
  .then(response => response.json())

  // Une fois les données transformées, on peut les utiliser
  .then(data => {
    // data.results contient un tableau avec tous les films
    const movies = data.results;

    // On sélectionne l'élément <ul> avec l'ID "list_movies"
    const list = document.getElementById('list_movies');

    // Pour chaque film dans le tableau "movies"
    movies.forEach(movie => {
      // On crée un nouvel élément <li>
      const li = document.createElement('li');

      // On met le titre du film dans le <li>
      li.textContent = movie.title;

      // On ajoute le <li> à la liste <ul>
      list.appendChild(li);
    });
  })
  // En cas d'erreur (réseau, API, etc.), on affiche l'erreur dans la console
  .catch(error => {
    console.error('Erreur lors du chargement des films :', error);
  });
