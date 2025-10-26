# Diabetes Prediction API - How to Run

A FastAPI-based machine learning API for diabetes prediction using logistic regression.

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Your trained model file: `logistic_regression_model.pkl`

## 🚀 Local Development Setup

### Step 1: Clone/Download the Project

```bash
# If using git
git clone <your-repo-url>
cd diabetes-prediction-api

# Or download and extract the ZIP file
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Files

Ensure your project structure looks like this:
```
diabetes-prediction-api/
├── main.py
├── requirements.txt
├── runtime.txt
├── logistic_regression_model.pkl  ← Your trained model
└── index.html (optional - frontend)
```

### Step 5: Run the API Server

```bash
uvicorn main:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 6: Test the API

#### Option A: Interactive Documentation (Swagger UI)
1. Open browser: http://localhost:8000/docs
2. Click on `/predict` endpoint
3. Click "Try it out"
4. Enter patient data
5. Click "Execute"

#### Option B: Using cURL
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Pregnancies": 1,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 30,
    "Insulin": 0,
    "BMI": 25.5,
    "DiabetesPedigreeFunction": 0.3,
    "Age": 22
  }'
```

#### Option C: Using Frontend
1. Open `index.html` in your browser
2. Keep the API URL as `http://localhost:8000/predict`
3. Fill in patient data
4. Click "Predict Diabetes Risk"

## ☁️ Cloud Deployment

### Deploy to Render (Free)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to https://render.com
   - Sign up/Login with GitHub
   - Click "New" → "Web Service"
   - Connect your repository
   - Configure:
     - **Name:** diabetes-prediction-api
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Click "Create Web Service"

3. **Get Your API URL:**
   - After deployment, you'll get: `https://your-app-name.onrender.com`
   - API endpoint: `https://your-app-name.onrender.com/predict`

4. **Update Frontend:**
   - Open `index.html`
   - Change API URL to your Render URL
   - Deploy frontend to Netlify/Vercel (optional)

### Deploy to Railway (Alternative)

1. Push code to GitHub
2. Go to https://railway.app
3. Click "New Project" → "Deploy from GitHub"
4. Select your repository
5. Railway auto-deploys!

## 📡 API Endpoints

### Health Check
```
GET /
GET /health
```

### Make Prediction
```
POST /predict
Content-Type: application/json

{
  "Pregnancies": 1,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 30,
  "Insulin": 0,
  "BMI": 25.5,
  "DiabetesPedigreeFunction": 0.3,
  "Age": 22
}
```

**Response:**
```json
{
  "prediction": 0,
  "probability": 0.234,
  "message": "The model predicts that the patient is likely not to have diabetes.",
  "input_data": { ... }
}
```

## 🔧 Troubleshooting

### Issue: "Module not found" error
**Solution:** Make sure `main.py` is at the root level, not in a subdirectory.

### Issue: "Model file not found"
**Solution:** Ensure `logistic_regression_model.pkl` is in the same directory as `main.py`.

### Issue: Port already in use
**Solution:** 
```bash
# Use a different port
uvicorn main:app --reload --port 8001
```

### Issue: CORS errors from frontend
**Solution:** The API already has CORS middleware enabled. Make sure you're using the correct API URL.

### Issue: Python version errors on Render
**Solution:** Make sure `runtime.txt` contains `python-3.11.9`

## 📊 Input Parameters

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| Pregnancies | int | 0+ | Number of pregnancies |
| Glucose | float | 0+ | Plasma glucose concentration |
| BloodPressure | float | 0+ | Diastolic blood pressure (mm Hg) |
| SkinThickness | float | 0+ | Triceps skin fold thickness (mm) |
| Insulin | float | 0+ | 2-Hour serum insulin (mu U/ml) |
| BMI | float | 0+ | Body mass index |
| DiabetesPedigreeFunction | float | 0+ | Diabetes pedigree function |
| Age | int | 0+ | Age in years |

## 🛑 Stopping the Server

Press `CTRL+C` in the terminal where the server is running.

## 📝 Notes

