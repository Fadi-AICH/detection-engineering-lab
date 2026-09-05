# MITRE ATT&CK Coverage

| Rule | ATT&CK technique | Tactic | Telemetry |
|---|---|---|---|
| Encoded PowerShell | T1059.001 — PowerShell | Execution | Windows process creation |
| Scheduled Task Creation | T1053.005 — Scheduled Task/Job | Persistence / Privilege Escalation | Windows process creation |
| Repeated SSH Authentication Failures | T1110 — Brute Force | Credential Access | Authentication logs |
| TCP SYN Scan Pattern | T1046 — Network Service Discovery | Discovery | Network traffic / Suricata |

## Coverage approach

The goal is not to maximize ATT&CK technique count. Each mapping should be backed by a concrete telemetry source and a detection that can be explained, tested and tuned.

Future coverage will focus on process discovery, credential access, defense evasion, lateral movement and suspicious DNS/TLS behavior.
