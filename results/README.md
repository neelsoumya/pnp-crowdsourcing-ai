# Results
- `exploration_log.md`: seed log from the first two sessions (explorations 1-2) in the skill's format, with the Strategy Register at the top.
- `STRATEGY_REGISTER.md`: canonical register, edited by maintainers after merging explorations.
- `explorations/`: one file per crowdsourced exploration.
- `probes/`: scripts producing computed artifacts.
  - `formula_size_probe.py N`: exact minimum de Morgan formula size (leaf count) for all Boolean functions on N variables. Verified: N=3 max 10, N=4 max 16 (parity).
