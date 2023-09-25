import os
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

# Defina o caminho da pasta onde estão os arquivos de áudio e vídeo
folder_path = r"C:\Users\Rafael Santos\Documents\RIHAPPY"

# Lista dos formatos de arquivo suportados (áudio e vídeo)
supported_formats = (".wav", ".flac", ".m4a", ".ogg", ".wma", ".mp4", ".avi", ".mkv", ".mpeg")

# Função para converter um arquivo para MP3 e substituir o original
def convert_to_mp3_replace_original(file_path):
    # Verifica a extensão do arquivo para determinar o tipo
    file_extension = os.path.splitext(file_path)[1].lower()

    try:
        # Se for um arquivo de áudio suportado
        if file_extension in (".wav", ".flac", ".m4a", ".ogg", ".wma"):
            audio = AudioSegment.from_file(file_path)
            mp3_path = os.path.splitext(file_path)[0] + ".mp3"
            audio.export(mp3_path, format="mp3")
            os.remove(file_path)  # Remove o arquivo original
        # Se for um arquivo de vídeo suportado
        elif file_extension in (".mp4", ".avi", ".mkv", ".mpeg"):
            try:
                video = VideoFileClip(file_path)
                audio = video.audio
                mp3_path = os.path.splitext(file_path)[0] + ".mp3"
                audio.write_audiofile(mp3_path, codec="mp3")
                os.remove(file_path)  # Remove o arquivo original
            except Exception as e:
                print(f"Erro ao converter o arquivo: {file_path}")
                print(f"Detalhes do erro: {str(e)}")
        else:
            print(f"Arquivo não suportado: {file_path}")
    except Exception as e:
        print(f"Erro ao converter o arquivo: {file_path}")
        print(f"Detalhes do erro: {str(e)}")

# Percorre todos os arquivos na pasta
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_extension = os.path.splitext(file_path)[1].lower()

        # Verifica se o arquivo está em um formato suportado
        if file_extension in supported_formats:
            mp3_path = os.path.splitext(file_path)[0] + ".mp3"
            # Verifica se já existe um arquivo MP3 com o mesmo nome
            if not os.path.exists(mp3_path):
                print(f"Convertendo: {file}")
                convert_to_mp3_replace_original(file_path)
                print(f"Concluído: {mp3_path}")
            else:
                print(f"Arquivo MP3 já existe: {mp3_path}")
