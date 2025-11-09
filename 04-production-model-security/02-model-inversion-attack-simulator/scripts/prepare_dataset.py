import torchvision
import logging
import os

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- CONFIGURAÇÕES ---
DATA_DIR = "data"
LFW_DIR = os.path.join(DATA_DIR, "lfw_home")

def main():
    """
    Usa o downloader embutido do torchvision para baixar e preparar
    o dataset Labeled Faces in the Wild (LFW).
    """
    logging.info("Iniciando o download do dataset LFW usando torchvision.")
    logging.info("Este processo é robusto e pode demorar alguns minutos.")
    
    try:
        # O downloader do torchvision cuida de tudo: download, verificação e extração.
        # 'LFWPeople' é para tarefas de classificação, que é o que precisamos.
        dataset = torchvision.datasets.LFWPeople(
            root=DATA_DIR,      # Diretório principal para os dados
            split='train',      # Podemos usar qualquer split, só queremos os dados
            download=True       # A mágica acontece aqui
        )
        
        # O downloader cria uma estrutura de pastas um pouco diferente, vamos apenas verificar
        # se o diretório principal foi criado e contém dados.
        if os.path.exists(LFW_DIR) and len(os.listdir(LFW_DIR)) > 0:
             logging.info("Download e extração do LFW concluídos com sucesso.")
             logging.info(f"Dados disponíveis em: {LFW_DIR}")
        else:
            # O downloader do torchvision cria a pasta lfw-py, vamos checar ela
            lfw_py_dir = os.path.join(DATA_DIR, "lfw-py")
            if os.path.exists(lfw_py_dir):
                logging.info("Download e extração do LFW concluídos com sucesso.")
                logging.info(f"Dados disponíveis em: {lfw_py_dir}")
            else:
                 raise FileNotFoundError("O diretório do LFW não foi encontrado após o download.")

    except Exception as e:
        logging.error(f"Ocorreu um erro durante o download com torchvision: {e}")
        logging.error("Verifique sua conexão de internet ou se há restrições de firewall.")
        exit(1)

    logging.info("Script finalizado com sucesso.")


if __name__ == "__main__":
    main()