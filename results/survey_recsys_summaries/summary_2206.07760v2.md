# Summary of 2206.07760v2.md

**Token Usage**: Input: 23154, Output: 659, Total: 23813

---

### Main Idea
- This research addresses the limitation of traditional single-cell transcriptomics analysis, which often relies on discrete clustering and differential gene expression (DGE) and may fail to detect continuous variation within and between cell types.
- The motivation is that cellular biology is nuanced with continuous transitions and variations within cell types, which traditional methods might miss.
- The paper proposes three topologically-motivated mathematical methods for unsupervised feature selection that consider discrete and continuous transcriptional patterns equally across multiple scales: Eigenscores, Multiscale Laplacian Score (MLS), and Persistent Rayleigh Quotient (PRQ).

### Technologies
- **Eigenscores:** Ranks genes based on their correspondence to low-frequency intrinsic patterning in the data using the spectral decomposition of the Laplacian graph. It calculates the alignment of gene signals with Laplacian eigenvectors.
- **Multiscale Laplacian Score (MLS):** An unsupervised method for locating relevant scales in data and selecting genes that are coherently expressed at these scales. It uses continuous-time random walks and Markov stability to rank genes according to their consistency with local to global geometric structures.
- **Persistent Rayleigh Quotient (PRQ):** Takes data equipped with a filtration (e.g., pseudo-time), allowing the separation of genes with different roles in a bifurcation process. It is based on the Kron reduced Laplacian and Rayleigh quotient.
- **UMAP:** Used to construct an undirected weighted k-nearest neighbor cell similarity graph from preprocessed single-cell data.
- **Seurat:** Used for preprocessing single-cell data.
- **Louvain algorithm:** Used for community detection in the MLS pipeline.
- **Variance of Information (VI):** Used to assess the consistency and robustness of partitions in the MLS pipeline.
- **Datasets:**
    - 2700 human peripheral blood mononuclear cells (PBMC).
    - 24,911 human T cells infiltrating lung tumors.
    - 447 mouse foetal liver cells at different developmental stages.

### Results
- The methods validated previously identified genes in the tested datasets and detected additional biologically meaningful genes with coherent expression patterns.
- Eigenscores identified genes enriched in broader cell types in the PBMC data, which were not highly ranked by DGE due to their expression in multiple cell clusters. It also identified the cell cycle as an important source of biological variation in the PBMC data.
- MLS in PBMC data revealed genes (GZMK and CD8B) with higher consistency at finer resolutions (t1) and others (GZMB and XCL2) with higher consistency at coarser resolutions (t3), indicating transitions between cell states.
- MLS applied to the T cell data identified IGKC and IFI27, representing T cell binding B cells, and an antiviral/interferon-induced response, respectively.
- PRQ applied to the mouse liver data differentiated genes involved in cell differentiation, identifying those expressed in parent cells (hepatoblasts) and daughter cells (hepatocytes and cholangiocytes).
- The methods can identify genes common to disparate cell types, spanning known cell types and providing possible pathway transitions between them, and provide multiple rankings of gene expression patterns at different scales of the data.
