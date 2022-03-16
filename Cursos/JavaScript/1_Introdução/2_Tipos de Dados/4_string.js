// var
var altura = 5;
var comprimento = 7;
var area
area = altura * comprimento;
console.log (area)


// let - Aceita mudança de valor
let altura = 5;
let comprimento = 7;
let forma = "retangulo"
let area = 0;

if (forma === "retangulo") {
  area = altura * comprimento;
} else {
  area = (altura * comprimento) / 2;
}
console.log(area)


// const - Não aceita mudança de valor
const altura = 5;
const comprimento = 7;
const forma = "triangulo";
let area = 0;

if (forma === "quadrado") {
  area = altura * comprimento;
} else {
  area = (altura * comprimento) / 2;
}
console.log(area)