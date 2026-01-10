# Unit Converter

A simple web application to convert between different units of measurement. Built with Python Flask using a clean server-side rendering approach.

**Project URL:** https://roadmap.sh/projects/unit-converter

## Features

- ✅ Convert length units (millimeter, centimeter, meter, kilometer, inch, foot, yard, mile)
- ✅ Convert weight units (milligram, gram, kilogram, ounce, pound)
- ✅ Convert temperature units (Celsius, Fahrenheit, Kelvin)
- ✅ Clean, responsive user interface
- ✅ Server-side form processing
- ✅ Input validation with immediate feedback
- ✅ Result display with original values preserved
- ✅ No database required

## Requirements

- Python 3.6 or higher
- Flask 3.1.2 or higher
- No additional dependencies

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jurabek-abd/python-backend-fundamentals.git
cd unit-converter
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate
```

3. Install Flask:
```bash
pip install Flask
```

## Project Structure

```
unit-converter/
├── static/
│   └── style.css              # Application styling
├── templates/
│   ├── length.html            # Length conversion page
│   ├── weight.html            # Weight conversion page
│   └── temperature.html       # Temperature conversion page
├── app.py                     # Main application file
├── README.md
└── requirements.txt
```

## Usage

1. Start the Flask development server:
```bash
flask run
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. Select a conversion type (Length, Weight, or Temperature) from the navigation menu

4. Enter a value, select units to convert from and to, then click "Convert"

5. View the result and click "Reset" to start a new conversion

## Conversion Logic

### Length Conversions

All length conversions use **meters** as the base unit:

| Unit | Conversion to Meters |
|------|---------------------|
| Millimeter | × 0.001 |
| Centimeter | × 0.01 |
| Meter | × 1.0 |
| Kilometer | × 1000.0 |
| Inch | × 0.0254 |
| Foot | × 0.3048 |
| Yard | × 0.9144 |
| Mile | × 1609.344 |

### Weight Conversions

All weight conversions use **grams** as the base unit:

| Unit | Conversion to Grams |
|------|---------------------|
| Milligram | × 0.001 |
| Gram | × 1.0 |
| Kilogram | × 1000.0 |
| Ounce | × 28.3495 |
| Pound | × 453.592 |

### Temperature Conversions

Temperature conversions use **Kelvin** as the intermediate unit:

- **Celsius to Kelvin**: K = C + 273.15
- **Fahrenheit to Kelvin**: K = (F - 32) × 5/9 + 273.15
- **Kelvin to Celsius**: C = K - 273.15
- **Kelvin to Fahrenheit**: F = (K - 273.15) × 9/5 + 32

## Example Workflow

### Length Conversion
1. Navigate to the Length page
2. Enter `100` in the value field
3. Select "Centimeter" as the unit to convert from
4. Select "Meter" as the unit to convert to
5. Click "Convert"
6. Result: `100 centimeter = 1.0 meter`

### Weight Conversion
1. Navigate to the Weight page
2. Enter `5` in the value field
3. Select "Pound" as the unit to convert from
4. Select "Kilogram" as the unit to convert to
5. Click "Convert"
6. Result: `5 pound = 2.26796 kilogram`

### Temperature Conversion
1. Navigate to the Temperature page
2. Enter `32` in the value field
3. Select "Fahrenheit" as the unit to convert from
4. Select "Celsius" as the unit to convert to
5. Click "Convert"
6. Result: `32 fahrenheit = 0.0 celsius`

## Input Validation

The application handles various scenarios:

- **Required fields**: HTML5 validation ensures all fields are filled
- **Numeric input**: Only accepts valid numbers (integers and decimals)
- **Same unit conversion**: Returns the original value when converting to the same unit
- **Form preservation**: Original input values are preserved after conversion for easy adjustments

## Development

### Code Organization

- **app.py**: Contains Flask routes, conversion logic, and application configuration
  - Conversion dictionaries for length and weight
  - Temperature conversion functions
  - Three route handlers for each conversion type
  
- **templates/**: HTML templates with Jinja2 templating
  - Form handling with POST method
  - Dynamic result display
  - Navigation between conversion types
  
- **static/**: CSS styling for the user interface

### Best Practices Implemented

- ✅ Base unit conversion strategy (reduces code complexity)
- ✅ Separation of conversion logic from route handlers
- ✅ Template inheritance for consistent UI
- ✅ Server-side form processing with Flask
- ✅ Clean URL structure with RESTful routes
- ✅ Input preservation for better user experience

### Running the Application

**Development mode:**
```bash
flask run
```

**Debug mode (for development):**
```bash
flask --app app --debug run
```

The application will be available at `http://127.0.0.1:5000`

## Future Enhancements

Potential improvements for learning:
- Add more unit types (area, volume, speed)
- Implement conversion history
- Add unit abbreviations in results
- Support for scientific notation
- Add keyboard shortcuts

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh Unit Converter project](https://roadmap.sh/projects/unit-converter).

---

**Project URL:** https://roadmap.sh/projects/unit-converter
