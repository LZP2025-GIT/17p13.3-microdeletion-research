from pathlib import Path
import fitz

SOURCE = Path('manuscript/Genomic_and_Molecular_Analysis_of_a_17p13.3_Microdeletion_and_Its_Candidate_Visual-Neurological_Mechanisms_CC-BY-NC-SA-4.0.pdf')
RANGES = {1:(4,32),2:(33,79),3:(80,183),4:(184,244),5:(245,249),6:(250,265)}
outdir=Path('phases'); outdir.mkdir(exist_ok=True)
src=fitz.open(SOURCE)
for n,(start,end) in RANGES.items():
    out=fitz.open(); out.insert_pdf(src, from_page=start-1, to_page=end-1)
    out.save(outdir/f'Phase_{n}_Final_Record.pdf', garbage=4, deflate=True)
    out.close()
src.close()
