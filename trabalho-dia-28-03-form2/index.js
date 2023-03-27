const password = document.querySelector('#password')
const button = document.querySelector('.btn')
const bar = document.querySelector('.bar')
const text = document.querySelector('.text')

password.addEventListener('keyup', event => {
    if(password.value.length > 2) {
        bar.setAttribute('class', 'red-bar')
        text.textContent = 'Senha fraca'
        text.setAttribute('class', 'red-text')
        
    }else if(password.value.length <= 2) {
        bar.setAttribute('class', '')
        text.setAttribute('class', '')
        text.textContent = ''
    }
})

