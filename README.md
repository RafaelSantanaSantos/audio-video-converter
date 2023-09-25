# Conversor de Áudio e Vídeo para MP3

Este é um script Python simples que permite converter arquivos de áudio e vídeo para o formato MP3. Ele percorre uma pasta especificada em busca de arquivos com extensões suportadas e realiza a conversão, substituindo os arquivos originais. A lista de formatos de arquivo suportados inclui: .wav, .flac, .m4a, .ogg, .wma, .mp4, .avi, .mkv e .mpeg.

## Como Usar

1. Certifique-se de ter o Python instalado no seu sistema.
2. Instale as bibliotecas necessárias executando `pip install pydub moviepy`.
3. Clone este repositório para o seu computador ou baixe o arquivo `videotomp3.py`.
4. Execute o script Python `videotomp3.py` na pasta onde estão os arquivos de áudio e vídeo que você deseja converter.
5. O script detectará automaticamente os arquivos suportados, converterá para MP3 e substituirá os originais, se necessário.

```bash
python videotomp3.py
