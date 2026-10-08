# Genomic and Molecular Analysis of a 17p13.3 Microdeletion and Its Candidate Visual-Neurological Mechanisms

**Author:** Zachariah P. Laing  
**ORCID:** 0009-0004-8765-4601  
**Version:** 1.0 frozen first-pass in silico research record  
**Primary assembly:** GRCh37/hg19  
**Index interval:** chr17:1,411,408-1,841,103  
**Variant:** heterozygous deletion  
**Nominal span:** 429,696 bp  
**License:** CC-BY-NC-SA 4.0

This repository preserves the complete Version 1.0 project record for the 17p13.3 microdeletion analysis. It is organized to preserve the frozen phase structure, evidence boundaries, negative findings, and reproducibility record rather than silently rewriting earlier conclusions.

## Repository contents

- `manuscript/` - the complete integrated APA 7 project manuscript and a searchable plain-text export.
- `phases/` - the six final phase records extracted directly from the final integrated project PDF.
- `scripts/` - reproducible phase-extraction utility.
- `MANIFEST.sha256` - SHA-256 checksums for the integrated PDF and six phase PDFs.
- `CITATION.cff` - citation metadata.
- `LICENSE` - CC-BY-NC-SA 4.0 license notice.
- `NOTICE.md` - third-party-material and scientific-record notice.

## Final phase records

The standalone phase records are page-preserving extracts from the final integrated Version 1.0 PDF; no scientific wording was rewritten during extraction.

| Phase | Final record | Integrated PDF pages | Scope |
|---|---|---:|---|
| 1 | `phases/Phase_1_Final_Record.pdf` / `.txt` | 4-32 | Locus characterization and structural definition |
| 2 | `phases/Phase_2_Final_Record.pdf` / `.txt` | 33-79 | Molecular and chemical characterization |
| 3 | `phases/Phase_3_Final_Record.pdf` / `.txt` | 80-183 | Spatiotemporal functional genomics |
| 4 | `phases/Phase_4_Final_Record.pdf` / `.txt` | 184-244 | Dosage sensitivity, perturbation, convergence, and adjudication |
| 5 | `phases/Phase_5_Final_Record.pdf` / `.txt` | 245-249 | Deterministic evidence integration and reproducibility analysis - available frozen summary v1.0 |
| 6 | `phases/Phase_6_Final_Record.pdf` / `.txt` | 250-265 | Project conclusion, critical appraisal, forward research paths, and frozen record |

The vocabulary/formulas appendix, consolidated references, and final CC-BY-NC-SA 4.0 licensing notice remain in the integrated manuscript.

## Fixed genomic reference

Unless formally reopened through a documented correction or breakpoint-resolving evidence, the project uses:

- Assembly: **GRCh37/hg19**
- Chromosome: **17**
- Interval: **1,411,408-1,841,103**
- Variant: **heterozygous deletion**
- Nominal size: **429,696 bp**

Affected loci: INPP5K, PITPNA, SLC43A2, SCARF1, RILP, PRPF8, TLCD2, WDR81, SERPINF2, SERPINF1, SMYD4, RPA1, RTN4RL1, PITPNA-AS1, MIR22HG, MIR22, and RN7SL105P. INPP5K and RTN4RL1 are boundary-intersected.

## Frozen working interpretation

The deletion is biologically consequential and contains plausible mechanisms involving retinal support, membrane/phosphoinositide biology, trafficking, stress/DNA-damage response, neuronal development, and network organization. The accumulated evidence favors a distributed functional-reserve model over a single-gene photosensitivity mechanism. The Version 1.0 record does **not** establish that this exact heterozygous CNV directly causes epileptic photosensitivity, photoparoxysmal responses, or visually triggered seizures.

## Evidence discipline

The project distinguishes genomic evidence, molecular mechanism, spatiotemporal opportunity, dosage/perturbation, molecular phenotype, cellular phenotype, developmental effect, tissue/system physiology, organism phenotype, human phenotype, and causality. Findings from knockout, biallelic loss, missense variants, pharmacological inhibition, or other genotype states are not treated as automatically equivalent to heterozygous deletion.

## Reproducing the phase PDFs

With PyMuPDF installed, run:

```bash
python scripts/extract_phase_pdfs.py
```

The script uses the frozen integrated manuscript and the recorded page boundaries above. Compare resulting hashes against `MANIFEST.sha256` when validating archival copies.

## Citation

Laing, Zachariah P. *Genomic and Molecular Analysis of a 17p13.3 Microdeletion and Its Candidate Visual-Neurological Mechanisms*. Version 1.0, 2026. ORCID: 0009-0004-8765-4601.

## License

Except where otherwise noted, original project material is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC-BY-NC-SA 4.0)**. Third-party publications, database records, quoted material, and externally sourced figures or factual records remain subject to their respective rights and terms.
