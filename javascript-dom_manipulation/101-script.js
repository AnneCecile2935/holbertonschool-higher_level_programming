document.addEventListener('DOMContentLoaded', () => {
  const transbtn = document.getElementById('btn_translate');
  const langcCode = document.getElementById('language_code');
  const trad = document.getElementById('hello');

  transbtn.addEventListener('click', () => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=' + langcCode.value)
      .then(response => response.json())
      .then(data => {
        trad.textContent = data.hello;
      });
  });
});
