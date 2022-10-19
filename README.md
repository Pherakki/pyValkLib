# pyValkLib
Python library for reading and writing files in the Valkyria Chronicles game series. The goal of this library is to provide interfaces for these files, so that end-user tools can ignore the details of reading and writing them.

pyValkLib is intended as a research tool, with an eventual companion ValkLib library providing a clean C++ implementation of the read-and-write logic.

Documentation is available in the `docs` folder of the repository. Since the library is in-development this is currently very barebones. The API for Supported interfaces will be provided in the documentation, as well as a qualitative description of the filetypes pyValkLib reads and writes.

## README Table of Contents
| Section | Contents |
|---|---|
| [Used By](#used-by) | A list of programs known to use pyValkLib. |
| [Acknowledgements](#acknowledgements) | Important acknowledgements of assistance and resources used in the development of this library. |
| [Completion Status](#completion-status) | Which filetypes can currently be read by the library, and to which degree. |

## Used By
- [MXEEditor](https://github.com/Pherakki/MXEEditor)
    - Capable of unpacking and rebuilding entire MXE files, and allowing the deletion and addition of new records in these files. 
    - Intended to be a more powerful successor program to [ValkyrieEdit](https://github.com/dhavard/ValkyrieEdit).

## Acknowledgements
This library does not exist in a vacuum; several others have written codebases for reading Canvas engine formats. Two (at the time of writing, unmaintained?) repositories have influenced the development of pyValkLib, for which I give credit to the authors:
- [import_valkyria](https://github.com/gomtuu/import_valkyria) by [gomtuu](https://github.com/gomtuu), featuring contributions and research from chrrox and [angavrilov](https://github.com/angavrilov).
    - The goal of this repository was to read the model formats in Valkyria Chronicles. Although the scope was limited to reading and extracting information only relevant for importing the models to Blender, this repository nonetheless provided valueable information on the structure of several formats, as well as the general container-tree structure used by the files. In particular, this repository has so far greatly assisted in sketching out the overall structure of HMDL, HSHP, and HMOT containers.
- [ValkyrieEdit](https://github.com/dhavard/ValkyrieEdit) by [dhavard](https://github.com/dhavard).
    - The goal of this repository was to allow the editing of game data records contained within the MXE files. This repository has helped with identifying the purpose of many variables contained within these records.

## Completion Status
The status of the code is tabulated for the different filetypes given in the sections below, with the following keys:

#### Read/Write Key
| Key | Status | Definition |
| --- | --- | --- |
|✔️| Supported | A complete production-ready Interface Object exists.|
|🟡| Partial Support | A partially-complete Interface Object or usable Read/Writer object exists.|
|❌| Not supported | Insufficient code exists for a complete Read/Writer. |

#### API Key
| Key | Status | Definition |
| --- | --- | --- |
|✔️| Stable | Breaking changes in Interface Object API unlikely between versions.|
|🟡| Mostly stable | Breaking changes in Interface Object API may happen versions.|
|❌| Unstable | Breaking changes in Interface Object API to be expected between versions. |

### Valkyria Chronicles 1

| Filetype | Read | Write | API | Purpose | Notes |
| --- | --- | ---| -- | -- | -- |
| ABD | ❌ | ❌ | ❌ | 3D Model? | |
| ABR | ❌ | ❌ | ❌ | 3D Model? | |
| BF1 | ❌ | ❌ | ❌ | Font | |
| BHV | ❌ | ❌ | ❌ | ??? | |
| BIN | ❌ | ❌ | ❌ | ??? | |
| CSD | ❌ | ❌ | ❌ | SFX/VFX | |
| CVD | ❌ | ❌ | ❌ | ??? | |
| ESR | ❌ | ❌ | ❌ | ??? | |
| GRD | ❌ | ❌ | ❌ | ??? | |
| HCA | ❌ | ❌ | ❌ | ??? | |
| HCM | 🟡 | 🟡 | ❌ | Camera Animation | |
| HMD | ❌ | ❌ | ❌ | 3D Model | |
| HMM | 🟡 | 🟡 | ❌ | ??? | |
| HMO | 🟡 | 🟡 | ❌ | Animation? | |
| HMT | 🟡 | 🟡 | ❌ | 3D Model Animation | (1) |
| HSC | ❌ | ❌ | ❌ | ??? | |
| HSM | 🟡 | 🟡 | ❌ | ??? | |
| HSP | ❌ | ❌ | ❌ | 2D Sprite | |
| HST | ❌ | ❌ | ❌ | ??? | |
| HTR | ❌ | ❌ | ❌ | Texture Pack Metadata | |
| HTX | 🟡 | 🟡 | 🟡 | Texture Pack | (2)|
| MCL | 🟡 | 🟡 | ❌ | 3D Physics | (3)|
| MLX | ❌ | ❌ | ❌ | Generic 3D Data Pack | |
| MMF | ✔️ | 🟡 | ❌ | Asset Pack Metadata | (4) |
| MMR | 🟡 | 🟡 | ❌ | Asset Pack | (4) |
| MSB | ❌ | ❌ | ❌ | ??? | |
| MTP | ❌ | ❌ | ❌ | ??? | |
| MXE | 🟡 | 🟡 | ❌ | Database | (5)|
| NAD | ❌ | ❌ | ❌ | Script? | |
| PVS | ❌ | ❌ | ❌ | ??? | |

1) Basic read/write functionality achieved, but the purpose of the elements in the ReadWriters need to be more carefully defined.
2) Some HTSF containers have header flags of 0x10000000, and some have 0x10000004. It should be determined if these flags are determinable from the input DDS file or not before marking the Interface as "Complete" and upgrading the status of the API stability. The interface can be simplified to just a list of bytestrings if they can be calculated.
3) Basic read/write functionality achieved, but the purpose of the elements in the ReadWriters need to be more carefully defined.
4) MMFReadWriter and MMRReadWriter present. The MMR and MMF files are tightly coupled, and so these two files should be dealt with simultaneously. MMF files can in principle be parsed without the need for an MMR file. An MMF Interface is also present that is capable of extracting the contained files. This might be replaced with a single MMF Interface than can build both the MMR and MMF file, or such an object might be added as a third Interface.
5) First interface written, and thus is not as clean as it could be. Should be tidied up and given a proper interface. Some questions remain over whether some unknowns in the data can be calculated from the rest of the data, and being able to calculate them would simplify and alter the API.

### Valkyria Chronicles 2

[Filetypes not enumerated]

### Valkyria Chronicles 3

[Filetypes not enumerated]

### Valkyria Chronicles 4

[Filetypes not enumerated]
 
