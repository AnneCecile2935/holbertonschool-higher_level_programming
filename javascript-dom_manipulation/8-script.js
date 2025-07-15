// On attend que le contenu HTML de la page soit complètement chargé
document.addEventListener('DOMContentLoaded', () => {
  // On envoie une requête à l'API hellosalut pour obtenir la traduction de "hello" en français
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    // Quand la réponse est reçue, on la convertit en objet JSON
    .then(response => response.json())
    // Une fois les données JSON prêtes
    .then(data => {
      // On sélectionne l'élément HTML qui a l'id "hello"
      const helloElement = document.getElementById('hello');
      // Si l'élément existe dans la page
      if (helloElement) {
        // On insère dans cet élément la traduction de "hello" (ex. : "Bonjour")
        helloElement.textContent = data.hello;
      }
    })
    // Si une erreur se produit (connexion perdue, API inaccessible, etc.)
    .catch(error => {
      // On affiche un message d'erreur dans la console du navigateur
      console.error('Erreur lors de la récupération du message de salutation :', error);
    });
});
