## Introduction
- The simulation.py file contains Python code for simulating container Terminal operations. The simulation models the arrival, unloading, and transportation of containers, managing resources like berths, cranes, and trucks.
## Task Description
The simulation models the following terminal operations:
### Arrival of Vessels
- Vessels arrive based on an exponential distribution with a mean interval of 5 hours.
- Each vessel carries 150 containers that need to be unloaded.
### Berthing / Docking
- The terminal has two berths.
- Vessels will wait if both berths are occupied until a berth becomes available.
### Unloading Containers onto Trucks
- Two quay cranes are available, with each vessel using one crane for unloading.
- It takes 3 minutes for each crane to move one container from vessel to truck.
- Cranes will wait if no trucks are available for unloading.
### Transport Container
- The terminal has three trucks for moving containers from the quay cranes to the yard.
- Each truck takes 6 minutes to drop off a container and return.
### Simulation Logs
- Logs include timestamps for events such as vessel arrivals, berthing, crane operations, and truck operations.
## Requirements
- Python 3.x
- SimPy
# Code
  
## Classes and Methods
### `Class Port` : This class represents the container port and manages its resources.
- env: The simulation environment.
- num_berths: Number of berths available.
- num_cranes: Number of cranes available.
- num_trucks: Number of trucks available.
### Function `operate_crane(self, vessel_id, num_containers)` : 
- Operates a crane to unload containers from a vessel.
- vessel_id: Identifier for the vessel.
- num_containers: Number of containers to be unloaded.
### Function `unload_container(self, vessel_id, container_id)` : 
- Handles the unloading of a single container and requests a truck for transport.
- vessel_id: Identifier for the vessel.
- container_id: Identifier for the container.
### Function `transport_container(self, vessel_id, container_id)` : 
- Simulates transporting a container to the yard.
- vessel_id: Identifier for the vessel.
- container_id: Identifier for the container.
### Function `Process_Vessel(env, vessel_id, port)` : 
- Simulates the arrival and processing of a vessel at the port.
- env: The simulation environment.
- vessel_id: Identifier for the vessel.
- port: The port instance.
### Function `simulate_vessel_arrival(env, port)` : 
- Simulates the continuous arrival of vessels to the port.
- env: The simulation environment.
- port: The port instance.
### Function `start_simulation()`
Starts the entire simulation, prompting the user for simulation time and initializing the environment and port.
- Prompts the user to enter the simulation time in minutes.
- Initializes the simulation environment.
- Creates the port with specified resources.
- Starts the vessel arrival process.
- Runs the simulation for the specified time.

## To run the code
- Run the Command
  ```sh
  python Simulation.py
  ```
