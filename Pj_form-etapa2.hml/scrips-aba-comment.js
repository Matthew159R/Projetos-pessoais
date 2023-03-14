const avatar = document.querySelector('.avatar')
const avatarUsuario = document.querySelector('.avatarUsuario')
const username = document.querySelector('.username')
const button = document.querySelector('.ok')
const nome = document.querySelector('.comments h4')

let avatarChildren = Array.from(avatar.children)

avatarChildren.forEach(element => {
  element.addEventListener('click', event => {
    let clickedElement = event.target
    
    if (clickedElement === avatarChildren[1]) {
      avatarUsuario.src = 'Avatar1.png'
    } else if (clickedElement === avatarChildren[2]) {
      avatarUsuario.src = 'Avatar2.png'
    }
  })
})

button.addEventListener('click', event => {
  event.preventDefault()
  
  if (username.value.length < 2) {
    //Popup simples aqui
    alert('Seu username não pode estar vazio ou ser menor que 2 caracteres')
  }
  
  nome.textContent = username.value
  document.querySelector('.popup').style.display = 'none'
  document.querySelector('.content').style.display = 'block'
})
