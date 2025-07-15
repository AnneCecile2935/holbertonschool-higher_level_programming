// On sélectionne l'élément avec l'id "red_header" (par exemple un bouton)
document.querySelector('#red_header')
  // On ajoute un écouteur d'événement qui se déclenche au clic sur cet élément
  .addEventListener('click', () => {
    // On sélectionne la balise <header> de la page
    // Puis on ajoute la classe CSS "red" à cet élément
    document.querySelector('header').classList.add('red');
  });
