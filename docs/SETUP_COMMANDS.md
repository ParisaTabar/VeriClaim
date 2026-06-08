# VeriClaim Academic Patch Setup Commands

Run from the repository root after copying these files into the project.

## 1. Create folders if missing

```bash
mkdir -p infrastructure/sql infrastructure/docker workflows pages
```

## 2. Copy environment file

```bash
cp .env.example .env
```

Edit `.env` and set:

```bash
OPENALEX_MAILTO=your.email@example.com
N8N_ENCRYPTION_KEY=a_real_random_32_character_string
```

Do not commit `.env`.

## 3. Reset demo database

```bash
docker compose down -v
docker compose up --build
```

## 4. Check database schema

```bash
docker exec -it vericlaim_db psql -U vericlaim_user -d vericlaim_db -c "\dn"
docker exec -it vericlaim_db psql -U vericlaim_user -d vericlaim_db -c "\dt sovereign_pipeline.*"
docker exec -it vericlaim_db psql -U vericlaim_user -d vericlaim_db -c "\d+ sovereign_pipeline.latest_verifications"
```

## 5. Configure n8n credentials

Postgres credentials inside n8n must use Docker service host `db`, not `localhost`.

```text
Host: db
Port: 5432
Database: vericlaim_db
User: vericlaim_user
Password: vericlaim_pass
```

Import the workflow and activate it.

## 6. Test production webhook from host

```bash
curl -X POST http://localhost:5678/webhook/verify-claim \
  -H "Content-Type: application/json" \
  -d '{"claim":"Microplastics are detectable in human blood"}'
```

## 7. Open Streamlit

```text
http://localhost:8501
```
