# 🐍 Jogo da Cobrinha - Pygame

Bem-vindo ao **Jogo da Cobrinha**, um jogo clássico e viciante desenvolvido com a biblioteca **Pygame**! 🎮  
Controle a cobrinha, coma a comida, cresça e tente bater seu recorde! ⚡

---

## 📌 Funcionalidades

✅ Menu Inicial com 3 opções: **Jogar**, **Sobre** e **Sair**  
✅ Jogo fluido com movimentação por setas do teclado  
✅ Tela de **Game Over** com sua pontuação final  
✅ Tela "Sobre" com informações e instruções úteis  
✅ Visual colorido com plano de fundo personalizado

---

## 🚀 Como Jogar

### 🎯 Passo a passo:

1. **Clone** este repositório ou **baixe os arquivos**.
2. Instale o **Pygame**, se ainda não tiver:

   ```bash
   pip install pygame
Execute o jogo no terminal:

bash
Copiar
Editar
python jogo_da_cobrinha.py
No menu principal, escolha:

▶️ Jogar – começa a partida

ℹ️ Sobre – veja informações e instruções

❌ Sair – fecha o jogo

🎮 Controles do Jogo:
🔼 Seta para cima → Move a cobra para cima
🔽 Seta para baixo → Move a cobra para baixo
◀️ Seta para a esquerda → Move a cobra para a esquerda
▶️ Seta para a direita → Move a cobra para a direita
⎋ ESC → Volta ao menu ou encerra o jogo

🧠 Como Funciona
Durante o jogo:

A cobra cresce ao comer a comida 🍎

Se bater nas bordas ou em si mesma, o jogo termina ❌

A pontuação aumenta a cada comida comida ✅

Ao perder:

Você verá a mensagem "Game Over!"

Poderá voltar ao menu pressionando ESC

🌟 Tecnologias Utilizadas
🐍 Python – Linguagem de programação

🎮 Pygame – Biblioteca para desenvolvimento de jogos

🖼️ fundoo.jpg – Imagem de fundo personalizada

📸 Captura de Tela
Adicione aqui uma imagem chamada screenshot.png para mostrar o jogo em funcionamento!

bash
Copiar
Editar
# Exemplo:
![Tela do Jogo](screenshot.png)
🛠️ Personalize seu Jogo!
Quer deixar o jogo com a sua cara? Veja como:

🔁 Mudar o fundo
Substitua o arquivo fundoo.jpg por outra imagem com tamanho 800x600.

🚀 Alterar a velocidade da cobra
Na função start_game(), mude este valor:

python
Copiar
Editar
mainClock.tick(10)  # Aumente para deixar mais rápido!
🎨 Trocar a cor da cobra
Edite esta linha para outra cor:

python
Copiar
Editar
SNAKE_COLOR = (0, 255, 0)  # Verde limão, por exemplo
👩‍💻 Sobre a Desenvolvedora
Desenvolvido com 💙 por Gabrielli Vitória Glowatski
🎓 Estudante da Turma STEAM 2934
Este projeto foi criado para praticar lógica, criatividade e o uso da biblioteca Pygame.
