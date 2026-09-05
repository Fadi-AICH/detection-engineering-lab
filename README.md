<div align="center">

# Detection Engineering Lab

![Sigma](https://img.shields.io/badge/Sigma-Detection_Rules-111827?style=for-the-badge)
![Wazuh](https://img.shields.io/badge/Wazuh-SIEM%2FXDR-005571?style=for-the-badge)
![Suricata](https://img.shields.io/badge/Suricata-IDS%2FIPS-EF3B2D?style=for-the-badge)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-E34F26?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-Tooling-3776AB?style=for-the-badge&logo=python&logoColor=white)

**A practical blue-team lab for writing, mapping and validating detections across endpoint and network telemetry.**

</div>

---

## Focus

This repository is a compact detection-engineering portfolio built around:

- **Sigma** for portable log detections
- **Wazuh** for host/SIEM rules
- **Suricata** for network IDS signatures
- **MITRE ATT&CK** mappings for coverage tracking
- small Python utilities for rule inventory and validation

All examples are intended for controlled lab use and defensive learning.

## Repository structure

```text
.
├── sigma/                  # portable log detection rules
├── wazuh/                  # Wazuh XML rules
├── suricata/               # network IDS signatures
├── mappings/               # MITRE ATT&CK coverage matrix
├── tools/                  # helper scripts
└── tests/                  # lightweight validation checks
```

## Detection catalogue

| Detection | Source | MITRE ATT&CK | Status |
|---|---|---|---|
| Encoded PowerShell command | Sigma / Wazuh | T1059.001 | ✅ |
| Suspicious scheduled task creation | Sigma | T1053.005 | ✅ |
| Repeated SSH authentication failures | Wazuh | T1110 | ✅ |
| TCP SYN scan pattern | Suricata | T1046 | ✅ |

## Design principles

1. **Readable first** — rules should be understandable by another analyst.
2. **ATT&CK mapped** — every detection should explain what behavior it covers.
3. **Low-noise mindset** — descriptions include likely false-positive sources.
4. **Cross-platform thinking** — compare host and network visibility where possible.
5. **Safe validation** — use controlled lab telemetry, never production attack traffic.

## Quick validation

Run the repository checks:

```bash
python tools/validate_rules.py
```

The validator checks basic file presence, ATT&CK identifiers and required metadata fields.

## Roadmap

- add more Sigma ↔ Wazuh translations
- add Windows process-tree detections
- add DNS/TLS network detections
- add sample benign/alerting event fixtures
- generate an ATT&CK coverage summary automatically

---

Built as a hands-on defensive security lab for detection engineering, SOC analysis and threat-informed defense.
