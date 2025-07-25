import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional

_configure = None

DEFAULT_LOGGER_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] %(message)s"


# logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)

class ColoredFormatter(logging.Formatter):
    """색상 포맷터"""

    # ANSI 색상 코드
    COLORS = {
        'DEBUG': '\033[36m',  # 청록색
        'INFO': '\033[32m',  # 녹색
        'WARNING': '\033[33m',  # 노란색
        'ERROR': '\033[31m',  # 빨간색
        'CRITICAL': '\033[35m',  # 마젠타색
        'RESET': '\033[0m'  # 리셋
    }

    def format(self, record):
        # 기본 포맷팅
        formatted = super().format(record)

        # 레벨에 따른 색상 적용
        level_name = record.levelname
        if level_name in self.COLORS:
            color = self.COLORS[level_name]
            reset = self.COLORS['RESET']
            formatted = f"{color}{formatted}{reset}"

        return formatted

def setup_logging(logger_level:str ="DEBUG", logger_format: str =DEFAULT_LOGGER_FORMAT):
    """전역 로깅 설정"""
    global _configure
    if _configure:
        return
    LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")
    LOGGING_LEVEL = logging.getLevelName(logger_level)
    LOGGING_FORMAT = logger_format


    # 루트 로거 설정
    root_logger = logging.getLogger()
    root_logger.setLevel(LOGGING_LEVEL)

    # 콘솔 핸들러 (색상 적용)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOGGING_LEVEL)
    console_handler.setFormatter(ColoredFormatter(LOGGING_FORMAT))
    root_logger.addHandler(console_handler)

    # 파일 핸들러
    file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=10485760, backupCount=5)
    file_handler.setLevel(LOGGING_LEVEL)
    file_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))

    # 루트 로거에 추가
    logging.getLogger("").addHandler(file_handler)
    _configure = True


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """로거 반환"""
    setup_logging()
    return logging.getLogger(name) if name else logging.getLogger()

if __name__ == "__main__":
    _logger = get_logger(__name__)
    _logger.debug("debug")
    _logger.info("info")
    _logger.warning("warning")
    _logger.error("error")
