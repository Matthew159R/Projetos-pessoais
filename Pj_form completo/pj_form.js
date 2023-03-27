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

const regexPasswordRedBar = /^[a-z0-9]{1,6}$/
const regexPasswordYellowBar = /^[a-zA-Z0-9]{7,10}$/
const regexPasswordGreenBar = /^[a-zA-Z0-9]{11,}$/


password.addEventListener('keyup', () => {
 if(regexPasswordRedBar.test(password.value)) {
    media.textContent = ''
    forte.textContent = ''
    fraca.textContent = 'Senha fraca'
    fraca.style.color = 'red'
    bar.setAttribute('class', 'red_bar')
 }else if(regexPasswordYellowBar.test(password.value)) {
    fraca.textContent = ''
    forte.textContent = ''
    bar.setAttribute('class', 'yellow_bar')
    media.textContent = 'Senha media'
    media.style.color = 'yellow'
 }else if(regexPasswordGreenBar.test(password.value)) {
    fraca.textContent = ''
    media.textContent = ''
    forte.textContent = 'Senha forte'
    forte.style.color = 'green'
    bar.setAttribute('class', 'green_bar')
 }else {
    fraca.textContent = ''
    media.textContent = ''
    forte.textContent = ''
    bar.setAttribute('class', '')
 }
  
})




button.addEventListener('click', event => {
  
    if (!email.value || !password.value || !nome.value) {

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
    }
})






