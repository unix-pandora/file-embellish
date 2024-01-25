# file-embellish

<hr>

## Implementation

Used for batch encryption and decryption of all files in the specified directory (including sub folders),
The scope includes: file name and file content.

<hr>

## Encryption methods used

- AES symmetric encryption algorithm
- DES symmetric encryption algorithm
- BASE64 encoding
- Caesar encryption method

<hr>

## Initialization

```
pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

```

<hr>

## Main entrance script

```
application
```

<hr>

## Input command format

```
python application.py --pattern number;
python application.py -p number;
```

<hr>

## Parameter Set Script (Fixed)

```
background_setting
```

<hr>

## Custom parameter input script

```
# here you need to enter the key and specify the directory path
front_reception
```

<hr>

## Module path file (pth) generation script

```
# needs to be executed before project execution
generate_project_pth
```

<hr>

## Common command text records required for the project

```
python-scripts.md
```

<hr>

## Pre steps

Before starting the project, it is necessary to execute the `generate_project_pth` script to generate the pth file, and then execute a command in the `python-scripts.md` to move the generated pth file to the environment ** site-packages ** directory, so that the project can find the path of the custom module at runtime

<hr>

## Identify

AntiX22-unix-de-in156

<hr>
