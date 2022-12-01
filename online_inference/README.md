### Билд и запуск докера локально
**Внимание** - если у вас не макбук на м1, то тег платформы не указывать
```
sudo docker buildx build --platform=linux/arm64 -t mlopshw2 .
docker run -d -p 8080:8080  mlopshw2
```

### Скачать и поднять образ
Ссылка на образ - https://hub.docker.com/repository/docker/klarefor/mlops
```
docker pull klarefor/mlops:latest
docker run -d -p 8080:8080 mlopshw2 
```
   
### Запустить тестовый запрос
```commandline
cd online_inference
python request_example.py
```


### Что сделано
1. inference модели обернут в restapi. Endpoint /predict лежит в routers/ml_model +3
2. /health endpoint лежит там же +1 
3. Юнит тест лежит в /tests/predict_test +3
4. Скрипт для запроса - request_example.py. Переходим в online_inference и python request_example (Важно - должны быть установлены зависимости из requirements.txt) +2
5. Докерфайл лежит в корне проекта +4.
6. Образ опубликован +2
7. Коректные команды для скачки и поднятия докера + запуск скрипта для теста лежат в ридми выше +1
8. Самооценка проведена +1

**Суммарно 17 баллов**