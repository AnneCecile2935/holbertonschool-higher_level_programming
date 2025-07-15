// On sélectionne l'élément avec l'id "add_item"
document.querySelector('#add_item')
  // On ajoute un écouteur d'événement pour détecter les clics sur cet élément
  .addEventListener('click', () => {
    // À chaque clic, on crée un nouvel élément <li>
    const newItem = document.createElement('li');

    // On définit le contenu texte de ce nouvel élément <li> à "Item"
    newItem.textContent = 'Item';

    // On sélectionne la liste (élément avec la classe "my_list")
    // et on ajoute le nouvel élément <li> à la fin de cette liste
    document.querySelector('.my_list').appendChild(newItem);
  });
