# Puzzle Solver API

---

**Docs:** <https://giraycoskun.github.io/puzzle-solver-api/>

## Architecture

---

![Architecture](https://drive.google.com/uc?export=view&id=1QvKGTU_ZbMEFSL-eMyVMGwQP9Y14DxB2)

## Docker

---

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