- Free tier on Render may spin down after 15 minutes of inactivity
- First request after inactivity may take ~30 seconds
- For production use, consider paid tier for always-on service

## 🆘 Need Help?

- API Documentation: http://localhost:8000/docs
- Check logs for error messages
- Ensure all dependencies are installed
- Verify model file is present and accessible

## 📦 Project Files

- `main.py` - FastAPI application
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version for deployment
- `logistic_regression_model.pkl` - Trained ML model
- `index.html` - Frontend interface (optional)

## 💻 Hardware & Runtime

### Local Development Requirements

**Minimum Specifications:**
- **CPU:** Any modern processor (Intel Core i3 / AMD Ryzen 3 or equivalent)
- **RAM:** 2GB available memory
- **Storage:** 500MB free space
- **OS:** Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)

**Recommended Specifications:**
- **CPU:** Intel Core i5 / AMD Ryzen 5 or better
- **RAM:** 4GB+ available memory
- **Storage:** 1GB+ free space for dependencies

### Cloud Deployment Specifications

**Render (Free Tier):**
- **CPU:** Shared CPU (0.1 CPU)
- **RAM:** 512MB
- **Storage:** Ephemeral (model must be < 500MB)
- **Bandwidth:** 100GB/month
- **Uptime:** Spins down after 15 min inactivity
- **Cold start:** ~30 seconds

**Railway (Free Tier):**
- **CPU:** Shared vCPU
- **RAM:** 512MB
- **Storage:** Ephemeral
- **Execution time:** 500 hours/month
- **Better uptime:** Stays active longer

**Heroku (Eco Dyno - $5/month):**
- **CPU:** 1x Shared
- **RAM:** 512MB
- **Storage:** Ephemeral
- **Sleeps after 30 min inactivity

### Runtime Performance

**Model Loading Time:**
- Local: ~0.5-1 second
- Cloud (cold start): ~5-10 seconds
- Cloud (warm): ~0.5-1 second

**Prediction Response Time:**
- Single prediction: ~50-200ms
- Includes model inference + JSON serialization

**Concurrent Requests:**
- Free tier: ~10-20 concurrent users
- Paid tier: 100+ concurrent users

### Python Runtime

**Supported Versions:**
- **Python 3.11.x** (Recommended)
- Python 3.10.x (Supported)
- Python 3.12.x (Supported, but less tested)
- ❌ Python 3.13+ (Pandas compatibility issues)

**Specified in `runtime.txt`:**
```
python-3.11.9
```

### Dependencies Size

**Total Installation Size:** ~450MB
- fastapi: ~10MB
- uvicorn: ~15MB
- pandas: ~150MB
- numpy: ~50MB
- scikit-learn: ~200MB
- pydantic: ~5MB
- python-multipart: ~1MB

## ✅ Reproducibility Checklist

### Environment Setup
- [ ] Python 3.11.9 installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed from `requirements.txt`
- [ ] No dependency version conflicts

### Model Files
- [ ] `logistic_regression_model.pkl` present in project root
- [ ] Model file size verified (< 500MB for free tier deployment)
- [ ] Model pickle format compatible with scikit-learn version
- [ ] Model was trained with same scikit-learn version (or compatible)

### Code Files
- [ ] `main.py` exists at project root
- [ ] `requirements.txt` with pinned versions present
- [ ] `runtime.txt` specifies Python 3.11.9
- [ ] All imports resolve successfully
- [ ] No hardcoded file paths (use relative paths)

### Local Testing
- [ ] Server starts without errors: `uvicorn main:app --reload`
- [ ] Health endpoint responds: `GET http://localhost:8000/`
- [ ] Swagger docs accessible: `http://localhost:8000/docs`
- [ ] Prediction endpoint works with sample data
- [ ] CORS headers present in responses
- [ ] Error handling works for invalid inputs

### API Validation
- [ ] All 8 input parameters accepted
- [ ] Data types validated correctly
- [ ] Negative values rejected (where applicable)
- [ ] Response includes prediction, probability, message
- [ ] Probability is between 0 and 1
- [ ] Prediction is 0 or 1

