```markdown
# Data Inventory Analyzer

A lightweight CSV analysis tool built with pure Python — no pandas, no `csv` module, just built-ins. Written as the Phase 1 capstone for the Vervenest Python track.

## What it does

Reads a CSV file and computes per-column statistics:
- **Numeric columns** → min, max, average
- **Text columns** → unique value count, most common value

Results are printed to the console and written to a `report.txt` summary file.

## Why pure Python

This project intentionally avoids external libraries to reinforce core fundamentals: file I/O with `open()`/`with`, list and dict comprehensions, set operations, and `pathlib` for path handling.

## Usage

```bash
python analyzer.py
```

By default it looks for `sample_data.csv` in the same directory and writes results to `report.txt`. Swap `input_path` in the script to point at your own CSV.

## Example

Input (`sample_data.csv`):
```
name,age,city,score
alice,23,mumbai,88
bob,31,delhi,72
```

Output:
```
Column: name (text)
  count=5  unique=5  most_common=alice

Column: age (numeric)
  count=5  min=23.0  max=31.0  avg=27.0
```

## Tech

- Python 3.10+
- Standard library only (`pathlib`)
```

Drop that in as `README.md`, then `git add README.md && git commit -m "update README" && git push`.
