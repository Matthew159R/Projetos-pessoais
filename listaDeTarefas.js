const button = document.querySelector('button')

const ul = document.querySelector('ul')


const lis = document.querySelectorAll('li')

lis.forEach(li => {
    li.addEventListener('click', event => {
        const clickedElement = event.target

        clickedElement.innerHTML = '✔️'

        clickedElement.style.textAlign = 'center'

        clickedElement.style.backgroundColor = 'blue'

      //clickedElement.remove()

    })
})
button.addEventListener('click', () => {
  document.querySelector('h2').remove()
})

button.addEventListener('click', () => {
    let item = prompt('Nome do item')
    const li = document.createElement('h3')
    const p = document.createElement('p')
    
    p.textContent = ''
    li.textContent = `${item}`
    ul.append(li)
    li.style.width = '200px'
    li.style.height = '30px'
    li.style.color = 'green'
    li.style.borderRadius = '25px'

    ul.append(p)

    
    li.style.backgroundColor = 'lightgreen'

    

    li.addEventListener('click', event => {
        const clickedElement = event.target

        clickedElement.innerHTML = '✔️'

        clickedElement.style.textAlign = 'center'

        clickedElement.style.backgroundColor = 'blue'
    })
})
