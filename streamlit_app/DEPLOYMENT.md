# Deployment Guide - Sandoz Pipeline Streamlit App

## Local Deployment

### Prerequisites
- Python 3.8+
- pip
- Virtual Environment (recommended)

### Installation

1. **Clone/Download the project**
   ```bash
   cd Sandoz_pipeline_streamlit
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Cloud Deployment

### Streamlit Cloud (Recommended)

1. **Prepare GitHub Repository**
   - Push your code to GitHub
   - Ensure `.gitignore` is properly configured

2. **Deploy on Streamlit Cloud**
   - Go to https://streamlit.io/cloud
   - Sign in with GitHub account
   - Click "New app"
   - Select repository and branch
   - Set main file path: `app.py`
   - Click "Deploy"

### Heroku Deployment

1. **Create `Procfile`**
   ```
   web: streamlit run --server.port=$PORT --server.address=0.0.0.0 app.py
   ```

2. **Create `setup.sh`**
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
   headless = true
   port = $PORT
   enableCORS = false
   " > ~/.streamlit/config.toml
   ```

3. **Deploy**
   ```bash
   heroku create app-name
   git push heroku main
   ```

### Docker Deployment

1. **Create `Dockerfile`**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Create `.dockerignore`**
   ```
   .git
   .gitignore
   venv/
   __pycache__/
   .pytest_cache/
   .streamlit/
   ```

3. **Build and run**
   ```bash
   docker build -t sandoz-pipeline .
   docker run -p 8501:8501 sandoz-pipeline
   ```

### AWS EC2 Deployment

1. **Launch EC2 instance**
   - Choose Ubuntu 20.04 LTS
   - Configure security group (allow port 8501)

2. **Connect and setup**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   
   # Update system
   sudo apt-get update
   sudo apt-get upgrade -y
   
   # Install Python and pip
   sudo apt-get install python3-pip -y
   
   # Clone repository
   git clone your-repo-url
   cd Sandoz_pipeline_streamlit
   
   # Create venv and install
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   
   # Run app
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```

3. **Use systemd for persistence**
   ```bash
   sudo nano /etc/systemd/system/streamlit.service
   ```
   
   Add:
   ```
   [Unit]
   Description=Streamlit App
   After=network.target
   
   [Service]
   Type=simple
   User=ubuntu
   WorkingDirectory=/home/ubuntu/Sandoz_pipeline_streamlit
   ExecStart=/home/ubuntu/Sandoz_pipeline_streamlit/venv/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   Restart=always
   
   [Install]
   WantedBy=multi-user.target
   ```
   
   Enable:
   ```bash
   sudo systemctl start streamlit
   sudo systemctl enable streamlit
   ```

## Environment Variables

Create `.env` file (add to `.gitignore`):
```
# Database configuration (if needed)
DB_HOST=localhost
DB_USER=admin
DB_PASS=password

# API Keys (if needed)
API_KEY=your_api_key

# App settings
DEBUG=False
LOG_LEVEL=INFO
```

## Monitoring & Maintenance

### Logging

Add to `app.py`:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

### Health Check

Create `health_check.py`:
```python
import requests

def check_health(url="http://localhost:8501"):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False

if __name__ == "__main__":
    if check_health():
        print("✓ App is running")
    else:
        print("✗ App is not responding")
```

## Performance Optimization

1. **Enable caching**
   ```python
   @st.cache_data
   def load_data():
       return PIPELINE_PRODUCTS
   ```

2. **Use session state wisely**
   ```python
   if "data" not in st.session_state:
       st.session_state.data = load_expensive_data()
   ```

3. **Optimize rendering**
   - Use columns for layout
   - Defer heavy computations
   - Use expanders for hidden content

## Security Considerations

1. **Sensitive data**
   - Use environment variables for secrets
   - Never commit API keys
   - Use `.env` files with `.gitignore`

2. **Authentication** (optional)
   ```python
   import streamlit_authenticator as stauth
   ```

3. **HTTPS**
   - Use reverse proxy (nginx)
   - Implement SSL/TLS

4. **Rate limiting**
   - Add request throttling if exposed publicly
   - Implement user quotas

## Troubleshooting Deployment

### App won't start
- Check Python version compatibility
- Verify all dependencies installed
- Check ports are available

### Memory issues
- Increase instance size
- Optimize data loading
- Use streaming for large datasets

### Slow performance
- Enable caching
- Optimize queries
- Reduce data volume

## Scaling Strategies

1. **Load Balancing**
   - Use multiple instances
   - Implement session state sharing

2. **Database**
   - Move data to external database
   - Implement caching layer

3. **CDN**
   - Serve static assets from CDN
   - Reduce bandwidth usage

## Backup & Recovery

1. **Regular backups**
   ```bash
   git push origin main  # Backup code
   # Schedule database backups
   ```

2. **Recovery procedures**
   - Document recovery steps
   - Test recovery regularly
   - Keep backup copies

---

**Last Updated**: 2026-02-04
