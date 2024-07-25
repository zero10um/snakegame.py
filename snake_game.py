import random
import pygame
import sys

class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)
    
    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y
    
    def para_tupla(self):
        return (self.x, self.y)

def posicao_aleatoria(largura, altura):
    return Vetor(random.randint(0, largura - 1), random.randint(0, altura - 1))

class Cobra:
    def __init__(self, posicao_inicial):
        self.corpo = [posicao_inicial]
        self.direcao = Vetor(1, 0)
    
    def mover(self):
        nova_cabeca = self.corpo[0] + self.direcao
        self.corpo.insert(0, nova_cabeca)
        self.corpo.pop()
    
    def crescer(self):
        nova_cabeca = self.corpo[0] + self.direcao
        self.corpo.insert(0, nova_cabeca)
    
    def mudar_direcao(self, nova_direcao):
        if nova_direcao + self.direcao != Vetor(0, 0):
            self.direcao = nova_direcao
    
    def verificar_colisao(self, largura, altura):
        cabeca = self.corpo[0]
        if cabeca.x < 0 or cabeca.x >= largura or cabeca.y < 0 or cabeca.y >= altura:
            return True
        if cabeca in self.corpo[1:]:
            return True
        return False

class Comida:
    def __init__(self, posicao):
        self.posicao = posicao
    
    def reposicionar(self, largura, altura):
        self.posicao = posicao_aleatoria(largura, altura)

class Jogo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.cobra = Cobra(Vetor(largura // 2, altura // 2))
        self.comida = Comida(posicao_aleatoria(largura, altura))
        self.pontuacao = 0
    
    def atualizar(self):
        self.cobra.mover()
        self.imprimir_vetores()
        if self.cobra.corpo[0] == self.comida.posicao:
            self.cobra.crescer()
            self.comida.reposicionar(self.largura, self.altura)
            self.pontuacao += 1
        
        if self.cobra.verificar_colisao(self.largura, self.altura):
            print("Fim de Jogo")
            print("Pontuação:", self.pontuacao)
            return False
        return True
    
    def mudar_direcao_cobra(self, nova_direcao):
        self.cobra.mudar_direcao(nova_direcao)
    
    def imprimir_vetores(self):
        print(f"Posição da comida: {self.comida.posicao.para_tupla()}")
        print("Posições da cobra:")
        for segmento in self.cobra.corpo:
            print(segmento.para_tupla())

def desenhar_jogo(tela, jogo, tamanho_celula):
    tela.fill((0, 0, 0))
    for segmento in jogo.cobra.corpo:
        pygame.draw.rect(tela, (0, 255, 0), (segmento.x * tamanho_celula, segmento.y * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.draw.rect(tela, (255, 0, 0), (jogo.comida.posicao.x * tamanho_celula, jogo.comida.posicao.y * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.display.flip()

def tela_fim_de_jogo(tela, pontuacao, tamanho_celula):
    fonte = pygame.font.Font(None, 50)
    texto = fonte.render(f"Fim de Jogo", True, (255, 0, 0))
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    texto_reiniciar = fonte.render("Pressione R para Reiniciar", True, (255, 255, 255))
    tela.fill((0, 0, 0))
    tela.blit(texto, ((tela.get_width() - texto.get_width()) // 2, tela.get_height() // 2 - 60))
    tela.blit(texto_pontuacao, ((tela.get_width() - texto_pontuacao.get_width()) // 2, tela.get_height() // 2))
    tela.blit(texto_reiniciar, ((tela.get_width() - texto_reiniciar.get_width()) // 2, tela.get_height() // 2 + 60))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    esperando = False
                    return True
                elif evento.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
    return False

def main():
    pygame.init()
    largura, altura = 20, 20
    tamanho_celula = 20
    tela = pygame.display.set_mode((largura * tamanho_celula, altura * tamanho_celula))
    relogio = pygame.time.Clock()

    while True:
        jogo = Jogo(largura, altura)
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        jogo.mudar_direcao_cobra(Vetor(0, -1))
                    elif evento.key == pygame.K_DOWN:
                        jogo.mudar_direcao_cobra(Vetor(0, 1))
                    elif evento.key == pygame.K_LEFT:
                        jogo.mudar_direcao_cobra(Vetor(-1, 0))
                    elif evento.key == pygame.K_RIGHT:
                        jogo.mudar_direcao_cobra(Vetor(1, 0))
            
            if not jogo.atualizar():
                rodando = False
            
            desenhar_jogo(tela, jogo, tamanho_celula)
            relogio.tick(10)
        
        if not tela_fim_de_jogo(tela, jogo.pontuacao, tamanho_celula):
            break

if __name__ == "__main__":
    main()
