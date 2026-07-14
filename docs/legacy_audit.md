# Legacy Audit

The preserved legacy work documents an important learning path. The limitations
below are recorded to protect the new research pipeline from treating
educational demonstrations as validated detector simulation.

## Known Numerical and Methodological Limitations

1. The Week 1 Boris integration advances particles using steps defined as a
   fraction of a complete gyroperiod. At detector-scale rigidities, a single
   step can span metres while the tracker is approximately metre scale.
2. Tracker-layer intersections are consequently interpolated from an
   under-resolved trajectory.
3. The saved integrated dataset has poor rigidity reconstruction:
   - Approximately 99% absolute relative error at the 68th percentile.
   - True/reconstructed rigidity correlation of approximately 0.12.
4. The simple parameterized tracker performs much more consistently, at
   approximately 2% absolute relative error at the 68th percentile, but remains
   a hand-defined response model.
5. The current tracker geometry is educational rather than AMS-like.
6. Current rigidity reconstruction depends indirectly on truth information and
   does not robustly reconstruct signed rigidity.
7. The Week 2 ECAL model samples only scalar Gaussian-like values.
8. `E_ecal` and `E_over_p` are sampled separately even though `E_over_p` should
   be derived from reconstructed energy and momentum/rigidity.
9. The classifier primarily learns manually assigned feature distributions.
10. Nearly perfect nuclear classification is driven by direct, lightly smeared
    charge proxies.
11. Electrons and positrons have identical simulated ECAL/TRD responses and
    therefore cannot be separated without tracker charge sign.
12. Overall accuracy hides the physically important proton-rejection problem.
13. The repository contained duplicated notebook code, top-level execution in
    Python files, generated data, cached bytecode, and notebook outputs
    containing machine-specific paths.
14. There were no proper package, test, configuration, or dependency
    boundaries.

## Educationally Useful Components

- The Week 1 notebooks introduce Lorentz-force motion, rigidity, beta, gamma,
  helical trajectories, and the basic idea of curvature fitting.
- The Boris-pusher examples are useful as learning material, but require
  detector-scale timestep control before reuse in validated tracking.
- The Week 2 notebooks illustrate the concept of redundant detector responses
  and the risk of building classifiers from hand-assigned distributions.
- The notes and paper summaries remain useful context for AMS-02 subsystems,
  cosmic-ray terminology, and future reading.

## Preservation

Legacy notebooks, Python exports, notes, generated CSVs, figures, and reference
PDFs are preserved on the GitHub `legacy` branch. Numerical results in those
files should not be edited except by an explicit historical-correction task.
