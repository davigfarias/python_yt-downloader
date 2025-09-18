# 📽️ YouTube Video Downloader em Python

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

Um script de linha de comando (CLI) simples e eficiente para baixar vídeos do YouTube, seja individualmente ou em lote a partir de um arquivo de texto. Este projeto segue boas práticas de Python.

## ⛏️ Funcionalidades

- **Download de Vídeo Único**: Baixe qualquer vídeo fornecendo a URL.
- **Download em Lote**: Informe um arquivo `.txt` com URLs, uma por linha.
- **Alta Resolução**: Busca automaticamente o melhor vídeo com áudio.
- **Interface Amigável**: Menu interativo no terminal.
- **Organização Automática**: Salva vídeos na pasta `downloads/`.
- **Tratamento de Erros**: URLs inválidas ou vídeos indisponíveis são tratados.

## 💻 Tecnologias Utilizadas

- **Python 3.8+**
- **yt-dlp**: Para baixar vídeos e áudios do YouTube.
- **tqdm**: Barra de progresso visual.

## 📝 Estrutura do Projeto

```bash
baixador-youtube/
├── main.py # Ponto de entrada do projeto
├── downloader.py # Lógica de download
├── utils.py # Funções auxiliares
├── requirements.txt # Dependências
└── README.md # Documentação
```

## ⏬ Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/baixador-youtube.git
cd baixador-youtube
```

2. **Crie e ative um ambiente virtual**

```bash
python -m venv venv
```

### Windows

```bash
.\\venv\\Scripts\\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

## ❓ Como Usar?

Execute o script principal:

```bash
python main.py
```

### Menu interativo

```bash
=========================================
    Downloader de Vídeos do YouTube
=========================================
Escolha uma opção:
1. Baixar um único vídeo
2. Baixar vídeos em lote de um arquivo .txt
3. Sair
-----------------------------------------
```

Digite o número da sua escolha:

### Exemplo 1: Baixar um Vídeo

1. Escolha 1.
2. Cole a URL do vídeo.
3. O download começa, com barra de progresso, salvando na raiz de onde o `main.py` foi rodado

### Exemplo 2: Baixar em Lote

1. Crie videos.txt com URLs, uma por linha:

```bash
https://www.youtube.com/watch?v=video1
https://www.youtube.com/watch?v=video2
https://www.youtube.com/watch?v=video3
```

2. Execute python main.py e escolha 2.
3. Informe o nome do arquivo (videos.txt) e pressione Enter.
4. Cada vídeo será baixado sequencialmente.

## ✅ Possíveis Melhorias Futuras
 [  ] Seleção de qualidade (360p, 720p, 1080p)
 [  ] Extração de áudio (MP3)
 [  ] Download de playlists
 [  ] Barra de progresso aprimorada com tqdm
 [  ] Interface gráfica (Tkinter, PyQt ou Kivy)

 [  ] Argumentos de linha de comando com argparse
