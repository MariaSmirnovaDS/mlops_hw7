# MLops HW7: CI/CD для ML-модели

## Ссылки
- GitHub репозиторий: https://github.com/MariaSmirnovaDS/mlops_hw7
- GitLab/GitVerse пайплайн: https://gitverse.ru/MariaDS/HW7_CICD/cicd/1
- GitHub Actions пайплайн: https://github.com/MariaSmirnovaDS/mlops_hw7/actions/runs/25635298103

## Стратегия деплоя
Выбрана **Blue-Green deployment**:
- Blue: v1.0.0
- Green: v1.1.0
- Балансировщик: Nginx
- Возможность мгновенного отката

### Запуск

Запустить Blue и Green
```bash
docker run -d --name blue -p 5001:5000 ml-service:v1.0.0
docker run -d --name green -p 5002:5000 ml-service:v1.1.0
```

Запустить Nginx
```bash
docker run -d --name nginx -p 9090:80 nginx:alpine
```

Переключить трафик на Green
```bash
./switch.sh green
```

Откат на Blue
```bash
./switch.sh blue
```

### Проверка
```bash
curl http://localhost:5001/health  # Blue: v1.0.0
curl http://localhost:5002/health  # Green: v1.1.0
curl http://localhost:9090/health  # Через балансировщик
```

### ADR
Архитектурное решение: doc/architecture/decisions/



