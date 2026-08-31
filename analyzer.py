"""
Mini Project 1: Data Inventory Analyzer
Phase 1 Capstone - Vervenest Python Track

Reads a CSV file (using only built-ins), computes per-column stats,
and writes a summary report. No external libraries (no pandas/csv module)
to reinforce Phase 1 fundamentals: file I/O, lists, dicts, sets, comprehensions.
"""

from pathlib import Path


def load_csv(path):
    """Read a CSV file and split into header + rows using only built-ins."""
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    rows = [line.split(",") for line in lines]
    header, data = rows[0], rows[1:]
    return header, data


def is_number(s):
    """Check if a string can be parsed as a float."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def compute_column_stats(data, col_idx, col_name):
    """Compute stats for one column. Numeric -> min/max/avg. Text -> unique count."""
    values = [row[col_idx] for row in data if col_idx < len(row)]

    if all(is_number(v) for v in values if v):
        nums = [float(v) for v in values if v]
        return {
            "column": col_name,
            "type": "numeric",
            "count": len(nums),
            "min": min(nums),
            "max": max(nums),
            "avg": round(sum(nums) / len(nums), 2) if nums else 0,
        }
    else:
        unique_vals = set(values)
        return {
            "column": col_name,
            "type": "text",
            "count": len(values),
            "unique": len(unique_vals),
            "most_common": max(unique_vals, key=values.count) if unique_vals else None,
        }


def analyze(path):
    """Run the full analysis and return a list of per-column stat dicts."""
    header, data = load_csv(path)
    return [compute_column_stats(data, i, col) for i, col in enumerate(header)]


def write_report(stats, out_path):
    """Write a human-readable summary report."""
    lines = ["Data Inventory Report", "=" * 30, ""]
    for s in stats:
        lines.append(f"Column: {s['column']} ({s['type']})")
        if s["type"] == "numeric":
            lines.append(f"  count={s['count']}  min={s['min']}  max={s['max']}  avg={s['avg']}")
        else:
            lines.append(f"  count={s['count']}  unique={s['unique']}  most_common={s['most_common']}")
        lines.append("")

    Path(out_path).write_text("\n".join(lines))


if __name__ == "__main__":
    input_path = "sample_data.csv"
    output_path = "report.txt"

    if Path(input_path).exists():
        stats = analyze(input_path)
        write_report(stats, output_path)
        print(f"Report written to {output_path}")
        for s in stats:
            print(s)
    else:
        print(f"No file found at {input_path} — drop a CSV there and rerun.")