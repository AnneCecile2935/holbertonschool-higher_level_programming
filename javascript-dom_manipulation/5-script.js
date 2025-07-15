// On sélectionne l'élément avec l'id "update_header"
document.querySelector('#update_header')
  // On ajoute un écouteur d'événement qui réagit au clic sur cet élément
  .addEventListener('click', () => {
    // Quand on clique, on sélectionne l'élément <header> de la page
    document.querySelector('header').textContent = 'New Header!!!';
    // Et on change son contenu texte en "New Header!!!"
  });
