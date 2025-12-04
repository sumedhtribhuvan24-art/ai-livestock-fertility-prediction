# 🐄 AI Livestock Fertility Prediction System

A professional web application for predicting livestock fertility using video analysis. Built with Streamlit, OpenCV, and advanced AI simulation models.

## Features

### 🔐 User Authentication
- Simple login/signup system using JSON storage
- Role-based access (Farmer/Admin)
- Secure password hashing

### 📹 Video Analysis
- Upload cow videos (.mp4, AVI, .mov)
- Real-time fertility analysis using OpenCV
- Multi-feature AI analysis for accurate predictions
- Visual fertility trend charts with detailed insights

### 🧠 Advanced AI Analysis
- **Multi-Feature Analysis:** Motion, Posture, Behavior, Physical Condition, and Estrus Behavior
- **Consistent Results:** Deterministic analysis for reproducible results
- **Weighted Scoring:** 25% Behavior, 20% Estrus, 20% Physical, 20% Motion, 15% Posture
- **Enhanced Recommendations:** 10 detailed recommendation levels

### 📊 Prediction Results
- Fertility probability percentage with detailed breakdown
- Actionable recommendations based on fertility score
- Real-time alerts for high fertility (>80%)
- Comprehensive analysis statistics

### 📈 History Tracking
- Complete prediction history per user
- Analytics and metrics dashboard
- Export capabilities (CSV download)
- Clear history option

### ⚡ Live Monitoring
- Enhanced real-time monitoring based on previous analyses
- Configurable monitoring parameters (duration, interval, sensitivity)
- Real-time fertility trend visualization
- Monitoring data export
- Detailed monitoring summary with statistics

### 👑 Admin Dashboard
- System-wide analytics and metrics
- User management capabilities
- Advanced data visualization
- Performance monitoring

## Installation

### Option 1: Virtual Environment Setup (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/nevilsonani/ai-livestock-fertility-prediction.git
cd ai-livestock-fertility-prediction
```

2. Create a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

5. To deactivate the virtual environment when finished:
```bash
deactivate
```

### Option 2: Direct Installation

1. Clone the repository:
```bash
git clone https://github.com/nevilsonani/ai-livestock-fertility-prediction.git
cd ai-livestock-fertility-prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

### Getting Started
1. Open your browser to `http://localhost:8501`
2. Register a new account or login with existing credentials
3. Upload a cow video for analysis
4. View detailed results and recommendations
5. Use Live Monitoring to track fertility over time

### User Roles
- **Farmer:** Personal dashboard with video analysis, history, and monitoring
- **Admin:** Full system access with analytics and user management

### Video Requirements
- Format: MP4, AVI, or MOV
- Size: Up to 200MB
- Duration: 10-15 minutes recommended
- Quality: Clear view of the cow with good lighting

## Technical Details

### AI Model (Enhanced Simulation)
The system uses advanced simulated AI logic that analyzes multiple fertility indicators:
- **Motion Analysis:** Activity levels and movement patterns
- **Posture Analysis:** Body positioning and stance
- **Behavioral Indicators:** Time-based behavioral patterns
- **Physical Condition:** Body condition scoring
- **Estrus Behavior:** Specific estrus behavior indicators

### Fertility Scoring (Enhanced)
- **90%+:** Peak fertility - Inseminate immediately (Optimal window)
- **85-89%:** High fertility - Inseminate within 12 hours (Excellent probability)
- **80-84%:** Strong fertility - Inseminate within 24 hours (Good prospects)
- **75-79%:** Moderate to high - Monitor closely and prepare
- **70-74%:** Early signs - Continue monitoring
- **65-69%:** Minimal signs - Observe regularly
- **60-64%:** Subtle indicators - Continue routine monitoring
- **55-59%:** Very minimal - Monitor periodically
- **50-54%:** Low indicators - Routine checks sufficient
- **<50%:** Not fertile - Recheck in 24-48 hours

### Alert System
- Configurable threshold (default: 80%)
- Visual alerts in the dashboard
- Real-time status indicators
- Trend analysis

## File Structure

```
ai-livestock-fertility-prediction/
├── app.py                 # Main Streamlit application
├── auth.py               # Authentication system
├── prediction.py         # Video analysis and AI logic
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── users.json           # User accounts (auto-generated)
└── history.json         # Prediction history (auto-generated)
```

## Dependencies

- **Streamlit:** Web application framework
- **OpenCV:** Video processing and analysis
- **NumPy:** Numerical computations
- **Plotly:** Interactive charts and visualizations
- **Pandas:** Data manipulation and analysis

## Development Notes

### Enhanced Features
- **Deterministic Analysis:** Videos produce consistent results on re-analysis
- **Enhanced UI/UX:** Improved dashboard with better visualization
- **Live Monitoring:** Advanced monitoring with parameter controls
- **Multi-Feature Analysis:** Comprehensive fertility assessment
- **Detailed Recommendations:** Expanded recommendation system

### Demo Limitations
- Uses simulated AI models (not real fertility detection)
- Video analysis is simplified for demonstration
- Local JSON storage (not production database)

### Future Enhancements
- Real AI model integration
- Cloud storage and processing
- Mobile app companion
- IoT sensor integration
- Veterinary consultation features
- Multi-language support
- Advanced notification system

## Deployment

### Local Development with Virtual Environment (Recommended)
```bash
# Create and activate virtual environment
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Local Development without Virtual Environment
```bash
streamlit run app.py
```



