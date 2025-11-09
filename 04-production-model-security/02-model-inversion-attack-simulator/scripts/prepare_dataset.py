import logging
from sklearn.datasets import fetch_lfw_people

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- CONFIGURAÇÕES ---
# Pessoas com no mínimo 50 imagens, para garantir classes com dados suficientes
MIN_FACES_PER_PERSON = 50
DATA_DIR = "data" # scikit-learn gerenciará a subpasta 'lfw_home' aqui dentro

def main():
    """
    Usa o downloader embutido do scikit-learn para baixar e preparar
    o dataset Labeled Faces in the Wild (LFW).
    Este método é o padrão da indústria, robusto e gerencia seu próprio cache.
    """
    logging.info("Iniciando o download do dataset LFW usando scikit-learn.")
    logging.info(f"Serão baixadas as imagens de pessoas com no mínimo {MIN_FACES_PER_PERSON} fotos.")
    
    try:
        # A mágica acontece aqui. O scikit-learn lida com o download,
        # extração e cache de forma transparente.
        fetch_lfw_people(
            min_faces_per_person=MIN_FACES_PER_PERSON, 
            data_home=DATA_DIR, # Especifica onde salvar
            resize=0.4          # Reduz o tamanho para ser mais rápido
        )
        
        lfw_home_dir = os.path.join(DATA_DIR, "lfw_home")
        if os.path.exists(lfw_home_dir):
             logging.info("Download e preparação do LFW concluídos com sucesso.")
             logging.info(f"Dados cacheados e prontos para uso em: {lfw_home_dir}")
        else:
            raise FileNotFoundError("O diretório do LFW não foi encontrado após o download.")

    except Exception as e:
        logging.error(f"Ocorreu um erro durante o download com scikit-learn: {e}")
        exit(1)

    logging.info("Script finalizado com sucesso.")


if __name__ == "__main__":
    import os
    main()