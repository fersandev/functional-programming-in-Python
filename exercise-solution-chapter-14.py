from functools import partial

def log(level, module, message):
    print(f"[{level}] {module}: {message}")

log_error = partial(log, level="ERROR")
db_logger = partial(log, level="INFO", module="database")

log_error(module="auth", message="Usuario no autenticado")
db_logger(message="Conexión establecida")

# [ERROR] auth: Usuario no autenticado
# [INFO] database: Conexión establecida
