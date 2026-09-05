from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / "sigma" / "powershell_encoded_command.yml",
    ROOT / "sigma" / "scheduled_task_creation.yml",
    ROOT / "wazuh" / "local_rules.xml",
    ROOT / "suricata" / "local.rules",
    ROOT / "mappings" / "attack_coverage.md",
]

ATTACK_ID = re.compile(r"T\d{4}(?:\.\d{3})?")


def main() -> None:
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")

    mapped = set()
    for path in REQUIRED:
        text = path.read_text(encoding="utf-8")
        mapped.update(ATTACK_ID.findall(text))

    if not mapped:
        raise SystemExit("No MITRE ATT&CK identifiers found")

    print("Rule set looks structurally valid.")
    print("ATT&CK techniques found:", ", ".join(sorted(mapped)))


if __name__ == "__main__":
    main()
