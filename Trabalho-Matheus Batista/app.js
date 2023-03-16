const button = document.querySelector('.button1')
const container = document.querySelector('.popup')
const fechar = document.querySelector('.fechar')

button.addEventListener('click', () => {
  container.setAttribute('class', 'popupinline')
  document.querySelector('body').style.backgroundColor = 'rgb(236, 224, 224)'
})

fechar.addEventListener('click', event => {
  const clickedElement = event.target 
  if(clickedElement) {
    container.style.display = 'none'
    document.querySelector('body').style.backgroundColor = 'white'
  }
})

