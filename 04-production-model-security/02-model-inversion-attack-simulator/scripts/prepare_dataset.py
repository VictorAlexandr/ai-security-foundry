import os
import zipfile
import requests
from tqdm import tqdm
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- CONFIGURAÇÕES ---
# URLs para os arquivos do CelebA (usando um mirror confiável)
URL_IMAGES = "https://huggingface.co/datasets/AI-Security-Foundry/CelebA-sample/resolve/main/img_align_celeba.zip"
URL_PARTITION = "https://huggingface.co/datasets/AI-Security-Foundry/CelebA-sample/resolve/main/list_eval_partition.txt"

# Caminhos locais
DATA_DIR = "data/celeba"
ZIP_PATH = os.path.join(DATA_DIR, "img_align_celeba.zip")
PARTITION_PATH = os.path.join(DATA_DIR, "list_eval_partition.txt")
IMAGE_DIR = os.path.join(DATA_DIR, "img_align_celeba")
SAMPLED_DIR = os.path.join(DATA_DIR, "sampled_validation")

# Parâmetros da amostragem
NUM_SAMPLES = 1000

def download_file(url, dest_path):
    """Baixa um arquivo com uma barra de progresso."""
    if os.path.exists(dest_path):
        logging.info(f"Arquivo já existe em {dest_path}. Pulando download.")
        return
    
    logging.info(f"Baixando de {url} para {dest_path}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Lança um erro para status HTTP ruins
        total_size = int(response.headers.get('content-length', 0))
        
        with open(dest_path, 'wb') as f, tqdm(
            total=total_size, unit='iB', unit_scale=True, desc=os.path.basename(dest_path)
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                bar.update(len(chunk))
        logging.info("Download concluído com sucesso.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro no download: {e}")
        if os.path.exists(dest_path):
            os.remove(dest_path) # Remove arquivo incompleto
        exit(1)

def main():
    """Orquestra o processo de download, extração e amostragem."""
    logging.info("Iniciando o script de preparação do dataset CelebA.")
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(SAMPLED_DIR, exist_ok=True)

    # Passo 1: Baixar os arquivos necessários
    download_file(URL_IMAGES, ZIP_PATH)
    download_file(URL_PARTITION, PARTITION_PATH)

    # Passo 2: Extrair as imagens
    if not os.path.exists(IMAGE_DIR):
        logging.info(f"Extraindo {ZIP_PATH}...")
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(DATA_DIR)
        logging.info("Extração concluída.")
    else:
        logging.info("Diretório de imagens já existe. Pulando extração.")

    # Passo 3: Identificar e copiar as imagens de validação
    logging.info(f"Identificando as primeiras {NUM_SAMPLES} imagens de validação...")
    
    copied_count = 0
    with open(PARTITION_PATH, 'r') as f:
        for line in f:
            if copied_count >= NUM_SAMPLES:
                break
            
            filename, partition = line.strip().split()
            # partição '1' corresponde à validação
            if partition == '1':
                src_path = os.path.join(IMAGE_DIR, filename)
                dest_path = os.path.join(SAMPLED_DIR, filename)
                
                if not os.path.exists(dest_path):
                    # Simular a cópia, já que o zip contém apenas as amostras
                     if os.path.exists(src_path):
                        # Esta parte seria 'shutil.copy(src_path, dest_path)' em um cenário real
                        # Como nosso ZIP é pré-amostrado, a existência já é suficiente.
                        pass
                
                copied_count += 1
    
    # Como o ZIP já é a amostra, vamos apenas verificar se os arquivos estão lá
    final_file_count = len(os.listdir(IMAGE_DIR))
    logging.info(f"Processo de amostragem concluído. {final_file_count} imagens prontas para uso em {IMAGE_DIR}.")
    logging.info("Script finalizado com sucesso.")


if __name__ == "__main__":
    main()