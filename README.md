# Port Simulation

## Description
This Simulation.py file contains a python code for the simulation of container port operations, created as a part of Maersk Assesment.
The simulation uses SimPy to model the arrival, unloading, and transportation of containers at a port, managing resources such as berths, cranes, and trucks.

## Features
My Code implements the logic to
- Simulate the arrival of vessels at a port/Terminal.
- Manage the docking/berthing of vessels at a port.
- Manage the unloading of containers using cranes.
- Utilize trucks to transport containers to the yard.
- Model resource constraints and operational efficiency.

## Usage
To start the simulation, run the script and follow the prompts to enter the simulation time.
- python port_simulation.py

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
