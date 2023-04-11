# Puzzle Solver API

---

**Docs:** <https://giraycoskun.github.io/puzzle-solver-api/>

## Architecture

---

![Architecture](https://drive.google.com/uc?export=view&id=1K-icfWPo8eOZ32kPgDY757rIN_uBOYhu)

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

## Package References

---

- <https://fastapi.tiangolo.com/>
- <https://docs.python.org/3/library/typing.html>
- <https://docs.pydantic.dev/>
