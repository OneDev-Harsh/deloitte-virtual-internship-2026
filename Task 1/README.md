# Telemetry Data Normalization

## Overview
This project standardizes telemetry data from multiple input formats into a single unified schema. It ensures consistency in data representation, making it suitable for downstream analytics, monitoring systems, and data pipelines.

The system supports two different JSON formats and converts them into a common structure while preserving all critical information.

---

## Problem Statement
Telemetry data from devices can arrive in different formats depending on the source system. This inconsistency creates challenges for:

- Data processing pipelines  
- Monitoring and alerting systems  
- Analytics and reporting  

The goal of this project is to normalize these heterogeneous data formats into a single, consistent structure.

---

## Supported Input Formats

### Format 1
- Flat structure  
- Location stored as a single string  
- Timestamp already in milliseconds  

### Format 2
- Nested structure  
- Location fields separated  
- Timestamp in ISO 8601 format  

---

## Unified Output Format

The output schema standardizes both formats into:

- `deviceID`
- `deviceType`
- `timestamp` (milliseconds since epoch)
- `location` (structured object)
  - country
  - city
  - area
  - factory
  - section
- `data`
  - status
  - temperature

---

## Key Features

- Handles multiple input formats seamlessly  
- Converts ISO 8601 timestamps to epoch milliseconds  
- Parses and structures location data  
- Includes input validation for robustness  
- Clean and modular code design  
- Automated unit testing using `unittest`  

---

## How It Works

1. The program reads input JSON files  
2. Detects the format based on structure  
3. Applies the appropriate conversion logic:
   - `convertFromFormat1()`
   - `convertFromFormat2()`  
4. Outputs data in the unified schema  
5. Validates correctness using unit tests  

---

## Installation & Setup

### Prerequisites
- Python 3.x

### Steps

1. Clone or download the project  
2. Navigate to the project directory  
3. Run the program:

```bash
python main.py