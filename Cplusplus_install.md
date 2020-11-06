# Cplusplus hello world
## How to check if you already have C++ installed on your mac
1. Open the terminal an at the prompt type `g++`. If you then see an error similar to `clang: error: no input files` then you do have C++ installed

## How to install C++
1. Open the Safari browser and go to the Apple Developer site.
1. Click on Download Xcode to get the most recent version.
1. Click on the Free icon to change it to Install App (may take a while)

## Simple hello world
Create a document `myfile.cpp` as follows:

```
#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}
```
## Compile, Link and Run

1. To run your C++ code, you first have to _compile_ it to create an **object** file.

 ```
g++ -c hello_world.cpp
```
will compile `hello_world.cpp` to create an object file named `hello_world.o`.
2. Now you need to _link_ this object code with other libraries that are needed to create an _executable_ that you can **run**.
```
g++ -std=c++17 hello_world.o
```
will link the C++17 standard library and the object code `myfile.o` and create an _executable_ named `a.out`.
3. To run this _executable_ you type
 ```
 ./a.out
 ```

## Compile/Link/Rename/Run - in one line!

 ```
g++ -o hw hello_world.cpp
```
The above will compile and run the code and instead of creating an executable called a.out - which is the default - it will create an executable called `hw.o`. You can now run this executable.
 ```
./hw
```
## So what is different about C++?
For Python or Javascript you can try out commands on the command prompt, trying out one line of code at a time, and it will compile and run. In C++ you have to write the full code, then compile, link and run. This takes a very different mindset and approach to problem solving.


<sub>
**NOTE**
<sub>
Modern C++ compilers provide shortcuts that let's us create an executable without having to explicitly go through the linking process. g++ -std=c++17 filename.cpp will create the a.out directly. While it is OK to bypass explicit linking for small tests, keeping compile and link process separate helps you isolate and fix errors quickly. There are many use cases when by passing the linking actually will not work.
</sub>
