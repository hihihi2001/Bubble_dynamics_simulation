# Bubble_dynamics_simulation
1. [**Python basics**](#Python basics): Feel free to skip this part. Helps with installations, briefly introduces some special python construct, and links tutorials. Important construct for this library: dictionaries, fstrings. NINCS KÉSZ!
2. [**The simulation**](#The simulation): Introduces some of the basic functions in *diffeq.py*. Shows, how to solve the differential equation with different control parameters. Shows how to plot, process, or save the results.
3. [**Bruteforce parameter sweep**](#Bruteforce parameter sweep): A simple multithread example. A control parameter space is sweeped with the given resolution. Results are saved into CSV files.

## Python basics
Feel free to skip this part.
### Dictionary
Dictionaries are data contaniers used to store different types of variables in an organised manner. Each member variable can be accesed via a key. It's similar to STL maps in c++. Basic usage:

~~~Python
# create a dictionary
datas = dict(
    data1=1,
    data2='one',
)

# add new element
datas['data3']=1.0

# remove element
datas.pop('data1')

# print dictionary
print(datas)

# iterate trought key
for key in datas:
    print(datas[key], end=' ')
    
# acces element
datas['data2']
~~~
~~~
{'data2': 'one', 'data3': 1.0}
one 1.0 
'one'
~~~
For easier syntax, you can use the dot notation to acces an element via this 4 lines of magic:
~~~Python
class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    
datas = dotdict(dict( data=1 ))
datas.data
~~~
~~~
1
~~~
This code is also included in *diffeq.py*. Other features of the dictionary is not affected. Most of my codes uses the dot notation. Note, that this makes the dictionaries a bit slower. Also, multiprocessing.Pool() doesn't like dotdicts.

## The simulation
Example file: *full bubble model (diffeq).ipynb* <br>
For import: *diffeq.py* <br>
The mathematical model is detailed in *full bubble model (diffeq).ipynb*. This is a notebook, where each function has a little demo, and all the formulas are attached in markdown cells. In most editors, you can navigate the file with the markdown headers. Note, that notebooks can not be imported in other codes, therefore all the code cells are copied to *diffeq.py*.  If you modify the notebook (.ipynb), make sure to copy the changes into the python file (.py).
### Parameters
EZ MEG FOG VÁLTOZNI AZ AUTOMATA BEOLVASÁSSAL!!! <br>
All the numerical constants and coefficents are stored in a seperate file. You can import this file and use it's variables:
~~~Python
import chemkin_AR_HE as par
par.R_g   # universal gas constant
~~~
~~~
8.31446
~~~
Make sure, you don't change the variables in par in the code! If you import diffeq as de, you can acces the parameters, as de.par .

### Control parameters
The control parameters are strored in a dictionary for easier managing. (Not in the high performance part) An example of souch a dictionary:
~~~Python
import diffeq as de

cpar = de.dotdict(dict(
    ID=0,
    R_E=3e-6, # [m]
    ratio=20.0, # [-]
    P_inf=50e5, # [Pa]
    alfa_M=0.05, # [-]
    T_inf=303.15, # [m]
    surfactant=0.25, # [-]
))
cpar.P_v = de.VapourPressure(cpar.T_inf) # [Pa]
~~~
This cpar will be passed to most of the not JITted functions. Don't forget, that cpar most contain an ID number, and all 7 control parameters, including the saturated vapour pressure, which is calculated from the temperature, otherwise not independent.

### Simulating
You should start with
~~~Python
import diffeq as de
~~~
The most important functions: <br>


* **plot(cpar, *t_int*, *n*, *base_name*)**: This funfction solves the differential equation, and plots it <br>
  Arguments:
  * cpar
  * t_int (optional): time interval, the default is [0, 1.0] seconds. Graphs will be plotted in this intervall, if you change it.
  * n (optional): how long should the plotted time interval be compared to the collapse time, default: 5 [-]
  * base_name (optional): save plots as .png, default: don't save. Use base_name='plot' --> plot_1.png, plot_2.png. Use base_name='images/plot' to save into images folder. Using a folder for images is recommended. This folder have to be created manually

  Returns: - <br>
  Example:
  ~~~Python
  de.plot(cpar)
  ~~~
  ~~~
  succecfully solved with LSODA solver
  ~~~
  ![image](https://user-images.githubusercontent.com/42745647/209476530-2d066b51-919c-4747-8969-af3763e5999c.png)
  ~~~
  Control parameters:
    	ID = 0
    	R_E = 3.00 [um]
    	ratio = 20.00 [-]
    	P_inf = 50.00 [bar]
    	alfa_M = 0.05 [-]
    	T_inf = 30.00 [°C]
    	P_v = 4245.13 [Pa]
    	surfactant = 0.25 [bar]
    Simulation info:
    	error_code = 0
    	elapsed_time = 1.77 [s]
    	steps = 14920 [-]
    Final state:
    	R_final = 3.07 [um];   R_dot_final =9.218886127073536e-18 [m/s];   T_final = 303.15 [K]
    	n_H2 =1.131533482140633e-14 [mol]; n_O2 =5.613844012476124e-15 [mol]
    	Final molar concentrations: [mol/cm^3]
        H: 1.0438444212257289e-24;  H_2: 9.300065864055777e-05;  O: 1.2342146154859568e-25;  O_2: 4.614014511333239e-05;  
        OH: 1.3657228605487174e-25;  H_2O: 1.6842204457213926e-06;  N_2: -6.557087373162561e-28;  HO_2: 3.850836132640751e-11;  
        H_2O_2: 7.203106513489704e-07;  Ar: 0.0018468099725707447;  He: 0.0;  OH_{ex}: -1.8351199382955463e-53;  
    Results:
          collapse_time = 8.007919977859432e-07 [s]
          T_max = 4104.54 [K]
          expansion work = 4.515209424703302e-06 [J]
          hydrogen production = 199517.27 [MJ/kg]
  ~~~
  
  
* **solve(cpar, *t_int*)**: This funfction solves the differential equation, and returns the numerical solution. Use, if you want to use the numerical solution itself. <br>
  Arguments:
  * cpar
  * t_int (optional): time interval, the default is [0, 1.0] seconds.

  Returns:
  * num_sol: an object containing the numerical solutions. Time is stored in array num_sol.t, the solution in array num_sol.y
  * error_code: a number from 0 to 4. If 3 or 4, the solver wasn't succesful.
  Example:
  ~~~Python
  num_sol, error_code, elapsed_time = de.solve(cpar)
  ~~~
  
  
* **get_data(cpar, num_sol, error_code, elapsed_time)**: This function gets the numerical solution and the control parameters, and returns some datas about the simulation. <br>
  Arguments:
  * cpar
  * num_sol: from solve()
  * error_code: from solve()
  * elapsed_time: from solve()

  Returns: A dictionary containing several inforamtions about the simulation, souch as the control parameters, error code, final results.
  Example:
  ~~~Python
  data = de.get_data(cpar, num_sol, error_code, elapsed_time)
  data
  ~~~
  ~~~
  {'ID': 0,
  'R_E': 3e-06,
  'ratio': 20.0,
  'P_inf': 5000000.0,
  'alfa_M': 0.05,
  'T_inf': 303.15,
  'P_v': 4245.12571625229,
  'surfactant': 0.25,
  'error_code': 0,
  'elapsed_time': 1.75,
  'steps': 14920,
  'collapse_time': 8.007919977859432e-07,
  'T_max': 4104.537031649485,
  'x_final': array([ 3.07395561e-06,  9.21888613e-18,  3.03150000e+02,  1.04384442e-24,
         9.30006586e-05,  1.23421462e-25,  4.61401451e-05,  1.36572286e-25,
         1.68422045e-06, -6.55708737e-28,  3.85083613e-11,  7.20310651e-07,
         1.84680997e-03,  0.00000000e+00, -1.83511994e-53]),
  'n_H2': 1.131533482140633e-14,
  'n_O2': 5.613844012476124e-15,
  'work': 4.515209424703302e-06,
  'energy': 199517.2699689556}
  ~~~
  
* **print_data(data)**: This function prints the data dictionary in an organised way. <br>
  Arguments:
  * data: from get_data()

  Returns: - <br>
  Example:
  ~~~Python
  de.print_data(data)
  ~~~
  ~~~
  Control parameters:
    	ID = 0
    	R_E = 3.00 [um]
    	ratio = 20.00 [-]
    	P_inf = 50.00 [bar]
    	alfa_M = 0.05 [-]
    	T_inf = 30.00 [°C]
    	P_v = 4245.13 [Pa]
    	surfactant = 0.25 [bar]
   Simulation info:
    	error_code = 0
    	elapsed_time = 1.80 [s]
    	steps = 14920 [-]
   Final state:
    	R_final = 3.07 [um];   R_dot_final =9.218886127073536e-18 [m/s];   T_final = 303.15 [K]
    	n_H2 =1.131533482140633e-14 [mol]; n_O2 =5.613844012476124e-15 [mol]
    	Final molar concentrations: [mol/cm^3]
        H: 1.0438444212257289e-24;  H_2: 9.300065864055777e-05;  O: 1.2342146154859568e-25;  O_2: 4.614014511333239e-05;  
        OH: 1.3657228605487174e-25;  H_2O: 1.6842204457213926e-06;  N_2: -6.557087373162561e-28;  HO_2: 3.850836132640751e-11;  
        H_2O_2: 7.203106513489704e-07;  Ar: 0.0018468099725707447;  He: 0.0;  OH_{ex}: -1.8351199382955463e-53;  
    Results:
    	collapse_time = 8.007919977859432e-07 [s]
    	T_max = 4104.54 [K]
    	expansion work = 4.515209424703302e-06 [J]
    	hydrogen production = 199517.27 [MJ/kg]
  ~~~
  
* **simulate(cpar, *t_int*)**: This function runs solve() and getData(), then returns with data. Both the input and the output is (or can be) a normal dictionary. This function is used in the bruteforce parameter sweep for multithreading. <br>
  Arguments:
  * cpar (normal dictionary, not dotdict)
  * t_int (optional): time interval, the default is [0, 1.0] seconds.

  Returns:
  * data: same, as in get_data(), but normal dictionary
  Example:
  ~~~Python
  data = de.simulate(cpar)
  ~~~
  
  
* **Make_dir**: class for saving things into CSV files. To use, first run:
~~~ Python
file = de.Make_dir('test')
~~~
This will create a folder called test, or use the existing one. Inside the folder, you can create a new, automatically numbered CSV file with a header:
~~~ Python
file.new_file()
~~~
The default name is *output_1.csv* with the number automatically incrementing itself. You can add a new line and store results:
~~~Python
data = de.simulate(cpar)
file.write_line(data)
~~~
You can close the CSV to save it:
~~~Python
file.close()
~~~
You can also save the numerical solution:
~~~Python
num_sol, error_code, elapsed_time = de.solve(cpar)
data = de.get_data(cpar, num_sol, error_code, elapsed_time)
file.write_solution(data, num_sol, 'testfile')
~~~
Two files will be created in the *test* folder. *testfile_data.csv* contains the data dictionary, while *testfile_num_sol.csv* contains the numerical solution. This function is independent of new_file() and close().


## Bruteforce parameter sweep
Example file: *bruteforce parameter sweep.ipynb* <br>
