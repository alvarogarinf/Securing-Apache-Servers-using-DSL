<h3 align="center">Securing Apache Servers using DSL</h3>

<br />
<div align="center">
  <p align="center">
    CLI Application created to improve the security of Apache servers using Domain-Specific Languages
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# About The Project

Final Degree Project of the Software Engineering Degree in the University of Oviedo.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
# Getting Started

This application works for Windows (Windows 11) and Linux (Ubuntu and CentOS). In case that
there is something that needs to be indicated for one OS or the other, it will be explained.
To get a local copy up and running follow these simple example steps.

## Prerequisites

In the Linux versions you will also need to install the package deep_translator, like this:
  ```sh
  pip install deep_translator
  ```
Python 3.7 installed

## Installation

Clone the repo
   ```sh
   git clone https://github.com/alvarogarinf/Securing-Apache-Servers-using-DSL.git
   ```
   
 Here we may distinct two different versions:
  ### Windows
  Double click on the main.exe application.
  
  ### Linux
  Use the following line of code
  ```sh
  sudo python main.py
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
# Usage

We are going to explain now the different functionalities of the application

## Using the DSL commands
The DSL commands are separated into sections. In order to use a command we will have to make:
```sh
  section_name command_name
  ```

This commands can be found on the files ComandosApacheWindows.json, ComandosApacheUbuntu.json and ComandosApacheCentOS.json.
After the execution of the command, it will show the executed command, the expected output of that given command and the execution of the command.


## Help
You could ask for help of all the commands with the order:
```sh
  help
  ```

You could also ask for help about a command with:
```sh
  help command_name
  ```
  
  
## Create new command
In case of wanting to define a new command with name command_name, write:
```sh
  create command_name
  ```


## Import a command
In case of wanting to import a command or a set of commands use the order:
```sh
  import from name_of_file name_of_command_1, name_of_command_2, ...
  ```

If the name of the command is not specified, all commands will be imported.


## Export a command
In case of wanting to export  a command or a set of commands use the order:
```sh
  export name_of_command_1, name_of_command_2, ... into name_of_file
  ```

If the name of the command is not specified, all commands will be imported.


## Change language
If you want to change the language write:
```sh
  set language LANGUAGE
  ```
LANGUAGE being the desired language (Only English and Spanish are available)



## User-friendly functionalities
1. Auto-fill of commands with the TAB key
2. History of command with the arrow keys and a local copy called history.txt
3. In case of mispelling an algorithm will tell you which option resembles most the given input

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
# License

Distributed under the Apache License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
# Contact

Álvaro García Infante

Project Link: [https://github.com/alvarogarinf/Securing-Apache-Servers-using-DSL](https://github.com/alvarogarinf/Securing-Apache-Servers-using-DSL)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
# Acknowledgments

* [CIS BENCHMARKS](https://www.cisecurity.org/)

<p align="right">(<a href="#top">back to top</a>)</p>
