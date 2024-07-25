import simpy
import random

class Port:
    def __init__(self, env, num_berths, num_cranes, num_trucks):
        #intializing the Port with default Values of Resources
        self.env = env
        self.berths = simpy.Resource(env, num_berths)
        self.cranes = simpy.Resource(env, num_cranes)
        self.trucks = simpy.Resource(env, num_trucks)

    def operate_crane(self, vessel_id, num_containers):
        crane_request = self.cranes.request() #Requesting for a Crane if Available
        yield crane_request
        for i in range(num_containers): #Simulating the unload_container for each Container
            yield self.env.process(self.unload_container(vessel_id, i + 1))
        self.cranes.release(crane_request) #Releasing the Crane after usage

    def unload_container(self, vessel_id, container_id):
        truck_request = self.trucks.request() #requesting for a truck from available resources
        if not truck_request.triggered:
            print(f"Vessel {vessel_id} - Crane waiting for a truck at Time : {self.env.now:.4f}")# Wait for a truck if not available
        yield truck_request  
        print(f"Vessel {vessel_id} - Crane loading container {container_id} at Time : {self.env.now:.4f}")
        yield self.env.timeout(3)  # Time to move container to truck
        self.env.process(self.transport_container(vessel_id, container_id)) #transport the container to yard after loading onto the truck
        self.trucks.release(truck_request) #releasing the truck resource after usage

    def transport_container(self, vessel_id, container_id): #method to simulate the time of transporting a container to yard
        print(f"Vessel {vessel_id} - Truck transporting container {container_id} to yard at Time : {self.env.now:.4f}")
        yield self.env.timeout(6)  # Time for truck to drop off container and return
        print(f"Vessel {vessel_id} - Truck returned from yard after transporting container {container_id} at Time : {self.env.now:.4f}")

def Process_Vessel(env, vessel_id, port): #Function to Simulate Vessel
    print(f"Vessel {vessel_id} - arrived to the port at Time : {env.now:.4f}")
    berth_request = port.berths.request() #Requesting for a empty berth from Resources
    if not berth_request.triggered:
        print(f"Vessel {vessel_id} - is waiting for a berth") #waiting until a berth is available
    yield berth_request  # Wait for berth if not available
    print(f"Vessel {vessel_id} - berthed at Time : {env.now:.4f}")
    yield env.process(port.operate_crane(vessel_id, 150)) #start operating on the vessel
    print(f"Vessel {vessel_id} - finished unloading and leaves the Port at Time : {env.now:.4f}")
    port.berths.release(berth_request) #releasing the resource for next vessel

def simulate_vessel_arrival(env, port):
    vessel_id = 0
    while True:
        yield env.timeout(random.expovariate(1 / 300))  # Time between vessel arrivals (average 5 hours)
        vessel_id += 1
        env.process(Process_Vessel(env, vessel_id, port)) #Simulating each Vessel

def start_simulation():
    # Taking input of simulation time from the user
    Sim_Time = int(input("Enter The Simulation Time (in minutes): "))
    Berths, Cranes, Trucks = 2, 2, 3  # default values for resources available

    # Check for any change in the resources
    # check = int(input("Enter 1 if changes are required in the Resources else 0: "))
    # if check == 1:
    #     # Taking input of No of Berths, Cranes and Trucks Available in Resources
    #     Berths = int(input("Enter no of Berths: "))
    #     Cranes = int(input("Enter no of Cranes: "))
    #     Trucks = int(input("Enter no of Trucks: "))

    # Initializing the simulation environment
    Env = simpy.Environment()

    # Creating the container port with specified berths, cranes, trucks
    port = Port(Env, Berths, Cranes, Trucks)

    # Starting the vessel arrival process
    Env.process(simulate_vessel_arrival(Env, port))

    # Running the simulation
    Env.run(until=Sim_Time)

start_simulation()
