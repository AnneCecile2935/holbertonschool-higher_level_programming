// On sélectionne l'élément avec l'id "toggle_header" (par exemple un bouton)
document.querySelector('#toggle_header')
  // On ajoute un écouteur d'événement qui se déclenche au clic sur cet élément
  .addEventListener('click', () => {
    // On sélectionne la balise <header> de la page
    // Puis on bascule (ajoute ou enlève) la classe CSS "red"
    document.querySelector('header').classList.toggle('red');

    // Ensuite, on fait pareil avec la classe CSS "green"
    // Si "green" est présente, elle est retirée ; sinon, elle est ajoutée
    document.querySelector('header').classList.toggle('green');
  });
