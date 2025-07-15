// On sélectionne l'élément avec l'id "red_header" (par exemple un bouton)
document.querySelector('#red_header')
  // On ajoute un écouteur d'événement qui se déclenche au clic sur cet élément
  .addEventListener('click', function () {
    // On sélectionne la balise <header> de la page
    // Puis on modifie directement la couleur du texte en rouge (#FF0000)
    document.querySelector('header').style.color = '#FF0000';
  });
