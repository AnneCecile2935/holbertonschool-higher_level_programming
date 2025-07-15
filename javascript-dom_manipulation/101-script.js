// Attendre que le contenu HTML de la page soit complètement chargé
document.addEventListener('DOMContentLoaded', () => {
  // Récupérer le bouton sur lequel l'utilisateur va cliquer pour traduire
  const transbtn = document.getElementById('btn_translate');
  // Récupérer le champ où l'utilisateur entre le code langue (comme 'fr', 'es', 'en', etc.)
  const langcCode = document.getElementById('language_code');
  // Récupérer l'élément HTML où on va afficher la traduction de "Hello"
  const trad = document.getElementById('hello');
  // Ajouter un événement : quand on clique sur le bouton de traduction...
  transbtn.addEventListener('click', () => {
    // Appeler l’API avec le code langue choisi (ex: ?lang=fr)
    fetch('https://hellosalut.stefanbohacek.dev/?lang=' + langcCode.value)
      // Convertir la réponse en format JSON (objet utilisable en JS)
      .then(response => response.json())
      // Une fois la réponse reçue, afficher la traduction de "hello"
      .then(data => {
        trad.textContent = data.hello; // Afficher le mot "Hello" traduit dans l'élément avec l'id "hello"
      });
  });
});
