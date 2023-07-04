// Converta o array "wrongDataFormat" para o objeto do comentário abaixo.

const wrongDataFormat = [
    'preto-PP',
    'preto-M',
    'preto-G',
    'preto-GG',
    'preto-GG',
    'branco-PP',
    'branco-G',
    'vermelho-M',
    'azul-XG',
    'azul-XG',
    'azul-XG',
    'azul-P'
  ]

const object = wrongDataFormat.reduce((acc, item) => {
  const [cor, tamanho] = item.split('-')

  if (!acc[cor]) {
    acc[cor] = {}
  }
  if (!acc[cor][tamanho]) {
    acc[cor][tamanho] = 0
  }

  acc[cor][tamanho]++
  return acc
}, {})

console.log(object)
  /*
    {
      preto: {
        PP: 1,
        M: 1,
        G: 1,
        GG: 2
      },
      branco: {
        PP: 1,
        G: 1
      },
      vermelho: {
        M: 1
      },
      azul: {
        XG: 3,
        P: 1
      }
    }
  */