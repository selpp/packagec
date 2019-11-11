C Package: building a display library using the CSFML.

# C Package

## Build

In order to build the example file:
```bash
sudo apt install libcsfml-dev
git clone https://github.com/selpp/packagec
cd PackageC
make
```
In order to build the shared object library:
```bash
sudo apt install libcsfml-dev
git clone https://github.com/selpp/packagec
cd PackageC
make lib
```

## Usage

In order to run the example:
```bash
cd PackageC/build
./main
```

In order to use the shared object library:
```bash
make
make lib
BDL=./build/bdl.so python -m invader -r build/res
```
