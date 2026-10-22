# AIGC5005 Lab 04 - RecordsApp

## Project Setup

Clone the repository:

```bash
git clone <repository-url>
cd AIGC5005_Lab04
```

Create the environment:

```bash
conda env create -f environment.yml
conda activate recordsapp
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Configuration settings are stored in:

```text
config/recordsapp.toml
```

Example settings:

```toml
source_url = "https://api.tvmaze.com/shows?page=0"
timeout = 30
output_folder = "data/processed"
seed = 42
sample_size = 5
log_level = "INFO"
```

---

## Running the Program

Run the application:

```bash
python main.py
```

or

```bash
python -m recordsapp.main
```

---

## Running Tests

Run all tests:

```bash
pytest
```

The project contains more than 12 unit tests.

---

## Using Ruff

Check code quality:

```bash
ruff check .
```

---

## Using Mypy

Run type checking:

```bash
mypy src
```

---

## Error Handling

The project uses custom exceptions:

- PackageError
- SourceError
- DataError
- SettingsError

These exceptions provide clearer error reporting and handling.

---

## Generated Output

Processed data is stored in:

```text
data/processed/
```

Generated files include:

```text
summary.json
run_info.json
```

---

## Known Limitations

- Requires internet access to download TVMaze data.
- Results depend on external API availability.
- Only a subset of show information is processed.

---

## Validation

The project has been validated with:

```bash
pytest
mypy src
ruff check .
```

All checks pass successfully.