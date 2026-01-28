# Praticando Python: trabalhando com projetos 🐍

Repositório com exercícios e pequenos projetos desenvolvidos durante o curso
**Praticando Python: trabalhando com projetos**, da Alura.

O foco deste repositório é praticar os fundamentos do Python por meio de scripts
independentes, aplicando boas práticas de codificação, organização e tratamento
de erros.

---

## 🎯 Objetivos do curso

Durante o desenvolvimento dos exercícios, foram praticados os seguintes pontos:

- Estruturação de código de forma organizada e modular
- Uso eficiente de funções, listas, dicionários e estruturas de repetição
- Identificação e tratamento de erros comuns
- Aplicação das boas práticas de codificação seguindo a PEP 8
- Escrita de código legível, reutilizável e fácil de manter

---

## 📁 Estrutura do repositório

O repositório possui uma estrutura simples, composta por scripts independentes,
cada um resolvendo um problema específico:

.
├── soma_numeros.py
├── adivinhar_numero.py
├── calcular_gorjeta.py
├── contar_vogais.py
├── contrador_de_palavras.py
├── gerador_senha.py
├── limpar_valor.py
├── palavras_longas.py
├── pedra_papel_tesoura.py
├── selenium_code.py
└── README.md

---

## 📌 Descrição dos scripts

- soma_numeros.py  
  Realiza a soma de dois números informados pelo usuário, com tratamento de erros.

- adivinhar_numero.py  
  Jogo de adivinhação onde o usuário tenta descobrir um número aleatório entre 1 e 100.

- calcular_gorjeta.py  
  Calcula o valor da gorjeta e o total da conta, tratando diferentes formatos de entrada monetária.

- contar_vogais.py  
  Conta a quantidade de vogais em um texto informado pelo usuário.

- contrador_de_palavras.py  
  Conta palavras únicas em uma frase, normalizando o texto e removendo acentuação.

- gerador_senha.py  
  Gera uma senha aleatória contendo letras maiúsculas, minúsculas, números e caracteres especiais.

- limpar_valor.py  
  Exemplo simples de formatação de valores monetários no padrão brasileiro.

- palavras_longas.py  
  Identifica palavras com mais de 10 caracteres em um texto.

- pedra_papel_tesoura.py  
  Jogo clássico de pedra, papel e tesoura contra o computador.

- selenium_code.py  
  Exemplo de automação utilizando Selenium e WebDriverWait.

---

## ▶️ Como executar

Certifique-se de ter o Python 3 instalado.

Execute qualquer script individualmente com:

python nome_do_arquivo.py

Exemplo:

python adivinhar_numero.py

---

## 📦 Dependências

Alguns scripts utilizam bibliotecas externas:

- colorama
- selenium

Instale as dependências com:

pip install colorama selenium

Para o script selenium_code.py, é necessário possuir o ChromeDriver compatível
com a versão do Google Chrome instalada na máquina.

---

## 🧹 Boas práticas aplicadas

- Uso de funções para separar responsabilidades
- Validação das entradas do usuário
- Tratamento de exceções com try/except
- Uso do bloco if __name__ == "__main__"
- Código legível seguindo os padrões da PEP 8

---

## 📚 Observações

Este repositório tem finalidade educacional e serve como prática dos conteúdos
abordados no curso da Alura.

---

## 📄 Licença

Projeto de uso educacional.
Sinta-se à vontade para estudar, modificar e evoluir o código.
