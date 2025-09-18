from downloader import baixar_video_unico, baixar_em_lote
from utils import limpar_tela

def exibir_menu():
    print("=========================================")
    print("      Downloader de Vídeos do YouTube    ")
    print("          Author: Dave G. Farias         ")
    print("=========================================")
    print("Escolha uma opção:")
    print("1. Baixar um único vídeo")
    print("2. Baixar vídeos em lote de um arquivo .txt")
    print("3. Sair")
    print("-----------------------------------------")

def main():
    while True:
        limpar_tela()
        exibir_menu()
        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            limpar_tela()
            print("--- Baixar um Único Vídeo ---\n")
            url = input("Insira a URL do vídeo do YouTube: ")
            if url:
                baixar_video_unico(url)
            else:
                print("URL inválida.")
            input("\nPressione Enter para voltar ao menu...")

        elif escolha == '2':
            limpar_tela()
            print("--- Baixar Vídeos em Lote ---\n")
            caminho_arquivo = input("Insira o caminho para o arquivo .txt (ex: videos.txt): ")
            if caminho_arquivo:
                baixar_em_lote(caminho_arquivo)
            else:
                print("Caminho do arquivo inválido.")
            input("\nPressione Enter para voltar ao menu...")

        elif escolha == '3':
            print("\nObrigado por usar o programa. Até logo!")
            break

        else:
            print("\n❌ Opção inválida! Por favor, tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
