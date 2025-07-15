// Attendre que tout le contenu HTML soit chargé avant d'exécuter le script
document.addEventListener('DOMContentLoaded', () => {
  // Sélectionner le bouton "Add item" par son id
  const additem = document.getElementById('add_item');
  // Sélectionner le bouton "Remove item" par son id
  const removeItem = document.getElementById('remove_item');
  // Sélectionner le bouton "Clear list" par son id
  const clearList = document.getElementById('clear_list');
  // Sélectionner la liste (ul) qui contient les <li> à modifier
  const list = document.querySelector('.my_list');
  // Quand on clique sur "Add item", on ajoute un nouvel élément <li> à la liste
  additem.addEventListener('click', () => {
    const newItem = document.createElement('li'); // Créer un nouvel élément <li>
    newItem.textContent = 'Item'; // Lui donner le texte "Item"
    list.appendChild(newItem); // L'ajouter à la fin de la liste
  });
  // Quand on clique sur "Remove item", on supprime le dernier <li> de la liste
  removeItem.addEventListener('click', () => {
    if (list.lastElementChild) { // Vérifie s'il y a au moins un élément dans la liste
      list.removeChild(list.lastElementChild); // Supprime le dernier enfant (dernier <li>)
    }
  });
  // Quand on clique sur "Clear list", on vide complètement la liste
  clearList.addEventListener('click', () => {
    list.innerHTML = ''; // Supprime tout le contenu HTML de la liste
  });
});
