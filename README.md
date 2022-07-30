# pyValkLib
Python library for reading and writing files in the Valkyria Chronicles game series. The goal of this library is to provide interfaces for these files, so that end-user tools can ignore the details of reading and writing them.

pyValkLib is intended as a research tool, with an eventual companion ValkLib library providing a clean C++ implementation of the read-and-write logic.


## Completion Status
The status of the code is tabulated for the different filetypes given in the sections below, with the following keys:

#### Read/Write Key
| Key | Status | Definition |
| --- | --- | --- |
|✔️| Supported | A complete production-ready Interface Object exists.|
|🟡| Partial Support | A partially-complete Interface Object or fully complete Read/Writer object exists.|
|❌| Not supported | Insufficient code exists for a complete Read/Writer. |

#### API Key
| Key | Status | Definition |
| --- | --- | --- |
|✔️| Stable | Breaking changes in Interface Object API unlikely between versions.|
|🟡| Mostly stable | Breaking changes in Interface Object API may happen versions.|
|❌| Unstable | Breaking changes in Interface Object API to be expected between versions. |

### Valkyria Chronicles 1

| Filetype | Read | Write | API 
| --- | --- | ---| -- |
| ABD | ❌ | ❌ | ❌ | 
| ABR | ❌ | ❌ | ❌ | 
| BF1 | ❌ | ❌ | ❌ | 
| BHV | ❌ | ❌ | ❌ | 
| BIN | ❌ | ❌ | ❌ | 
| CSD | ❌ | ❌ | ❌ | 
| ESR | ❌ | ❌ | ❌ | 
| GRD | ❌ | ❌ | ❌ | 
| HCA | ❌ | ❌ | ❌ | 
| HCM | ❌ | ❌ | ❌ | 
| HMD | ❌ | ❌ | ❌ | 
| HMM | ❌ | ❌ | ❌ | 
| HMO | ❌ | ❌ | ❌ | 
| HMT | ❌ | ❌ | ❌ | 
| HSC | ❌ | ❌ | ❌ | 
| HSM | ❌ | ❌ | ❌ | 
| HSP | ❌ | ❌ | ❌ | 
| HTR | ❌ | ❌ | ❌ | 
| HTX | ❌ | ❌ | ❌ | 
| MCL | ❌ | ❌ | ❌ | 
| MLX | ❌ | ❌ | ❌ | 
| MMF | ❌ | ❌ | ❌ | 
| MMR | ❌ | ❌ | ❌ | 
| MSB | ❌ | ❌ | ❌ | 
| MTP | ❌ | ❌ | ❌ | 
| MXE | 🟡 | 🟡 | ❌ | 
| NAD | ❌ | ❌ | ❌ | 
| PVS | ❌ | ❌ | ❌ | 


### Valkyria Chronicles 2

[Filetypes not enumerated]

### Valkyria Chronicles 3

[Filetypes not enumerated]

### Valkyria Chronicles 4

[Filetypes not enumerated]
 
