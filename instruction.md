# **Инструкция по установке и запуску бота** #

- В корне репозитория создать директорию *.github/workflows/*
   
    *Для создания этой папки необходимо, чтобы гитхаб токен обладал специальными правами (в настройках токена в пункте scopes нужно постаивть галочку напротив workflow)*

- В папку *workflows* поместить файл скрипта с расширением *.yml*
- Скрипт будет автоматически запускаться при открытии пулл реквеста и проверять его на соответствие требованиям. В комментарии к пулл реквесту будут выводится соответствующие комментарии