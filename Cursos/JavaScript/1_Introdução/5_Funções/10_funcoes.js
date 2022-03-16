// funcoes
//Criandro função de printar
function imprimeTexto(texto) {
    console.log(texto)
}

// criando funcoes matematicas
function soma(v1, v2) { 
    return v1+v2
}

function subtracao(v1, v2) {
    return v1-v2
}

function multiplicacao(v1, v2) {
    return v1*v2
}

function divisao(v1, v2) {
    return v1/v2
}

//executando a função
imprimeTexto(`A soma entre os valores é igual a ${soma(10, 4)}`)
imprimeTexto(subtracao(25, 12))
imprimeTexto(multiplicacao(10, 4))
imprimeTexto(divisao(8,2))