### Frontend Integration
- [ ] `index.html` opens in browser
- [ ] API URL configurable
- [ ] Form accepts all patient parameters
- [ ] Loading state displays during API call
- [ ] Success results display correctly
- [ ] Error messages display for failed requests
- [ ] Works with both local and deployed API

### Deployment Checklist

**Pre-Deployment:**
- [ ] Code pushed to GitHub repository
- [ ] `.gitignore` excludes `venv/`, `__pycache__/`, `.env`
- [ ] `logistic_regression_model.pkl` included in repo (or accessible)
- [ ] No sensitive data (API keys, passwords) in code
- [ ] All file paths are relative, not absolute

**Render Deployment:**
- [ ] Render account created and linked to GitHub
- [ ] New Web Service created
- [ ] Correct repository selected
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- [ ] Python version set to 3.11.9 (via `runtime.txt`)
- [ ] Build logs checked for errors
- [ ] Deployment successful (status: Live)

**Post-Deployment:**
- [ ] Deployed API URL accessible
- [ ] Health endpoint responds: `GET https://your-app.onrender.com/`
- [ ] API docs accessible: `https://your-app.onrender.com/docs`
- [ ] Prediction endpoint works with sample data
- [ ] Response time acceptable (< 5 seconds)
- [ ] CORS enabled for frontend requests
- [ ] Frontend updated with deployed API URL

### Testing Checklist

**Functional Tests:**
- [ ] Valid input returns prediction
- [ ] All edge cases handled (0 values, high values)
- [ ] Invalid input returns 422 error
- [ ] Missing fields return validation error
- [ ] Model loading error handled gracefully

**Sample Test Cases:**
```python
# Test Case 1: Low Risk Patient
{
  "Pregnancies": 1,
  "Glucose": 85,
  "BloodPressure": 66,
  "SkinThickness": 29,
  "Insulin": 0,
  "BMI": 26.6,
  "DiabetesPedigreeFunction": 0.351,
  "Age": 31
}
# Expected: prediction = 0 (No diabetes)

# Test Case 2: High Risk Patient
{
  "Pregnancies": 8,
  "Glucose": 183,
  "BloodPressure": 64,
  "SkinThickness": 0,
  "Insulin": 0,
  "BMI": 23.3,
  "DiabetesPedigreeFunction": 0.672,
  "Age": 32
}
# Expected: prediction = 1 (Diabetes)

# Test Case 3: Invalid Input
{
  "Pregnancies": -1,  # Negative value
  "Glucose": 120,
  # ... other fields
}
# Expected: 422 Validation Error
```

### Documentation Checklist
- [ ] README.md with setup instructions
- [ ] API endpoints documented
- [ ] Input parameters described
- [ ] Example requests/responses provided
- [ ] Troubleshooting guide included
- [ ] Hardware requirements listed

### Version Control
- [ ] Git repository initialized
- [ ] `.gitignore` configured
- [ ] Initial commit made
- [ ] Requirements pinned to specific versions
- [ ] Python version specified in `runtime.txt`

### Security Checklist
- [ ] No API keys in code
- [ ] No database credentials hardcoded
- [ ] CORS properly configured (not allowing all origins in production)
- [ ] Input validation enabled
- [ ] Error messages don't expose sensitive info
- [ ] Model file integrity verified

### Performance Monitoring
- [ ] Response times logged
- [ ] Error rates monitored
- [ ] Cold start times acceptable
- [ ] Memory usage within limits
- [ ] No memory leaks detected

### Maintenance
- [ ] Dependency update schedule planned
- [ ] Model retraining pipeline documented
- [ ] Backup strategy for model file
- [ ] Monitoring/alerting setup (optional)
- [ ] Scaling strategy documented (if needed)

---

## 🔄 Version History

**v1.0.0** - Initial Release
- FastAPI backend with logistic regression model
- 8-parameter diabetes prediction
- Interactive frontend
- Cloud deployment ready

---

**Happy Predicting! 🏥✨**