# Crowdsourcing P vs NP

An open, public, crowdsourced attempt to make progress on the **P versus NP** problem, by combining human mathematicians and computer scientists with AI assistants, under a strict logging and verification discipline.

>  P vs NP is a very hard problem that has resisted attack since the early 1970s. 

<!--
The overwhelmingly likely outcome of this project is **not** a proof. The goal is a well-documented map of what has been tried, what has been ruled out, and what structure survives. In the skill's words: *a well-documented dead end is more useful than an undocumented spiral.* Any claim of a full resolution is treated with the highest scrutiny (see [Verification policy](#verification-policy)).
-->

## Contents

- [The problem](#the-problem)
- [Why it is hard: the known barriers](#why-it-is-hard-the-known-barriers)
- [How this repository works](#how-this-repository-works)
- [Repository layout](#repository-layout)
- [How to contribute](#how-to-contribute)
- [Verification policy](#verification-policy)
- [Using AI assistants responsibly](#using-ai-assistants-responsibly)
- [Current status](#current-status)
- [Where to start](#where-to-start)
- [Licensing and credit](#licensing-and-credit)

## The problem

**P** is the class of decision problems solvable by a deterministic algorithm in time polynomial in the input size. **NP** is the class of decision problems whose "yes" answers have certificates that can be *checked* in polynomial time. Clearly P is contained in NP. The question is whether the containment is strict:

> Is every problem whose solutions can be verified quickly also solvable quickly? i.e. is **P = NP**?

Most researchers believe **P ≠ NP**. 

<!--
Because SAT is NP-complete (Cook-Levin, 1971), the question reduces to a single concrete problem: *is there a polynomial-time algorithm for Boolean satisfiability?*

Two routes to P ≠ NP:

1. **Non-uniform:** show an explicit NP function requires superpolynomial-size Boolean circuits (NP not in P/poly). This implies P ≠ NP.
2. **Uniform:** show directly that no polynomial-time Turing machine decides SAT.

What a resolution would look like:

- **P = NP** would be a polynomial-time algorithm for SAT, with a correctness proof and a runtime bound.
- **P ≠ NP** is a lower bound: a statement about *all* algorithms. No finite computation can establish it.

So "find a counterexample" cannot be done by brute-force search over finite objects. Computation helps in other ways: testing conjectures on small cases, searching for circuits, finding structure that suggests lemmas.

-->

## Why it is hard: the known barriers

Any serious attempt must avoid three proven obstacles. Each rules out a whole *class* of proof techniques.

| Barrier | What it rules out | Reference |
|---|---|---|
| **Relativization** | Proofs that hold relative to every oracle (e.g. pure diagonalization/simulation) | Baker-Gill-Solovay, 1975 |
| **Natural proofs** | Constructive, "large" properties of Boolean functions that are useful against P/poly, *if* strong pseudorandom functions exist | Razborov-Rudich, 1994 |
| **Algebrization** | Techniques that survive low-degree algebraic extensions of oracles | Aaronson-Wigderson, 2008 |

Techniques that have worked *around* barriers for restricted problems include Williams' "algorithms imply circuit lower bounds" method (NEXP not in ACC^0, 2011), and the study of meta-complexity (MCSP, Kolmogorov complexity). Geometric Complexity Theory and proof complexity are other long-term programs.

Please verify all citations before relying on them; the first sessions assembled them from memory and flagged them as unverified.

## How this repository works

The project follows the **Long-Horizon Mathematical Investigation** skill (`skills/long-horizon-math-investigator/SKILL.md`). Its core ideas:

- **Log every attempt** (failed or not) with a precise *failure constraint*, what class of approaches it *rules out*, what *structure survives*, and any *reformulations* it reveals.
- Maintain a **Strategy Register**: eliminated approach classes, active structural constraints, known reformulations.
- Do **periodic synthesis** every 5 explorations: look across artifacts for patterns.
- **Escalate honestly** when the register stops changing.

The crowdsourced version of this protocol:

- Every contributor writes **one file per exploration** in `results/explorations/`. 
- *Please append your full name to the filename*
- Maintainers (and reviewers) fold accepted explorations into `results/STRATEGY_REGISTER.md`.
- The original two sessions that seeded this repository live in `results/exploration_log.md`.

## Repository layout

```
.
├── README.md                      This file
├── CONTRIBUTING.md                Detailed contributor guide
├── CODE_OF_CONDUCT.md
├── LICENSE
├── skills/
│   └── long-horizon-math-investigator/SKILL.md    The investigation protocol
├── prompts/                       Prompts used so far, plus reusable templates
├── results/
│   ├── exploration_log.md         Seed log (explorations 1-2)
│   ├── STRATEGY_REGISTER.md       Canonical register (maintainer-edited)
│   ├── explorations/              One file per crowdsourced exploration
│   └── probes/                    Scripts that generated computed artifacts
├── manuscript/
│   ├── README.md                  Manuscript policy
│   └── template/                  LaTeX template
├── docs/
│   ├── barriers_checklist.md      Check any proposed approach against this
│   └── reading_list.md            Starting literature (verify before citing)
└── .github/
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

## How to contribute

Full details are in [CONTRIBUTING.md](CONTRIBUTING.md). Summary:

### 1. Pick a contribution type

| You want to... | Do this |
|---|---|
| Report an attempt (success or failure) | Open an **Exploration report** issue, or PR a file into `results/explorations/` |
| Propose a new approach before investing time | Open an **Approach proposal** issue and run it through `docs/barriers_checklist.md` |
| Check a literature claim or citation | Open a **Literature check** issue (very valuable: many entries are unverified) |
| Reproduce or audit a computation | Open a **Reproduction / audit** issue |
| Improve a script, add a probe | PR into `results/probes/` with a README line on what it computes |
| Write up a result | PR into `manuscript/` (see manuscript policy) |
| Claim a full proof of P ≠ NP or P = NP | See the [verification policy](#verification-policy); use the **Extraordinary claim** issue template |

### 2. Workflow (pull requests)

1. Fork the repository and create a branch: `explore/<handle>-<short-topic>`.
2. Copy `results/explorations/_TEMPLATE.md` to `results/explorations/E-<handle>-<NNN>-<topic>.md` and fill it in using the skill's **full format** (substantive attempts) or **short format** (quick probes).
3. Put every script that produced a number in `results/probes/`. Artifacts must be recorded **in full**, not by reference.
4. Open a pull request using the template. Do **not** edit `STRATEGY_REGISTER.md` yourself; propose register changes in the PR description.
5. A reviewer checks: (a) the log is complete, (b) artifacts reproduce, (c) the claimed "what this rules out" scope is justified.
6. After merge, a maintainer updates the Strategy Register.

### 3. Rules for good explorations

- **Failure is a result.** State the *structural* reason for failure, precise enough to grep for.
- **Scope claims honestly.** Say how much your failure rules out, and your confidence.
- **Distinguish failure types:** wrong strategy vs missing lemma vs unverified step.
- **Cite precisely** and mark anything unverified as such.
- **One idea per file.** Small, reviewable PRs.


## Verification policy

Where an AI has contributed a genuine new result in a famous area, the bar that was met was independent examination by human mathematicians plus a machine-checked formalization. That is the bar here.

- **Tier 0 (idea):** Anything, labeled as such.
- **Tier 1 (logged):** Complete exploration entry with reproducible artifacts.
- **Tier 2 (reviewed):** A second contributor independently reproduced computations or checked the argument.
- **Tier 3 (formalized or expert-validated):** Machine-checked (Lean 4 / Coq / Isabelle) *or* checked by a domain expert in writing.
- **Extraordinary claims** (a full resolution of P vs NP, or any claim that overturns a classical barrier theorem): must be a **short, self-contained, complete** argument, must explicitly state where it evades each barrier in `docs/barriers_checklist.md`, and will not be announced as a result until Tier 3. Most such claims fail at the point where the same argument would also "prove" something false (for example a relativized or algebrized version). **Test your argument against that first.**
- Do not use this repository to submit claims to the Clay Mathematics Institute; its rules require publication in a qualifying venue and a waiting period.




## Using AI assistants responsibly

AI assistants are welcome, with these rules:

- **Disclose** in each exploration file which tool/model produced which part.
- **Humans stay accountable.** 
- **Do not trust AI-asserted citations or computations.** Verify every reference exists and says what is claimed; rerun every script.

## Current status

- Explorations logged: **2** (seed). See `results/exploration_log.md`.
- Computed artifact: exact minimum de Morgan formula sizes for all Boolean functions on 3 and 4 variables (parity: 10 and 16 leaves; n=4 matches Khrapchenko's n^2 bound).
- Literature survey of barriers: done, **unverified citations**.
- Next planned step: test whether any *magnification* theorem's hypothesis is within reach of current lower bounds, and log the exact gap.
- No new theorem has been proved.

## Where to start

1. **Literature checks.** Verify each citation in `results/exploration_log.md` and `docs/reading_list.md`.
2. **Extend the formula-size probe** to n=5 using smarter enumeration or SAT-based synthesis, and compare with known bounds.
3. **Circuit (not formula) size** for small functions, via SAT-based exact synthesis.
4. **Magnification survey:** state each known magnification theorem precisely, with its required lower bound, and record the gap to the best known bound.
5. **Barrier checklist:** run published partial results (e.g. ACC^0 lower bounds) through the checklist and document why each evades the barriers.

## My initial start

- My initial (admittedly crappy) first start

- Start with [Claude](https://claude.ai/new)

- I started with the [SKILLS.md](skills/long-horizon-math-investigator/SKILL.md)

- Started with the following prompt

> /long-horizon-math-investigator find me a proof or counterexample for P is not equal NP. believe in your self. you have superpowers



## Licensing and credit

- Code is under the MIT license (see `LICENSE`). Choose a license for text/results (for example CC BY 4.0); this is an open decision for the maintainers.
- `skills/long-horizon-math-investigator/SKILL.md` was supplied with the Claude environment this project began in. 
- Contributors are credited by handle in each exploration file and in manuscript author lists.


## Contact

[Soumya Banerjee](https://sites.google.com/site/neelsoumya/)

sb2333@cam.ac.uk

