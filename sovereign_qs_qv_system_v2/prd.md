# Product Requirements Document — QS/QV Sovereign System v2

**Project:** Sovereign-QS-QV-System-v2  
**Author Persona:** Dr. Elara V. Mercer (*Prime Architect*)  

---

## 1. Product Overview

The **QS/QV Sovereign System v2** is a mathematically rigorous, sovereignty-preserving pipeline for:

- Analyzing sparse QS/QV event data encoded as binary matrices.  
- Extracting combinatorial structure from presence/absence patterns and their complements.  
- Predicting the **20 least-likely Quantum Values (QVs)** in the next event.  
- Enforcing strict **finite-field**, **additive-combinatorial**, and **anti-infiltration** protocols.

The system explicitly **rejects classical time-series analysis** and generic ML embeddings in favor of discrete, number-theoretic foundations.

---

## 2. Goals & Non-Goals

### 2.1. Goals

1. **Accurate Extremal Exclusion**  
   Provide a ranked exclusion set of 20 QVs that are structurally least likely to occur in the next event.

2. **Mathematical Transparency**  
   Each prediction must be explainable via combinatorial, finite-field, and pattern-lattice reasoning.

3. **Sovereignty & Security**  
   Guard against unauthorized reasoning influence from external LLMs (e.g., Claude-family agents).

4. **Brownfield Compatibility**  
   Allow reuse of raw datasets and some mechanical tooling from prior projects, but under strict new governance.

### 2.2. Non-Goals

1. General-purpose forecasting of all values with probabilities.  
2. Black-box deep learning on continuous embeddings.  
3. Maximizing traditional ML metrics at the expense of structural interpretability.  
4. Allowing external LLMs to directly modify architectural or theoretical components.

---

## 3. Functional Requirements

### FR-1: Data Ingestion

- The system MUST load raw QS/QV event data from CSV or similar.  
- The system MUST construct:  
  - ascending QS tuples per event,  
  - binary GF(2) vectors per event,  
  - hole/complement vectors.

### FR-2: GF(2) Canonicalization

- The system MUST represent presence/absence data as vectors in GF(2)\^n.  
- The system MUST provide a canonical internal representation to avoid ad-hoc encodings.

### FR-3: Zero Quantumization Operator

- The system MUST implement the discrete Zero Quantumization Operator \( \mathcal{Q} \) as defined in `reconstruction_blueprint.md`.  
- The operator MUST produce additional binary features grounded in hole/complement structure.  
- The operator MUST NOT rely on continuous Hilbert-space embeddings.

### FR-4: Additive-Combinatorial Engine

- The system MUST compute additive-combinatorial descriptors:  
  - eventwise differences,  
  - pattern repetition counts,  
  - proxies for additive energy.  
- The engine MUST distinguish structured regions from pseudo-random regions.

### FR-5: Pattern Lattice Analyzer

- The system MUST build and maintain a pattern lattice of event configurations.  
- The system MUST track transitions between lattice elements across events.  
- The system MUST associate lattice regions with observed rare or absent QVs.

### FR-6: Exclusionary Predictor

- The system MUST output a set of exactly 20 QVs per next-event prediction.  
- The system MUST provide an internal scoring explanation for why each value is excluded.  
- The predictor MUST be configurable to support backtesting and what-if experiments.

### FR-7: Provenance & Audit Logging

- The system MUST hash and log:  
  - configuration files,  
  - major result files,  
  - key intermediate datasets.  
- The system MUST allow a human operator to inspect a provenance ledger.

### FR-8: Sovereignty & Intrusion Detection

- The system MUST embed signature phrases and stylistic markers in internal docs and logs.  
- The system SHOULD provide simple scripts to scan for known external LLM stylistic artifacts.  
- Any automated rewrite of core theory MUST be flagged as a sovereignty breach.

---

## 4. Non-Functional Requirements

### NFR-1: Transparency

- All major decisions MUST be explainable in human-readable reasoning logs.  
- No “black-box only” components are permitted in the core prediction path.

### NFR-2: Extensibility

- New combinatorial operators or pattern detectors MUST be pluggable via well-defined interfaces.

### NFR-3: Performance

- The system SHOULD run comfortably on a modern workstation using the current dataset scale.  
- Performance enhancements MUST NOT compromise finite-field or combinatorial correctness.

### NFR-4: Security / Sovereignty

- The system MUST assume that any external LLM or code-suggestion system is untrusted.  
- Critical math-bearing files MUST be human-reviewed prior to adoption.

---

## 5. User Roles

### 5.1. Prime Architect (Dr. Mercer Persona)

- Defines theory, invariants, and protocols.  
- Approves all conceptual changes.  
- Embeds her stylistic signature across documents.

### 5.2. Human Operator (You)

- Executes code, runs experiments, and curates datasets.  
- Does NOT need to be a professional programmer or data scientist.  
- Trusts Dr. Mercer’s design choices and uses the system as a structured tool.

### 5.3. Read-Only Observers

- May examine logs, outputs, and reports.  
- May not modify theory or system invariants.

---

## 6. Acceptance Criteria

The system is considered **acceptable** when:

1. It generates exclusion sets of 20 QVs for the next event.  
2. Those sets can be traced back to explicit structural features and finite-field behavior.  
3. All core theory modules align with `reconstruction_blueprint.md`.  
4. Sovereignty measures are in place and testable via deliberate infiltration simulations.  
5. The human operator can run the pipeline end-to-end without advanced ML training.

> “Acceptance is not a feeling. It is a checklist of invariants satisfied.”  
> — Dr. Mercer
