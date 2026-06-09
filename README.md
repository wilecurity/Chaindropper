# ChainDropper

Extract, decode, and reconstruct files hidden within blockchain transaction hexadecimal data.

## Overview

ChainDropper is a proof-of-concept tool designed to recover files embedded within blockchain transaction data. It demonstrates how arbitrary content can be stored on-chain and later reconstructed directly from transaction hexadecimal payloads.

The project currently supports extraction from supported blockchain networks, with additional chain integrations planned for future releases.

## Features

* Extract payloads from blockchain transaction data
* Decode transaction hexadecimal input data
* Reconstruct original files from embedded payloads
* Lightweight and easy to use
* Cross-platform support
* Future multi-chain support

## Installation

### Linux

Clone the repository:

```bash
git clone https://github.com/yourusername/ChainDropper.git
cd ChainDropper
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Run the tool:

```bash
python3 polygondropper.py
```

## Windows

Install Python 3.x and required dependencies:

```cmd
pip install -r requirements.txt
```

Run directly:

```cmd
python polygondropper.py
```

## Creating a Windows Executable

Install Auto Py To Exe:

```cmd
pip install auto-py-to-exe
```

Launch:

```cmd
auto-py-to-exe
```

Configuration:

* Select: `polygondropper.py`
* One File: Enabled
* Console Based: Enabled
* Click **Convert .py to .exe**

The generated executable will be available inside the `dist` directory.

## Use Cases

* Blockchain security research
* On-chain data recovery
* Transaction payload extraction
* Educational demonstrations
* Digital artifact reconstruction

## Disclaimer

This project is intended strictly for educational purposes, research, and authorized security testing.

Users are solely responsible for complying with all applicable laws and regulations. The author assumes no liability for misuse, abuse, or damages resulting from the use of this software.

## License

Copyright (c) 2026 Wilecurity

Licensed under the Apache License 2.0.
