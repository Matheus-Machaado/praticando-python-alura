<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
</head>

<body>
  <h1>🐍 Praticando Python: trabalhando com projetos (Alura)</h1>

  <p>
    Este repositório reúne exercícios e pequenos projetos desenvolvidos durante o curso
    <strong>"Praticando Python: trabalhando com projetos"</strong> da Alura.
    A ideia é praticar fundamentos de Python com foco em
    <strong>organização, legibilidade, modularização e robustez</strong>.
  </p>

  <hr />

  <h2>🎯 O que foi praticado</h2>
  <ul>
    <li>Estruturar código de forma <strong>organizada e modular</strong></li>
    <li>Uso eficiente de <strong>funções, listas, dicionários</strong> e <strong>laços</strong></li>
    <li><strong>Tratamento de erros</strong> e validação de entrada do usuário</li>
    <li>Boas práticas seguindo a <strong>PEP 8</strong> (legibilidade e consistência)</li>
  </ul>

  <hr />

  <h2>📁 Estrutura do repositório</h2>
  <p>
    O projeto é uma pasta “seca”, contendo scripts independentes (<code>.py</code>),
    cada um resolvendo um exercício específico:
  </p>

  <pre>
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
  </pre>

  <hr />

  <h2>📌 Scripts incluídos</h2>

  <h3>🔹 Básicos e utilitários</h3>
  <ul>
    <li><strong>soma_numeros.py</strong> – Soma dois números informados pelo usuário (com tratamento de erros).</li>
    <li><strong>contar_vogais.py</strong> – Conta vogais em um texto.</li>
    <li><strong>palavras_longas.py</strong> – Retorna palavras com mais de 10 caracteres.</li>
    <li><strong>contrador_de_palavras.py</strong> – Conta palavras únicas (normaliza texto e remove acentuação).</li>
    <li><strong>limpar_valor.py</strong> – Exemplo de formatação monetária no padrão brasileiro.</li>
  </ul>

  <h3>🔹 Mini-projetos</h3>
  <ul>
    <li><strong>adivinhar_numero.py</strong> – Jogo: adivinhe o número de 1 a 100.</li>
    <li><strong>pedra_papel_tesoura.py</strong> – Jogo contra o computador (pedra/papel/tesoura).</li>
    <li><strong>gerador_senha.py</strong> – Gera senha aleatória (letras, números e especiais).</li>
    <li><strong>calcular_gorjeta.py</strong> – Calcula gorjeta e total com parsing de valores (R$).</li>
  </ul>

  <h3>🔹 Automação (extra)</h3>
  <ul>
    <li><strong>selenium_code.py</strong> – Exemplo de automação com Selenium usando <code>WebDriverWait</code>.</li>
  </ul>

  <hr />

  <h2>▶️ Como executar</h2>
  <p>Execute qualquer script individualmente pelo terminal:</p>

  <pre>
python nome_do_arquivo.py
  </pre>

  <p>Exemplo:</p>

  <pre>
python adivinhar_numero.py
  </pre>

  <hr />

  <h2>📦 Dependências</h2>
  <p>Alguns scripts utilizam bibliotecas externas:</p>

  <ul>
    <li><strong>colorama</strong> – para cores no terminal</li>
    <li><strong>selenium</strong> – para automação no navegador</li>
  </ul>

  <p>Instalação:</p>
  <pre>
pip install colorama selenium
  </pre>

  <p>
    <strong>Observação (Selenium):</strong> para executar <code>selenium_code.py</code>, você precisa ter o
    <strong>ChromeDriver</strong> compatível com a versão do Google Chrome instalada.
  </p>

  <hr />

  <h2>🧹 Boas práticas aplicadas</h2>
  <ul>
    <li>Separação de lógica em <strong>funções</strong> (quando faz sentido)</li>
    <li>Validação de entradas e tratamento de exceções com <code>try/except</code></li>
    <li>Execução controlada com <code>if __name__ == "__main__":</code></li>
    <li>Foco em legibilidade e consistência (PEP 8)</li>
  </ul>

  <hr />

  <h2>📚 Objetivo deste repositório</h2>
  <ul>
    <li>Praticar Python com exercícios reais e pequenos projetos</li>
    <li>Reforçar fundamentos e boas práticas</li>
    <li>Servir como material de consulta rápida</li>
  </ul>

  <hr />

  <h2>📄 Licença</h2>
  <p>
    Projeto de uso educacional. Sinta-se à vontade para estudar, modificar e evoluir o código.
  </p>
</body>
</html>
