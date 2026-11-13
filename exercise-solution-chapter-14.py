from functools import partial

def log(level, module, message):
    print(f"[{level}] {module}: {message}")

log_error = partial(log, level="ERROR")
db_logger = partial(log, level="INFO", module="database")

log_error(module="auth", message="Unauthenticated user")
db_logger(message="Connection established")

# [ERROR] auth: Unauthenticated user
# [INFO] database: Connection established
