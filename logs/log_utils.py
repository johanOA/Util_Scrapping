from os import path, makedirs, remove
import logging

"""
    Args:
        log_file (str): Ruta al archivo de log.
        level (int): Nivel de logging.
        use_console (bool): Indica si los logs se muestran también en la consola.
"""
def setup_logging(log_file='logs/app.log', level=logging.INFO, use_console=True):
    # Crear directorio del archivo de log si no existe
    log_dir = path.dirname(log_file)
    if not path.exists(log_dir):
        makedirs(log_dir)
    
    # Si existe el archivo, eliminarlo
    if path.exists(log_file):
        remove(log_file)
    
    # Configuración del logging
    logging.basicConfig(
        filename=log_file,
        level=level,
        format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
    )
    
    # Configuración de logs en consola
    if use_console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logging.getLogger().addHandler(console_handler)
    
    logging.info(f"Logging inicializado. Logs en: {log_file}")