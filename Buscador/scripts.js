const imagens = document.querySelector('.img')

const form = document.querySelector('form')

const input = document.querySelector('input')

let children = Array.from(imagens.children)

children.forEach(img => {
    img.addEventListener('click', event => {
        let clickedElement = event.target

        if(clickedElement === children[0]){
            form.action = 'https://www.youtube.com/search'

        }else if (clickedElement === childre[1]){
            form.action = 'https://www.google.com/search'
        }
    })
})


