const password = document.querySelector('#senha')
const bar = document.querySelector('.bar_force_password')
const fraca = document.querySelector('.senha_fraca')
const media = document.querySelector('.senha_media')
const forte = document.querySelector('.senha_forte')
const pequena = document.querySelector('.senha_pequena')
const email = document.querySelector('#email')
const nome = document.querySelector('#name')
const button = document.querySelector('.continue')
const fechar = document.querySelector('.Fechar')
const popup = document.querySelector('.popup-wrapper')
const closeButton = document.querySelector('.popup-close')


password.addEventListener('input', function() {

const senha = password.value
    
if (senha.length <= 2) {
        
    fraca.innerHTML = ''
    bar.classList.remove('red_bar')
}else if (senha.length >= 3 && senha.length < 10) {
    fraca.innerHTML = 'Senha fraca'
    fraca.style.color = 'red'
    bar.classList.add('red_bar')
}else {
    fraca.innerHTML = ''
    bar.classList.remove('red_bar')
}

if (senha.length >= 10 && senha.length <= 15){
    media.innerHTML = 'Senha média'
    media.style.color = 'rgb(180, 180, 17)'
    bar.classList.add('yellow_bar')
}else {
    media.innerHTML = ''
    bar.classList.remove('yellow_bar')
}

if (senha.length > 15){
    forte.innerHTML = 'Senha forte'
    forte.style.color = 'green'
    bar.classList.add('green_bar')
}else {
    forte.innerHTML = ''
    bar.classList.remove('green_bar')
}
})


button.addEventListener('click', event => {
    if (!email.value || !password.value || !nome.value) {
        event.preventDefault()

        popup.style.display = 'inline'

        closeButton.addEventListener('click', () => {
            popup.style.display = 'none'
          })
          
          fechar.addEventListener('click', () => {
              popup.style.display = 'none'
          })
          
          popup.addEventListener('click', event => {
            const classNameOfClickedElement = event.target.classList[0]
            const shouldClosePopup = classNameOfClickedElement === 'popup-close' || classNameOfClickedElement === 'popup-link' || classNameOfClickedElement === 'popup-wrapper'
            
            if (shouldClosePopup) {
              console.log(classNameOfClickedElement)
              popup.style.display = 'none'
            }
          })   
    }else {
        document.querySelector('form').action = 'aba-comment.html'
        document.querySelector('form').submit()
    }
})






