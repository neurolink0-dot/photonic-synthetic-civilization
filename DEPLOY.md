# Deployment Guide

## Quick Start (Local Server)

### Prerequisites
- Docker & Docker Compose installed, OR
- Python 3.12.10 installed
- Port 10000 available

### Option A: Docker (Recommended)

```bash
# Build and run with Docker Compose
docker-compose up

# App will be available at http://localhost:10000
```

**Dashboard:** http://localhost:10000/
**API Docs:** http://localhost:10000/docs
**API Metrics:** http://localhost:10000/dashboard/metrics

### Option B: Local Python

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn backend.main:app --host 0.0.0.0 --port 10000

# Or with auto-reload for development
uvicorn backend.main:app --host 0.0.0.0 --port 10000 --reload
```

### Option C: Manual Build

```bash
# Build Docker image
docker build -t hrq-dynasty:latest .

# Run container
docker run -p 10000:10000 hrq-dynasty:latest
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard home page |
| `/docs` | GET | Interactive API documentation (Swagger UI) |
| `/status` | GET | System status |
| `/engine/multimodal` | POST | Send multimodal requests |
| `/karma/` | GET | Get karma metrics |
| `/dashboard/metrics` | GET | Dashboard metrics JSON |
| `/dashboard/system` | GET | System info JSON |

---

## Testing

```bash
# Run unit tests locally
pytest -q

# Run with coverage
pytest --cov=backend tests/

# Run specific test file
pytest tests/test_api.py -v
```

---

## CI/CD

GitHub Actions will automatically:
- Run tests on every push/PR to `main`
- Use Python 3.12.10 (synced with local environment)
- Install dependencies from requirements.txt

Check status: https://github.com/neurolink0-dot/photonic-synthetic-civilization/actions

---

## Environment Configuration

Create a `.env` file for production settings:

```env
ENVIRONMENT=production
LOG_LEVEL=info
PYTHONUNBUFFERED=1
```

---

## Production Checklist

- [ ] All tests passing (`pytest -q`)
- [ ] `.python-version` locked to 3.12.10
- [ ] Docker image builds successfully
- [ ] CI workflow passing on GitHub
- [ ] API endpoints respond correctly
- [ ] Dashboard loads without errors
- [ ] Environment variables set (if using `.env`)

---

## Troubleshooting

**Port 10000 in use:**
```bash
# Find and kill process using port 10000
lsof -ti:10000 | xargs kill -9

# Or use different port
uvicorn backend.main:app --port 8000
```

**Module import errors:**
- Ensure you're in the project root directory
- Verify Python version: `python --version` → should be 3.12.10
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

**Dashboard not loading:**
- Check that `/static` directory exists
- Verify `static/dashboard.html` file is present
- Check browser console for errors (F12)

---

## Next Steps

- Monitor logs: `docker-compose logs -f`
- Scale horizontally: Deploy multiple containers behind a load balancer
- Add authentication: Integrate JWT or OAuth2
- Add database: Connect PostgreSQL or MongoDB for persistent data
- Monitor metrics: Use Prometheus + Grafana for real-time dashboards

---

## Support

For issues, check:
- GitHub Issues: https://github.com/neurolink0-dot/photonic-synthetic-civilization/issues
- API Docs: http://localhost:10000/docs
- Test Results: `pytest -v`
