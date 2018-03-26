# Stereocilia Modeling

## Advisor
Manfred Auer (PI), Tom Goddard (UCSF)

## Purpose
Deafness and Hearing loss at various degrees affects 360 million to 1.1 billion people worldwide. ~10% of the population will become deaf over their lifetime, and one in a thousand children is being born deaf, and another one loses hearing before reaching adulthood. Over 100 deafness genes have been identified, and many of them affect the morphogenesis, function and degeneration of inner ear hair bundle, an organelle of hair cells, which directly convert mechanical signals such as sound to electrical signals. The hair bundle is composed of actin-rich rods, also known as stereocilia, protruding from the apical cell surface. <img align="right" src="images/Stereocilia_of_frog_inner_ear_wiki.jpg" | width=420> Despite significant progress being made over the last 2 decades, we still lack a comprehensive understanding of how these deafness genes affect stereocilia and hair bundle function.
Building on cryo-electron microscopy (EM) tomographic imaging work currently ongoing in the Auer laboratory, this project aims to derive a prototypic stereocilia and the hair bundle models through computational segmentation of identifiable macromolecular constituents (such as actin, actin-cross linkers as well as unconventional myosins), quantitative statistical volumetric analysis (length, numbers, order, distances) and building of an averaged prototypic model. We submit that such prototypic models will then allow us to compare the 3D organization and function of stereocilia and hair bundles under different conditions, including development, specific deafness gene malfunction and regeneration.

Using existing cryo-EM 3D tomographic whole mount stereocilia data sets, I will segment actin filaments and actin-actin/actin-membrane cross-connectors using semi-automated segmentation tools of the software packages UCSF Chimera and Dragonfly, as well as machine learning algorithms (Convolutional Neural Networks) currently being developed by our collaborator Dr. Chandrajit Bajaj at UT Austin. The segmented volumes will be built into volumetric models using approaches developed by our collaborators Dr. Silvia Crivelli (LBNL) and Dr. Nelson Max (UC Davis). This is followed by quantitative volumetric analysis, including number, orientation, length and distances of actin-filament segments and the actin-actin/actin-membrane cross-linkers. Independently I will subject segmented regions of stereocilia, featuring the space between the membrane and the actin core to template matching algorithms with unconventional myosin macromolecules as search templates, in order to identify the location of unconventional myosins along the stereocilia. The statistical data will inform a Computer Assisted Design (CAD) model of a prototypic stereocilium, which will be further assembled into a hair bundle, and used for subsequent computational simulation of stereocilia and bundle mechanical properties.

Successful completion of this project will not only yield unprecedented insight into the 3D architecture and thus function of hair cell stereocilia, but also will serve as a proof-of-principle study for our integrated bioimaging approach, that goes “beyond the pretty pictures” and aims for quantitative statistical analysis of volumetric parameters and for the generation of prototypic models that combine the information from different data sets not at the data, but at the model level. I submit that this integrated bioimaging approach will be applicable to a variety of other projects in the Auer lab and beyond.
