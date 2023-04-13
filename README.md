# Puzzle Solver API

---

**Docs:** <https://giraycoskun.github.io/puzzle-solver-api/>

## Architecture

---

![Architecture](https://drive.google.com/uc?export=view&id=1QYXgxS4O345L4OlKY-ga459XqkO8IiLi)

![API](./docs/assets/api-ss.png)

## Docker

---

**DockerHub:** <https://hub.docker.com/repository/docker/giraycoskun/puzzle-solver>

```bash
docker build -t puzzle-solver-api .
docker run -p 80:80 puzzle-solver-api
```

```bash
docker pull giraycoskun/puzzle-solver:latest
```

## Local Development

---

```bash
git clone <>
```

```bash
poetry install
```

```bash
poetry export -f requirements.txt --output requirements.txt --with dev,docs
```

```bash
poetry shell
```

```bash
mkdocs serve
```

```bash
uvicorn src.main:app --reload --reload-dir src  --port 8000
```

## Services: RabbitMQ & Redis

---

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11.13-management
```

```bash
docker run -it --rm --name redis -p 6379:6379  redis:latest
```

## Tasks

---

- [x] Create a REST API with FastAPI
- [ ] Apply Async in RabbitMQ Repository
- [ ] Initialize Subscription Service
- [ ] Initialize redis connection for solver service

## Package References

---

- <https://fastapi.tiangolo.com/>
- <https://docs.python.org/3/library/typing.html>
- <https://docs.pydantic.dev/>
- <https://pika.readthedocs.io/en/stable/index.html>
- <https://redis.readthedocs.io/en/stable/index.html>
