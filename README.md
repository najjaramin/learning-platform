# Learning Platform

Plateforme d'apprentissage en ligne — architecture microservices avec IA pédagogique.

## Démarrage rapide

```bash
git clone https://github.com/VOTRE-USERNAME/learning-platform.git
cd learning-platform
docker-compose up --build
```

## URLs

| Service | URL |
|---|---|
| Frontend | http://localhost |
| User Service | http://localhost:8002/health |
| Course Service | http://localhost:8001/docs |
| Analytics | http://localhost:8003/docs |
| AI Tutor | http://localhost:8004/docs |
| n8n | http://localhost:5678 |
| MinIO | http://localhost:9001 |

## Credentials

| Service | User | Password |
|---|---|---|
| MongoDB | admin | admin1234 |
| Redis | — | redis1234 |
| MinIO | minio_admin | minio1234 |
| n8n | admin | admin1234 |

## Commandes

```bash
docker-compose up --build     # Démarrer
docker-compose down           # Arrêter
docker-compose down -v        # Reset complet
docker-compose logs -f        # Logs
docker-compose ps             # État
```
