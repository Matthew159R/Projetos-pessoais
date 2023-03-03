const box = document.querySelector('.box')
const body = document.querySelector('body')

Array.from(box.children).forEach(element => {
  element.classList.add('caixas')
})

box.addEventListener('click', event => {
  Array.from(box.children).forEach(element => {
    if (element === event.target) {
      if (element.textContent.includes('Vermelho')) {
        body.style.backgroundColor = 'red'
      } else if (element.textContent.includes('Amarelo')) {
        body.style.backgroundColor = 'yellow'
      } else if (element.textContent.includes('Laranja')) {
        body.style.backgroundColor = 'orange'
      } else if (element.textContent.includes('Azul')) {
        body.style.backgroundColor = 'blue'
      } else if (element.textContent.includes('Rosa')) {
        body.style.backgroundColor = 'pink'
      }else if (element.textContent.includes('Preto')) {
        body.style.backgroundColor = 'black'
      }else if (element.textContent.includes('Roxo')) {
        body.style.backgroundColor = 'blueviolet'
      }else if (element.textContent.includes('Marrom')) {
        body.style.backgroundColor = 'brown'
      }
    }
  })
})

function mostrarValor() {

    var inputElement = document.getElementById("myInput")
    
    var valor = inputElement.value
    
    var resultadoElement = document.getElementById("resultado")
    
    resultadoElement.innerHTML = "Seu nome é : " + valor
}

function apagarValor() {
    let resultadoElement = document.getElementById('resultado')
  resultadoElement.innerHTML = ''
}


