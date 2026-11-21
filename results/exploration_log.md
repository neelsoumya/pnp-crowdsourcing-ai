# Exploration Log: P vs NP

## Strategy Register

**Eliminated approach classes:**
- Relativizing proofs (diagonalization, simulation-only arguments). Ruled out at exploration 2: Baker-Gill-Solovay 1975 gives oracles A, B with P^A = NP^A and P^B != NP^B, so any technique that holds relative to every oracle cannot decide the question.
- Natural proofs (a constructive, large property of Boolean functions that is useful against P/poly). Ruled out at exploration 2 under the assumption that strong pseudorandom functions exist (Razborov-Rudich 1994).
- Algebrizing proofs (arithmetization-based extensions of relativization). Ruled out at exploration 2: Aaronson-Wigderson 2008 give algebraic oracle separations in both directions.
- Direct extension of formula-size lower bound methods (Khrapchenko, Andreev, Hastad) to general circuits. Ruled out at exploration 1 and 2 as a *direct* extension: these rely on tree structure (each gate output used once), and the best known formula lower bounds are about n^(3-o(1)), far from superpolynomial.
- Brute-force search for a small counterexample. Not applicable: P != NP is a statement about all input lengths asymptotically, so no finite computation can refute or prove it.

**Active structural constraints:**
- Any proof of P != NP must be non-relativizing, non-algebrizing, and either non-natural or use a property that is not both constructive and large (exploration 2).
- Proving NP not contained in P/poly would suffice, but the best known general-circuit lower bound for an explicit NP function is only about 3.1n (Li-Yang 2022 improved on 3n-o(n)), i.e. linear (exploration 2, from literature, not re-derived).
- Parity on n variables needs formula size exactly n^2 at n=4 (16 leaves), matching Khrapchenko's n^2 bound (exploration 1).

**Known reformulations:**
- NP not in P/poly (non-uniform circuit lower bound), which implies P != NP (exploration 2).
- Proof complexity: NP != coNP would follow from superpolynomial lower bounds for every propositional proof system (Cook-Reckhow). Current lower bounds exist only for weak systems (resolution, bounded-depth Frege) (exploration 2).
- Geometric Complexity Theory: permanent vs determinant as an orbit-closure containment problem, targeting VP vs VNP (the algebraic analogue), via representation-theoretic obstructions (exploration 2, literature).

**Stagnation check:** Explorations 1-2 were the first two; no escalation yet. Honest status: no structural progress beyond cataloguing known barriers.

---

## Exploration 1 (probe)

### Strategy
Compute exact minimum de Morgan formula sizes for all Boolean functions on 3 and 4 variables, to see concretely what a lower bound looks like at small n.

### Outcome
SUCCEEDED (as a probe; it settles nothing about P vs NP).

### Concrete Artifacts
Method: DP over truth tables. Cost = number of leaves in an AND/OR formula, with negation free on variables. Script: probe.py, below.
- n=3: all 256 functions covered. Maximum formula size 10, attained by parity (and its complement). Last new functions appeared at size 10 (2 functions).
- n=4: all 65536 functions covered. Maximum formula size 16, attained by parity. Count of new functions: size 14 -> 1472, size 15 -> 96, size 16 -> 114 (cumulative 65326, 65422, 65536).
- Parity_4 formula size 16 = 4^2, matching Khrapchenko's lower bound n^2 for parity (tight here).

```
n=int(sys.argv[1]); N=1<<n; FULL=(1<<N)-1
cost: truth-table -> min leaves; seed with variables and negations at cost 1
for c = 2,3,...: for a+b=c, for f in level a, g in level b: record f&g, f|g at cost c
```

---

## Exploration 2

### Strategy
Survey which proof-technique classes are already known to be incapable of resolving P vs NP, so that a new attempt starts from the surviving region of technique space.

### Outcome
SUCCEEDED as a map; FAILED as a route to a proof. This is a wrong-strategy failure, not a missing-lemma failure: no technique in the surviving region was found that could be pursued with the tools available here.

### Failure Constraint
Every candidate I could formulate falls into one of: (a) relativizes, (b) algebrizes, (c) is a natural proof against strong PRFs, or (d) reduces to a stronger open problem (e.g. an explicit super-linear general circuit lower bound for an NP function, which is itself open). I could not state a candidate that avoids all four.

### What This Rules Out
Any argument whose steps all hold in the presence of an arbitrary oracle (BGS). Any argument whose key step is an efficiently checkable property true of most Boolean functions and false of all small circuits (Razborov-Rudich, conditional on PRFs). Any argument that survives low-degree-extension oracles (Aaronson-Wigderson). Scope of the natural proofs barrier is conditional, so it eliminates the class only if one-way functions exist.

### Surviving Structure
- Non-black-box techniques exist and have worked elsewhere: IP = PSPACE (arithmetization, but it relativizes in the algebrizing sense), Williams' ACC^0 lower bound for NEXP (2011), which evades natural proofs by using a non-constructive-large property via a faster-than-brute-force SAT algorithm. This "algorithms imply lower bounds" template is the most successful recent non-barrier-hitting method.
- Meta-complexity (MCSP, Kolmogorov complexity hardness, Hirahara's results) is currently an active frontier connected to one-way functions.

### Reformulations
See Strategy Register: NP not in P/poly, proof-complexity form, GCT form.

### Concrete Artifacts
Literature facts used (cited from memory, not re-verified this session, so treat as to be checked): BGS 1975; Razborov-Rudich 1994; Aaronson-Wigderson 2008; Williams 2011; Khrapchenko 1971 (parity n^2); Hastad / Tal formula lower bounds near n^3; best explicit general circuit lower bound for NP about 3.1n.

### Key Parameters
None computed. Pure literature survey.

### Open Questions
- Is there a restricted circuit class between ACC^0 and P/poly where a Williams-style algorithms-to-lower-bounds argument can give an NP lower bound?
- Does a magnification result (small improvements in lower bounds for MCSP-type problems imply big separations) give a path that is non-natural? Next probe: write down the precise magnification statements and check whether the required lower bound is within current reach.

---

## Next session plan
1. Resume from exploration 2. 
2. Concrete target: test whether any magnification theorem's hypothesis is currently provable, and log the exact gap.
3. Synthesis due after exploration 5.
