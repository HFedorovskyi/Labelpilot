from loguru import logger
import os
import sys
from datetime import datetime

if getattr(sys, 'frozen', False):
    # Если приложение запущено в режиме "frozen" (скомпилировано)
    main_directory_path = os.path.dirname(sys.executable)
    application_path = os.path.join(main_directory_path, 'app_loging', )

else:
    # Если приложение запущено в режиме разработки
    application_path = os.path.dirname(__file__)

log_dir = os.path.join(application_path, 'logs')

session_date = datetime.now().strftime("%Y-%m-%d")


logger.add(os.path.join(log_dir, f'log_INFO_{session_date}.log'),
           level='INFO',
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name} | {file}:{line} |"
                  " function name:{function} | {module} | {message}",
           rotation='10 Mb',
           retention='60 days',
           compression="zip")

logger.add(os.path.join(log_dir, f'log_DEBUG_{session_date}.log'),
           level='DEBUG',
           rotation='10 Mb',
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name} | {file}:{line} |"
                  " function name:{function} | {module} | {message}",
           retention='60 days',
           compression="zip")

logger.add(os.path.join(log_dir, f'log_WARNING_{session_date}.log'),
           level='WARNING',
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name} | {file}:{line} |"
                  " function name:{function} | {module} | {message}",
           rotation='10 Mb',
           retention='60 days',
           compression="zip")

logger.add(os.path.join(log_dir, f'log_ERROR_{session_date}.log'),
           level='ERROR',
           format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name} | {file}:{line} |"
                  " function name:{function} | {module} | {message}",
           rotation='10 Mb',
           retention='60 days',
           compression="zip")
