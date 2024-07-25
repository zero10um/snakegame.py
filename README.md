# Jogo Snake Utilizando POO e Álgebra Linear

Este projeto implementa um jogo Snake utilizando conceitos de Programação Orientada a Objetos (POO) e Álgebra Linear. O jogo é desenvolvido em Python utilizando a biblioteca Pygame para a interface gráfica.

## Índice

- [Introdução](#introdução)
- [Instalação](#instalação)
- [Como Jogar](#como-jogar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução

O jogo Snake é um jogo clássico onde o jogador controla uma cobra que se move pela tela, consumindo comida para crescer. O jogo termina quando a cobra colide com as bordas da tela ou com seu próprio corpo. Este projeto demonstra a aplicação de POO e Álgebra Linear no desenvolvimento de jogos.

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Pygame

### Passos para Instalação

1. **Clone o repositório:**

```sh
git clone https://github.com/zero10um/snakegame.py
cd seu-repositorio

Crie um ambiente virtual:
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências:
pip install pygame


Execute o jogo:

python snake_game.py


Como Jogar
Use as teclas de seta para mover a cobra:
↑ para cima
↓ para baixo
← para a esquerda
→ para a direita
Consuma a comida para crescer.
Evite colidir com as bordas da tela ou com o próprio corpo.
Estrutura do Projeto
snake_game.py: Arquivo principal que contém a lógica do jogo.
Vetor.py: Classe que representa um vetor bidimensional.
Cobra.py: Classe que representa a cobra do jogo.
Comida.py: Classe que representa a comida.
Jogo.py: Classe que gerencia a lógica geral do jogo.
README.md: Este arquivo.
Classes Principais
Classe Vetor
A classe Vetor encapsula operações de vetores como adição e comparação de igualdade, essenciais para movimentação e detecção de colisões.

Classe Cobra
A classe Cobra gerencia a lógica de movimentação, crescimento e colisão da cobra.

Classe Comida
A classe Comida gerencia a posição da comida no tabuleiro.

Classe Jogo
A classe Jogo integra todos os componentes e gerencia a lógica principal do jogo.

Estrutura do Código
.
├── Comida.py
├── Cobra.py
├── Jogo.py
├── README.md
├── snake_game.py
└── Vetor.py



Claro! Um README detalhado pode ser muito útil para quem quiser entender ou colaborar com o projeto. Vou criar um README.md que explica o projeto, como ele funciona, e como configurar o ambiente para rodá-lo.

README.md
markdown
Copiar código
# Jogo Snake Utilizando POO e Álgebra Linear

Este projeto implementa um jogo Snake utilizando conceitos de Programação Orientada a Objetos (POO) e Álgebra Linear. O jogo é desenvolvido em Python utilizando a biblioteca Pygame para a interface gráfica.

## Índice

- [Introdução](#introdução)
- [Instalação](#instalação)
- [Como Jogar](#como-jogar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução

O jogo Snake é um jogo clássico onde o jogador controla uma cobra que se move pela tela, consumindo comida para crescer. O jogo termina quando a cobra colide com as bordas da tela ou com seu próprio corpo. Este projeto demonstra a aplicação de POO e Álgebra Linear no desenvolvimento de jogos.

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Pygame

### Passos para Instalação

1. **Clone o repositório:**

```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie um ambiente virtual:
sh
Copiar código
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
Instale as dependências:
sh
Copiar código
pip install pygame
Execute o jogo:
sh
Copiar código
python snake_game.py
Como Jogar
Use as teclas de seta para mover a cobra:
↑ para cima
↓ para baixo
← para a esquerda
→ para a direita
Consuma a comida para crescer.
Evite colidir com as bordas da tela ou com o próprio corpo.
Estrutura do Projeto
snake_game.py: Arquivo principal que contém a lógica do jogo.
Vetor.py: Classe que representa um vetor bidimensional.
Cobra.py: Classe que representa a cobra do jogo.
Comida.py: Classe que representa a comida.
Jogo.py: Classe que gerencia a lógica geral do jogo.
README.md: Este arquivo.
Classes Principais
Classe Vetor
A classe Vetor encapsula operações de vetores como adição e comparação de igualdade, essenciais para movimentação e detecção de colisões.

Classe Cobra
A classe Cobra gerencia a lógica de movimentação, crescimento e colisão da cobra.

Classe Comida
A classe Comida gerencia a posição da comida no tabuleiro.

Classe Jogo
A classe Jogo integra todos os componentes e gerencia a lógica principal do jogo.

Estrutura do Código
plaintext
Copiar código
.
├── Comida.py
├── Cobra.py
├── Jogo.py
├── README.md
├── snake_game.py
└── Vetor.py

Contribuição
Contribuições são bem-vindas! Para contribuir:

Fork o projeto.
Crie uma branch para sua feature
Commit suas mudanças 
Push para a branch 
Abra um Pull Request.

