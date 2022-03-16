// == (comparação implícita)

const numero = 5;
const texto = "5";

console.log(numero === texto)

//typeof
console.log(typeof numero)
console.log(typeof texto)

// == compara apenas o valor
// === compara também o tipo de dado
// Para equalizar duas variáveis, é considerado boa pratica sempre comparar com === e se preciso alterar o tipo de dado explicitamente antes da comparação:
// Number("valornumerico") ou String(5)
