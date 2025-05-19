# 🐍 **Jogo da Cobrinha - Pygame**

Bem-vindo ao **Jogo da Cobrinha**, um jogo clássico desenvolvido utilizando a biblioteca **Pygame**! 🎮

Neste jogo, o objetivo é controlar a cobra e comer a comida que aparece na tela, enquanto evita colidir com as paredes e com o próprio corpo. A cada comida consumida, a cobra cresce, tornando o jogo ainda mais desafiador. ⚡

## 📌 Funcionalidades

- **Menu Inicial**: Escolha entre jogar, saber mais sobre o jogo ou sair.
- **Jogo**: Controle a cobra e tente sobreviver o máximo possível!
- **Tela de Game Over**: Mostra a pontuação final e oferece a opção de voltar ao menu inicial pressionando **ESC**.
- **Tela "Sobre"**: Instruções sobre o jogo e como jogar.

## 🚀 Como Jogar

### Passos para jogar:

1. **Clone o repositório** ou **faça o download dos arquivos**.
   
2. **Instale o Pygame** (se não tiver instalado) usando o comando:

   ```bash
   pip install pygame

No menu principal, escolha uma das opções:

**Jogar:** Comece a jogar o jogo da cobrinha! 🐍

**Sobre:** Veja mais informações sobre o jogo.

**Sair:** Sai do jogo. 🚪

Controles:

**Seta para cima:** Move a cobra para cima.

**Seta para baixo:** Move a cobra para baixo.

**Seta para a esquerda:** Move a cobra para a esquerda.

**Seta para a direita:** Move a cobra para a direita.

**ESC:** Volta ao menu ou encerra o jogo quando estiver em "Game Over".

🎮 Como Funciona

**Menu Inicial**

Quando o jogo começa, você verá o menu principal com as seguintes opções:

**Jogar:** Comece a partida.

**Sobre:** Saiba mais sobre o jogo.

**Sair:** Encerre o jogo.

**Jogo da Cobrinha**
Durante o jogo, você controlará uma cobra que começa com um tamanho pequeno. O objetivo é comer as "comidas" vermelhas que aparecem na tela, fazendo a cobra crescer. 🐍🍎

**Colisão com paredes ou corpo:** Se a cobra colidir com as bordas da tela ou com seu próprio corpo, o jogo termina e aparece a tela de Game Over.

**Pontuação:** Sua pontuação aumenta a cada comida que a cobra come.

**Tela de Game Over**
Quando o jogo terminar, você verá:

A mensagem "Game Over!".

Sua pontuação final.

A opção de pressionar ESC para voltar ao menu principal.

🌟 Tecnologias Utilizadas
Python: A linguagem de programação escolhida para o desenvolvimento.

Pygame: Biblioteca utilizada para criar a interface gráfica, gerenciar o jogo e os eventos.

Assets: Fundo do jogo (fundoo.jpg).

📸 Captura de Tela
Confira como o jogo se parece em funcionamento! 😍


✨ Contribuindo
Este projeto é de código aberto e qualquer contribuição é bem-vinda! Se você deseja melhorar o jogo ou corrigir algum bug, siga os passos abaixo:

Fork este repositório.

Crie uma branch para a sua funcionalidade (git checkout -b minha-feature).

Commit suas mudanças (git commit -am 'Adiciona nova feature').

Push para a branch (git push origin minha-feature).

Abra um Pull Request para a branch principal.

👨‍💻 Sobre o Desenvolvedor
Este projeto foi criado por Gabrielli Vitória Glowatski, estudante da Turma STEAM 2934. 🚀

O projeto tem como objetivo praticar o uso da biblioteca Pygame e criar um jogo simples e divertido para entreter os jogadores. 🎮

📄 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

🤖 Tutorial Adicional: Como Personalizar o Jogo
Se você deseja personalizar o jogo, aqui estão algumas ideias:

Alterar o Fundo:
Se quiser mudar o fundo do jogo, basta trocar o arquivo fundoo.jpg por uma imagem sua! Assegure-se de que a nova imagem tenha o mesmo tamanho (800x600 pixels).

Alterar a Velocidade:
Para modificar a velocidade da cobra, altere o valor dentro de mainClock.tick(10) na função start_game(). O número 10 controla a taxa de atualização do jogo, e você pode aumentá-lo para acelerar a cobra ou diminuí-lo para reduzir a velocidade.

Mudar a Cor da Cobra:
Você pode mudar a cor da cobra editando o valor de SNAKE_COLOR para uma cor diferente, por exemplo:

python
Copiar
Editar
SNAKE_COLOR = (0, 255, 0)  # Cobra verde
🔗 Links Úteis
Documentação do Pygame

Tutorial Pygame - Criando seu primeiro jogo

Obrigado por conferir o Jogo da Cobrinha! Divirta-se jogando! 🎮🍏
