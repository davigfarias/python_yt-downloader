import os
import shutil
from yt_dlp import YoutubeDL
from tqdm import tqdm

class ProgressBar:
    def __init__(self):
        self.pbar = None

    def __call__(self, d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)
            if total:
                if not self.pbar:
                    self.pbar = tqdm(total=total, unit='B', unit_scale=True, desc='Baixando', dynamic_ncols=True)
                self.pbar.n = downloaded
                self.pbar.refresh()
        elif d['status'] == 'finished':
            if self.pbar:
                self.pbar.n = self.pbar.total
                self.pbar.close()
                self.pbar = None
            print("\n✅ Download concluído!")

def ffmpeg_disponivel():
    return shutil.which("ffmpeg") is not None

def baixar_video_unico(url, caminho_saida="downloads"):
    os.makedirs(caminho_saida, exist_ok=True)
    print(f"\n🎬 Baixando: {url}")

    progresso = ProgressBar()

    if ffmpeg_disponivel():
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(caminho_saida, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'progress_hooks': [progresso],
            'quiet': True
        }
    else:

        print("⚠️ FFmpeg não encontrado. Baixando melhor formato já combinado (pode faltar áudio).")
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(caminho_saida, '%(title)s.%(ext)s'),
            'progress_hooks': [progresso],
            'quiet': True
        }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def baixar_em_lote(caminho_arquivo, caminho_saida="downloads"):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            urls = [linha.strip() for linha in f if linha.strip()]

        if not urls:
            print("❌ Nenhuma URL encontrada no arquivo.")
            return

        for url in urls:
            print("\n---------------------------------")
            baixar_video_unico(url, caminho_saida)

        print("\n✅ Download em lote finalizado!")

    except FileNotFoundError:
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"❌ Erro inesperado no download em lote. Detalhes: {e}")
