const nome = "Rodolfo"
const idade = 2021 - 1985;
const cidadeDeNascimento = "São Paulo"

// const apresentacao = "meu nome é " + nome + ", tenho " 
// + idade + " anos e sou de " + cidadeDeNascimento + ".";

// template string (precisa substituir as aspas por ` `)
const apresentacao = `meu nome é ${nome}, minha idade é ${idade} anos, e nasci na cidade de ${cidadeDeNascimento}`

console.log(apresentacao)