document.addEventListener('DOMContentLoaded', () => {
  const additem = document.getElementById('add_item');
  const removeItem = document.getElementById('remove_item');
  const clearList = document.getElementById('clear_list');
  const list = document.querySelector('.my_list');

  additem.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });
  removeItem.addEventListener('click', () => {
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });
  clearList.addEventListener('click', () => {
    list.innerHTML = '';
  });
});
