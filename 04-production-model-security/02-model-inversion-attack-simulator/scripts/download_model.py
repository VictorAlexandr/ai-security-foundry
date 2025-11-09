import timm
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# O nome do modelo no `timm`. 'inception_resnet_v2' é uma arquitetura poderosa,
# e 'pretrained=True' usará os pesos do ImageNet, que são excelentes para 
# detectar características de baixo nível, incluindo as de rostos.
MODEL_NAME = 'inception_resnet_v2'

def main():
    """
    Usa a biblioteca 'timm' para baixar e cachear um modelo pré-treinado.
    Este método é robusto, moderno e o padrão da indústria.
    """
    logging.info(f"Iniciando o download e cache do modelo '{MODEL_NAME}' usando timm.")
    
    try:
        # A primeira vez que esta linha é executada, timm baixa os pesos do modelo
        # para um diretório de cache local (~/.cache/torch/hub).
        model = timm.create_model(MODEL_NAME, pretrained=True)
        model.eval() # Coloca o modelo em modo de inferência
        
        logging.info("Modelo carregado com sucesso.")
        logging.info(f"Pesos do modelo '{MODEL_NAME}' foram baixados e cacheados localmente.")
        
    except Exception as e:
        logging.error(f"Ocorreu um erro durante o download do modelo com timm: {e}")
        exit(1)

    logging.info("Script finalizado com sucesso.")


if __name__ == "__main__":
    main()