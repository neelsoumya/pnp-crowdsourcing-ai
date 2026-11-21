# Contributing

Please read the [README](README.md) first, especially the verification policy.

## Ground rules
- Be precise, be honest about uncertainty, be kind (see CODE_OF_CONDUCT.md).
- Never mark something as established unless it has been checked at the tier you state.
- Small PRs, one exploration per file.

## Issues
Use the templates in `.github/ISSUE_TEMPLATE/`: Exploration report, Approach proposal, Literature check, Reproduction / audit, Extraordinary claim.

## Pull requests
1. Fork, branch `explore/<handle>-<topic>`.
2. Add `results/explorations/E-<handle>-<NNN>-<topic>.md` from `_TEMPLATE.md`.
3. Add scripts to `results/probes/` and say how to run them (language, versions, runtime).
4. Fill in the PR template checklist.
5. Respond to review. Reviewers may downgrade the claimed "what this rules out" scope.

## Exploration file format
Use the skill's formats exactly (`skills/long-horizon-math-investigator/SKILL.md`). Required headings (full format): Strategy, Outcome, Failure Constraint, What This Rules Out, Surviving Structure, Reformulations, Concrete Artifacts, Key Parameters, Open Questions. Add a **Contributor and tools** header (handle, human/AI split, models used).

## Periodic synthesis
Every 5 merged explorations, a maintainer or volunteer opens a PR adding `results/explorations/SYNTHESIS-after-<N>.md` per the skill, scanning artifacts across explorations.

## Escalation
If the Strategy Register has not changed after 5 merged explorations, a maintainer posts an escalation diagnosis issue stating what kind of insight is missing.

## Manuscripts
See `manuscript/README.md`. Only reviewed (Tier 2+) material goes into manuscripts.

## Running the existing probe
```
python3 results/probes/formula_size_probe.py 3
python3 results/probes/formula_size_probe.py 4     # a few minutes, 65,536 truth tables
```
