// On envoie une requête GET à l'API pour récupérer les infos du personnage ID 5
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  // On transforme la réponse en JSON (objet JavaScript)
  .then(response => response.json())

  // Quand les données sont prêtes, on les utilise
  .then(data => {
    // On récupère l'élément avec l'ID "character"
    const character = document.getElementById('character');

    // On affiche le nom du personnage dans cet élément
    character.textContent = data.name;
  })

  // Si une erreur survient (réseau, mauvaise réponse, etc.)
  .catch(error => {
    // On affiche un message d'erreur dans la console
    console.error('Erreur lors du chargement du personnage :', error);
  });
