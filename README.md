# Nautical Assistant

Nautical Assistant is a nautical calculator that helps compute values related to wind and vessel speed. It uses FastAPI for the backend and React for the frontend, providing an intuitive interface for users without technical knowledge. It also integrates a weather API to fetch real-time weather data, including temperature, wind speed, and general conditions.

## Features

**Nautical vector calculations:**
  - True Wind (intensity and direction)
  - Apparent Wind (intensity and direction)
  - Vessel Speed (intensity and direction)
**Unit converter:**
  - Convert between knots, kilometers per hour (km/h), and miles per hour (mph).
  - Convert distances between nautical miles (NM), kilometers (km), and statute miles (mi).
**Real-time weather information:**
  - Retrieve current weather conditions, including temperature, wind speed, and general conditions.
**Dark mode:**
  - Adaptive interface with an optional dark mode for better visibility in low-light conditions.
**User-friendly interface:**
  - React-based UI that allows easy input of vectors and displays calculated results clearly.
**Professional architecture:**
  - Clear separation between frontend (React) and backend (FastAPI).

## Requirements

Ensure you have the following installed:

- Python 3.11+ (for the backend)
- Node.js 18+ (for running the React frontend)

## Installation

### 1. Clone the repository

```bash

git clone https://github.com/ma-xi-punta/ayudante-cinematico.git
cd ayudante_cinematico
```

### 2. Set up the Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

### 3. Set up the Frontend

```bash
cd ../frontend
npm install
npm start
```

## Usage

1. Enter the values for two out of the three vectors.
2. The system will automatically calculate the third vector.
3. Use the unit converter to convert speeds and distances.
4. Check real-time weather conditions.
5. Enable dark mode if preferred.
6. View results clearly in the web interface.

## API Endpoints

- **POST `/calculate`**: Receives two vectors and calculates the third.
- **GET `/weather`**: Retrieves current weather data based on a provided location.
- **POST `/convert`**: Converts speed and distance units.

## Future Improvements

- Enhance results visualization with interactive charts.
- Implement advanced input validations.
- Add internationalization (i18n) for multiple languages.

## 📸 Screenshots

[Nautical Assistant (day)](static/day.png)
[Nautical Assistant (nigth)](static/nigth.png)

---

