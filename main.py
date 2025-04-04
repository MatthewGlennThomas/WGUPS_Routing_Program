#ALL CODE IS THE PROPERTY AND PRODUCT OF MATTHEW GLENN THOMAS
#ONLY SHARED FOR PROSPECTIVE EMPLOYERS, RECRUITERS, HR, AND OTHER APPLICABLE PERSONNEL'S VIEWING AND EVALUATION

#Developed hash table class to use as a data structure for holding package information
class HashTable:
    #__init__ is a constructor which sets up the table and size property when the object is created
    def __init__(self, size: int):
        self.table = [[] for _ in range(size)] #This creates a 2D array of the size we need
        self.size = size
    
    #This function creates the hash value of the indices we use for O(1) look up
    def hash(self, key: int) -> int:
        prime = 43 #Prime numbers help with the distribution of hash values (to minimize collisions)
        return (key * prime) % self.size
    
    #insert allows us to add data to the hash table
    def insert(self, package_id: int, delivery_address: str, delivery_deadline: str, delivery_city: str, delivery_zip_code: str, package_weight: int, delivery_status: str):
        idx = self.hash(package_id) #We need to place it at the hashed index rather than the id
        self.table[idx].append((package_id, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight, delivery_status))
    
    #This method is necessary to be able to update the information for each package
    def update(self, package_id: int, delivery_address: str, delivery_deadline: str, delivery_city: str, delivery_zip_code: str, package_weight: int, delivery_status: str):
        idx = self.hash(package_id)
        for i, pkg in enumerate(self.table[idx]):
            pkg_id, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight, _ = pkg
            if pkg_id == package_id: #Make sure it is the package we are looking for
                self.table[idx][i] = (pkg_id, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight, delivery_status)

    #look_up is how we get the packages' information from a hash table
    def look_up(self, package_id: int):
        idx = self.hash(package_id)
        #We need to iterate over every package retrieved at the index in case of collisions
        for pkg in self.table[idx]:
            pkg_id, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight, delivery_status = pkg
            #We're checking if the package at the index (pkg) has the correct package_id
            if pkg_id == package_id:
                return [delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight, delivery_status]
        return "no package" #We shouldn't ever see this, it will tell us nothing is found
    
    #A method to remove packages
    def remove(self, package_id: int):
        idx = self.hash(package_id)
        for i, pkg in enumerate(self.table[idx]): #We use i as well so we have a way to identify the delete
            pkg_id, _, _, _, _, _, _ = pkg #The underscores are used because we don't need those values
            if pkg_id == package_id:
                del self.table[idx][i]
    
    #Prints the state of all packages
    def display(self):
        string: str = "" #Assigning the string a value to allow concatenation
        for i in range(40): #Iterate over all 40 package ids
            string += "\n"+ str(i + 1) + " Address: " + self.look_up(i + 1)[0] + "\t" + "Deadline: " + self.look_up(i + 1)[1] + "\t" + "City: " + self.look_up(i + 1)[2] + "\t" + "Zip Code: " + self.look_up(i + 1)[3] + "\t" + "Weight: " + str(self.look_up(i + 1)[4]) + "\t" + "Status: " + self.look_up(i + 1)[5]
        print(string)

#Creating a hash table object using the HashTable class for package information
hash_table = HashTable(40)

#Inserting the information from the WGUPS Package File verbatim
hash_table.insert(1, "195 W Oakland Ave", "#######", "Salt Lake City", "84115 UT", 21, "At the hub")
hash_table.insert(2, "2530 S 500 E", "EOD", "Salt Lake City", "84106 UT", 44, "At the hub")
hash_table.insert(3, "233 Canyon Rd", "EOD", "Salt Lake City", "84103 UT", 2, "At the hub")
hash_table.insert(4, "380 W 2880 S", "EOD", "Salt Lake City", "84115 UT", 4, "At the hub")
hash_table.insert(5, "410 S State St", "EOD", "Salt Lake City", "84111 UT", 5, "At the hub")
hash_table.insert(6, "3060 Lester St", "#######", "West Valley City", "84119 UT", 88, "Delayed")
hash_table.insert(7, "1330 2100 S", "EOD", "Salt Lake City", "84106 UT", 8, "At the hub")
hash_table.insert(8, "300 State St", "EOD", "Salt Lake City", "84103 UT", 9, "At the hub")
hash_table.insert(9, "300 State St", "EOD", "Salt Lake City", "84103 UT", 2, "At the hub")
hash_table.insert(10, "600 E 900 South", "EOD", "Salt Lake City", "84105 UT", 1, "At the hub")
hash_table.insert(11, "2600 Taylorsville Blvd", "EOD", "Salt Lake City", "84118 UT", 1, "At the hub")
hash_table.insert(12, "3575 W Valley Central Station bus Loop", "EOD", "West Valley City", "84119 UT", 1, "At the hub")
hash_table.insert(13, "2010 W 500 S", "#######", "Salt Lake City", "84104 UT", 2, "At the hub")
hash_table.insert(14, "4300 S 1300 E", "#######", "Millcreek", "84117 UT", 88, "At the hub")
hash_table.insert(15, "4580 S 2300 E", "9:00 AM", "Holladay", "84117 UT", 4, "At the hub")
hash_table.insert(16, "4580 S 2300 E", "#######", "Holladay", "84117 UT", 88, "At the hub")
hash_table.insert(17, "3148 S 1100 W", "EOD", "Salt Lake City", "84119 UT", 2, "At the hub")
hash_table.insert(18, "1488 4800 S", "EOD", "Salt Lake City", "84123 UT", 6, "At the hub")
hash_table.insert(19, "177 W Price Ave", "EOD", "Salt Lake City", "84115 UT", 37, "At the hub")
hash_table.insert(20, "3595 Main St", "#######", "Salt Lake City", "84115 UT", 37, "At the hub")
hash_table.insert(21, "3595 Main St", "EOD", "Salt Lake City", "84115 UT", 3, "At the hub")
hash_table.insert(22, "6351 South 900 East", "EOD", "Murray", "84121 UT", 2, "At the hub")
hash_table.insert(23, "5100 South 2700 West", "EOD", "Salt Lake City", "84118 UT", 5, "At the hub")
hash_table.insert(24, "5025 State St", "EOD", "Murray", "84107 UT", 7, "At the hub")
hash_table.insert(25, "5383 South 900 East #104", "#######", "Salt Lake City", "84117 UT", 7, "Delayed")
hash_table.insert(26, "5383 South 900 East #104", "EOD", "Salt Lake City", "84117 UT", 25, "At the hub")
hash_table.insert(27, "1060 Dalton Ave S", "EOD", "Salt Lake City", "84104 UT", 5, "At the hub")
hash_table.insert(28, "2835 Main St", "EOD", "Salt Lake City", "84115 UT", 7, "Delayed")
hash_table.insert(29, "1330 2100 S", "#######", "Salt Lake City", "84106 UT", 2, "At the hub")
hash_table.insert(30, "300 State St", "#######", "Salt Lake City", "84103 UT", 1, "At the hub")
hash_table.insert(31, "3365 S 900 W", "#######", "Salt Lake City", "84119 UT", 1, "At the hub")
hash_table.insert(32, "3365 S 900 W", "EOD", "Salt Lake City", "84119 UT", 1, "Delayed")
hash_table.insert(33, "2530 S 500 E", "EOD", "Salt Lake City", "84106 UT", 1, "At the hub")
hash_table.insert(34, "4580 S 2300 E", "#######", "Holladay", "84117 UT", 2, "At the hub")
hash_table.insert(35, "1060 Dalton Ave S", "EOD", "Salt Lake City", "84104 UT", 88, "At the hub")
hash_table.insert(36, "2300 Parkway Blvd", "EOD", "West Valley City", "84119 UT", 88, "At the hub")
hash_table.insert(37, "410 S State St", "#######", "Salt Lake City", "84111 UT", 2, "At the hub")
hash_table.insert(38, "410 S State St", "EOD", "Salt Lake City", "84111 UT", 9, "At the hub")
hash_table.insert(39, "2010 W 500 S", "EOD", "Salt Lake City", "84104 UT", 9, "At the hub")
hash_table.insert(40, "380 W 2880 S", "#######", "Salt Lake City", "84115 UT", 45, "At the hub")

#Developed a two-key hash table class to use as a data structure for holding distance data
class TwoKeyTable:
    #__init__ sets up the two-key hash table and size property when the object is created
    def __init__(self, size: int):
        #Create a 2D array to hold the two-key hash table data
        self.table = [[] for _ in range(size)]
        self.size = size
    
    #This function creates the hash value of the indices we use for O(1) lookup
    def hash(self, key: str) -> int:
        prime = 43  #Prime numbers help with the distribution of hash values (to minimize collisions)
        return sum(ord(c) * prime for c in key) % self.size  #Hashing with character ASCII values' sum
    
    #insert allows us to add data to the two-key hash table
    def insert(self, primary_key: str, secondary_key: str, distance_data: float):
        idx = self.hash(primary_key) #Hash the primary key to find the index
        #Append the secondary_key and distance_data at the corresponding index
        self.table[idx].append([secondary_key, distance_data])
    
    #The method to retrieve distance data from the two-key hash table
    def look_up(self, primary_key: str, secondary_key: str):
        idx = self.hash(primary_key)  #Hash the primary key to find the index
        #We need to iterate over all the data retrieved at the index in case of collisions
        for loc in self.table[idx]:
            loc_key, distance_data = loc
            #We're checking if the distance data at the index (loc) has the correct secondary key (destination)
            if loc_key == secondary_key:
                return distance_data
        return "no distance data"

#Creating a two-key hash table object using the TwoKeyTable class for distance data
two_key_table = TwoKeyTable(729)

#List of all locations in the same order as the Excel table
locations = [
    "Western Governors University", #Hub
    "International Peace Gardens",
    "Sugar House Park",
    "Taylorsville-Bennion Heritage City Gov Off",
    "Salt Lake City Division of Health Services",
    "South Salt Lake Public Works",
    "Salt Lake City Streets and Sanitation",
    "Deker Lake",
    "Salt Lake City Ottinger Hall",
    "Columbus Library",
    "Taylorsville City Hall",
    "South Salt Lake Police",
    "Council Hall",
    "Redwood Park",
    "Salt Lake County Mental Health",
    "Salt Lake County/United Police Dept",
    "West Valley Prosecutor",
    "Housing Auth. of Salt Lake County",
    "Utah DMV Administrative Office",
    "Third District Juvenile Court",
    "Cottonwood Regional Softball Complex",
    "Holiday City Office",
    "Murray City Museum",
    "Valley Regional Softball Complex",
    "City Center of Rock Springs",
    "Rice Terrace Pavilion Park",
    "Wheeler Historic Farm"
]

#Complete 27x27 distance matrix matching the distance data in the Excel file verbatim
distances = [
    #Row 1: Western Governors University to all locations
    [0.0, 7.2, 3.8, 11.0, 2.2, 3.5, 10.9, 8.6, 7.6, 2.8, 6.4, 3.2, 7.6, 5.2, 4.4, 3.6, 7.6, 2.0, 3.6, 6.5, 1.9, 3.4, 2.4, 6.4, 2.4, 5.0, 3.6],
    #Row 2: International Peace Gardens to all locations
    [7.2, 0.0, 7.1, 6.4, 6.0, 4.8, 1.6, 2.8, 4.8, 6.3, 7.3, 5.3, 4.8, 3.0, 4.6, 4.5, 7.4, 6.0, 5.0, 4.8, 9.5, 10.9, 8.3, 6.9, 10.0, 4.4, 13.0],
    #Row 3: Sugar House Park to all locations
    [3.8, 7.1, 0.0, 9.2, 4.4, 2.8, 8.6, 6.3, 5.3, 1.6, 10.4, 3.0, 5.3, 6.5, 5.6, 5.8, 5.7, 4.1, 3.6, 4.3, 3.3, 5.0, 6.1, 9.7, 6.1, 2.8, 7.4],
    #Row 4: Taylorsville-Bennion Heritage City Gov Off to all locations
    [11.0, 6.4, 9.2, 0.0, 5.6, 6.9, 8.6, 4.0, 11.1, 7.3, 1.0, 6.4, 11.1, 3.9, 4.3, 4.4, 7.2, 5.3, 6.0, 10.6, 5.9, 7.4, 4.7, 0.6, 6.4, 10.1, 10.1],
    #Row 5: Salt Lake City Division of Health Services to all locations
    [2.2, 6.0, 4.4, 5.6, 0.0, 1.9, 7.9, 5.1, 7.5, 2.6, 6.5, 1.5, 7.5, 3.2, 2.4, 2.7, 1.4, 0.5, 1.7, 6.5, 3.2, 5.2, 2.5, 6.0, 4.2, 5.4, 5.5],
    #Row 6: South Salt Lake Public Works to all locations
    [3.5, 4.8, 2.8, 6.9, 1.9, 0.0, 6.3, 4.3, 4.5, 1.5, 8.7, 0.8, 4.5, 3.9, 3.0, 3.8, 5.7, 1.9, 1.1, 3.5, 4.9, 6.9, 4.2, 9.0, 5.9, 3.5, 7.2],
    #Row 7: Salt Lake City Streets and Sanitation to all locations
    [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0.0, 4.0, 4.2, 8.0, 8.6, 6.9, 4.2, 4.2, 8.0, 5.8, 7.2, 7.7, 6.6, 3.2, 11.2, 12.7, 10.0, 8.2, 11.7, 5.1, 14.2],
    #Row 8: Deker Lake to all locations
    [8.6, 2.8, 6.3, 4.0, 5.1, 4.3, 4.0, 0.0, 7.7, 9.3, 4.6, 4.8, 7.7, 1.6, 3.3, 3.4, 3.1, 5.1, 4.6, 6.7, 8.1, 10.4, 7.8, 4.2, 9.5, 6.2, 10.7],
    #Row 9: Salt Lake City Ottinger Hall to all locations
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.0, 4.8, 11.9, 4.7, 0.6, 7.6, 7.8, 6.6, 7.2, 5.9, 5.4, 1.0, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1],
    #Row 10: Columbus Library to all locations
    [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8.0, 9.3, 4.8, 0.0, 9.4, 1.1, 5.1, 4.6, 3.7, 4.0, 6.7, 2.3, 1.8, 4.1, 3.8, 5.8, 4.3, 7.8, 4.8, 3.2, 6.0],
    #Row 11: Taylorsville City Hall to all locations
    [6.4, 7.3, 10.4, 1.0, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0.0, 7.3, 12.0, 4.9, 5.2, 5.4, 8.1, 6.2, 6.9, 11.5, 6.9, 8.3, 4.1, 0.4, 4.9, 11.0, 6.8],
    #Row 12: South Salt Lake Police to all locations
    [3.2, 5.3, 3.0, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0.0, 4.7, 3.5, 2.6, 2.9, 6.3, 1.2, 1.0, 3.7, 4.1, 6.2, 3.4, 6.9, 5.2, 3.7, 6.4],
    #Row 13: Council Hall to all locations
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12.0, 4.7, 0.0, 7.3, 7.8, 6.6, 7.2, 5.9, 5.4, 1.0, 8.5, 10.3, 7.8, 11.5, 9.5, 2.8, 14.1],
    #Row 14: Redwood Park to all locations
    [5.2, 3.0, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0.0, 1.3, 1.5, 4.0, 3.2, 3.0, 6.9, 6.2, 8.2, 5.5, 4.4, 7.2, 6.4, 10.5],
    #Row 15: Salt Lake County Mental Health to all locations
    [4.4, 4.6, 5.6, 4.3, 2.4, 3.0, 8.0, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0.0, 0.6, 6.4, 2.4, 2.2, 6.8, 5.3, 7.4, 4.6, 4.8, 6.3, 6.5, 8.8],
    #Row 16: Salt Lake County/United Police Dept to all locations
    [3.6, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4.0, 5.4, 2.9, 6.6, 1.5, 0.6, 0.0, 5.6, 1.6, 1.7, 6.4, 4.9, 6.9, 4.2, 5.6, 5.9, 5.7, 8.4],
    #Row 17: West Valley Prosecutor to all locations
    [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4.0, 6.4, 5.6, 0.0, 7.1, 6.1, 7.2, 10.6, 12.0, 9.4, 7.5, 11.1, 6.2, 13.6],
    #Row 18: Housing Auth. of Salt Lake County to all locations
    [2.0, 6.0, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0.0, 1.6, 4.9, 3.0, 5.0, 2.3, 5.5, 4.0, 5.1, 5.2],
    #Row 19: Utah DMV Administrative Office to all locations
    [3.6, 5.0, 3.6, 6.0, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1.0, 5.4, 3.0, 2.2, 1.7, 6.1, 1.6, 0.0, 4.4, 4.6, 6.6, 3.9, 6.5, 5.6, 4.3, 6.9],
    #Row 20: Third District Juvenile Court to all locations
    [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1.0, 4.1, 11.5, 3.7, 1.0, 6.9, 6.8, 6.4, 7.2, 4.9, 4.4, 0.0, 7.5, 9.3, 6.8, 11.4, 8.5, 1.8, 13.1],
    #Row 21: Cottonwood Regional Softball Complex to all locations
    [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3.0, 4.6, 7.5, 0.0, 2.0, 2.9, 6.4, 2.8, 6.0, 4.1],
    #Row 22: Holiday City Office to all locations
    [3.4, 10.9, 5.0, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12.0, 5.0, 6.6, 9.3, 2.0, 0.0, 4.4, 7.9, 3.4, 7.9, 4.7],
    #Row 23: Murray City Museum to all locations
    [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10.0, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4, 0.0, 4.5, 1.7, 6.8, 3.1],
    #Row 24: Valley Regional Softball Complex to all locations
    [6.4, 6.9, 9.7, 0.6, 6.0, 9.0, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9, 4.5, 0.0, 5.4, 10.6, 7.8],
    #Row 25: City Center of Rock Springs to all locations
    [2.4, 10.0, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4.0, 5.6, 8.5, 2.8, 3.4, 1.7, 5.4, 0.0, 7.0, 1.3],
    #Row 26: Rice Terrace Pavilion Park to all locations
    [5.0, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11.0, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6.0, 7.9, 6.8, 10.6, 7.0, 0.0, 8.3],
    #Row 27: Wheeler Historic Farm to all locations
    [3.6, 13.0, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6.0, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1, 4.7, 3.1, 7.8, 1.3, 8.3, 0.0]
]

#Insert all distances into the TwoKeyTable
for i in range(len(locations)):
    for j in range(len(locations)):
        loc1 = locations[i]
        loc2 = locations[j]
        two_key_table.insert(loc1, loc2, distances[i][j])

#Function that translates the raw address to its name for the TwoKeyTable to use
def translate_address(address: str) -> str:
    match address:
        case "4001 South 700 East" | "Hub": #Included a shorthand because the address isn't used
            return "Western Governors University"
        case "1060 Dalton Ave S":
            return "International Peace Gardens"
        case "1330 2100 S":
            return "Sugar House Park"
        case "1488 4800 S":
            return "Taylorsville-Bennion Heritage City Gov Off"
        case "177 W Price Ave":
            return "Salt Lake City Division of Health Services"
        case "195 W Oakland Ave":
            return "South Salt Lake Public Works"
        case "2010 W 500 S":
            return "Salt Lake City Streets and Sanitation"
        case "2300 Parkway Blvd":
            return "Deker Lake"
        case "233 Canyon Rd":
            return "Salt Lake City Ottinger Hall"
        case "2530 S 500 E":
            return "Columbus Library"
        case "2600 Taylorsville Blvd":
            return "Taylorsville City Hall"
        case "2835 Main St":
            return "South Salt Lake Police"
        case "300 State St":
            return "Council Hall"
        case "3060 Lester St":
            return "Redwood Park"
        case "3148 S 1100 W":
            return "Salt Lake County Mental Health"
        case "3365 S 900 W":
            return "Salt Lake County/United Police Dept"
        case "3575 W Valley Central Station bus Loop":
            return "West Valley Prosecutor"
        case "3595 Main St":
            return "Housing Auth. of Salt Lake County"
        case "380 W 2880 S":
            return "Utah DMV Administrative Office"
        case "410 S State St":
            return "Third District Juvenile Court"
        case "4300 S 1300 E":
            return "Cottonwood Regional Softball Complex"
        case "4580 S 2300 E":
            return "Holiday City Office"
        case "5025 State St":
            return "Murray City Museum"
        case "5100 South 2700 West":
            return "Valley Regional Softball Complex"
        case "5383 South 900 East #104":
            return "City Center of Rock Springs"
        case "600 E 900 South":
            return "Rice Terrace Pavilion Park"
        case "6351 South 900 East":
            return "Wheeler Historic Farm"

#Function that translates addresses to their names and gets distance data
def get_distance(address_one: str, address_two: str) -> float:
    return two_key_table.look_up(translate_address(address_one), translate_address(address_two))

#Class blueprint of the trucks that deliver packages
class Truck:
    def __init__(self, size: int, name: str):
        self.inventory = HashTable(size)
        self.name = name
        self.numbers = [] #Keeping track of package ids is good for sorted lists
        self.location = "Hub" #All trucks start at the hub so it is the default
        self.truck_status: str = "At the hub" #All trucks start at the hub
        self.mins = 0 #Each truck tracks its own time offset in minutes
        self.distance = 0 #Total distance traveled by the truck
        self.stopped = False #A truck starts out able to deliver

    #Add a package to the truck's inventory
    def add(self, pkg_id: int):
        pkg_info = hash_table.look_up(pkg_id)
        self.inventory.insert(pkg_id, pkg_info[0], pkg_info[1], pkg_info[2], pkg_info[3], pkg_info[4], pkg_info[5])
        self.numbers.append(pkg_id)
    
    #A method to remove packages from the truck utilizing the hash table's remove method
    def remove(self, pkg_id: int):
        self.inventory.remove(pkg_id)
        self.numbers.remove(pkg_id)

    #Leverages HashTable's update method to update the address for a package
    def update_address(self, package_id: int, address: str):
        info = self.inventory.look_up(package_id)
        self.inventory.update(package_id, address, info[1], info[2], info[3], info[4], info[5])

    #Leverages HashTable's update method to update the zip_code for a package
    def update_zip_code(self, package_id: int, zip_code: str):
        info = self.inventory.look_up(package_id)
        self.inventory.update(package_id, info[0], info[1], info[2], zip_code, info[4], info[5])

    #Leverages HashTable's update method to update the status of a package
    def update_status(self, package_id: int, status: str):
        info = self.inventory.look_up(package_id)
        self.inventory.update(package_id, info[0], info[1], info[2], info[3], info[4], status)

    #Sets the current location of the truck for reference
    def set_location(self, location: str):
        self.location = location

    #Set the truck's time offset in minutes
    def set_mins(self, minutes):
        self.mins = minutes

    #Allows accumulation of total distance travelled with every stop
    def set_distance(self, distance):
        self.distance = distance

    #Allows setting of the stopped property. Important for the Algorithm
    def set_stopped(self, is_it: bool):
        self.stopped = is_it
    
    #Allows the name of the object to be called for strings
    def get_name(self):
        return self.name

    #Retrieves the inventory of a truck
    def get_inventory(self):
        return self.inventory

    #Retrieves the numbers list from a truck object
    def get_numbers(self) -> list:
        return self.numbers

    #Returns the current location of the truck
    def get_location(self):
        return self.location

    #Retrieves the current time offset relative to the truck in minutes
    def get_mins(self):
        return self.mins

    #Returns the total distance the truck has traveled
    def get_distance(self):
        return self.distance

    #Tells you whether the truck is delivering
    def get_stopped(self) -> bool:
        return self.stopped

    #Prints the truck's whole inventory of packages
    def display(self):
        string = ""
        numlist = []
        numlist = sorted(self.numbers)
        if len(numlist) > 0: #Check if numlist is empty before utilizing it
            string += self.inventory.look_up(numlist[0])[0] + " " + self.inventory.look_up(numlist[0])[1] + " " + self.inventory.look_up(numlist[0])[2] + " " + self.inventory.look_up(numlist[0])[3] + " " + str(self.inventory.look_up(numlist[0])[4]) + " " + self.inventory.look_up(numlist[0])[5]
        if len(numlist) > 1: #Check if there are more elements to iterate over and remove the already used one
            numlist.remove(numlist[0])
            for i in numlist:
                string += "\n" + self.inventory.look_up(i)[0] + " " + self.inventory.look_up(i)[1] + " " + self.inventory.look_up(i)[2] + " " + self.inventory.look_up(i)[3] + " " + str(self.inventory.look_up(i)[4]) + " " + self.inventory.look_up(i)[5]
        print("Truck Inventory:")
        print(string)

#Loading truck one respecting package loading conditions (some packages must go on truck two)
truck_one = Truck(16, "Truck One")
for i in range(2):
    truck_one.add(i + 1)
for i in range(2):
    truck_one.add(i + 4)
for i in range(2):
    truck_one.add(i + 7)
for i in range(8):
    truck_one.add(i + 10)
for i in range(2):
    truck_one.add(i + 19)

#Loading truck two including the packages it must have (also keeping max inventory in mind)
truck_two = Truck(16, "Truck Two")
truck_two.add(3)
truck_two.add(18)
for i in range (4):
    truck_two.add(i + 21)
for i in range(2):
    truck_two.add(i + 26)
for i in range(3):
    truck_two.add(i + 29)
for i in range(4):
    truck_two.add(i + 33)
truck_two.add(38)

#Loading truck three, a driver comes back for this one to accomodate delayed packages
truck_three = Truck(8, "Truck Three")
truck_three.add(6)
truck_three.add(25)
truck_three.add(28)
truck_three.add(32)
truck_three.add(37)
for i in range(2):
    truck_three.add(i + 39)
truck_three.add(9) #This package cannot be delivered before address is updated
truck_three.set_stopped(True) #Truck three needs to wait for truck one

#Converts distance into time in minutes
def dist_minutes(distance: float) -> float:
    return distance * (60.0 / 18.0)

#Converts a float of minutes into time in the normal format
def real_time(minutes: float) -> str:
    hours = int(minutes / 60)
    minutes -= hours * 60
    segment1 = ""
    segment2 = ":"
    segment3 = ""
    segment4 = " am"
    if hours > 12:
        hours -= 12
        segment4 = " pm"
    segment1 = str(hours)
    if round(minutes) < 10:
        segment3 = "0" + str(int(round(minutes)))
    else:
        segment3 = str(int(round(minutes)))
    return segment1 + segment2 + segment3 + segment4

#The same as real_time() but adds a zero to single-digit hours
def real_time_zerod(minutes: float) -> str:
    hours = int(minutes / 60)
    minutes -= hours * 60
    segment1 = ""
    segment2 = ":"
    segment3 = ""
    segment4 = " am" #Constructing the desired time format by segments
    if hours > 12:
        hours -= 12
        segment4 = " pm"
    if hours < 10:
        segment1 = "0" + str(hours)
    else:
        segment1 = str(hours)
    if round(minutes) < 10:
        segment3 = "0" + str(int(round(minutes)))
    else:
        segment3 = str(int(round(minutes)))
    return segment1 + segment2 + segment3 + segment4

#lists declared for use in the delivery algorithm
time_critical: list = []
delivered = []

#Sorting package priority for the algorithm
for i in range(40):
    info = hash_table.look_up(i + 1)
    if ":" in info[1]: #This works because only time critical packages have a time
        time_critical.append(i + 1)

#A function simulating the arrival of the delayed packages
def flight_arrives():
    for i in range(40):
        info = hash_table.look_up(i + 1)
        if info[5] == "Delayed":
            hash_table.update(i + 1, info[0], info[1], info[2], info[3], info[4], "At the hub")
            if i + 1 in truck_one.get_numbers():
                truck_one.update_status(i + 1, "At the hub")
            if i + 1 in truck_two.get_numbers():
                truck_two.update_status(i + 1, "At the hub")
            if i + 1 in truck_three.get_numbers():
                truck_three.update_status(i + 1, "At the hub")

#A function simulating WGUPS receiving and updating package 9's corrected address
def address_corrected():
    for i in range(40):
        info = hash_table.look_up(i + 1)
        hash_table.update(i + 1, "410 S State St", info[1], info[2], "84111 UT", info[4], info[5])
        if i + 1 in truck_one.get_numbers():
            truck_one.update_address(i + 1, "410 S State St")
            truck_one.update_zip_code(i + 1, "84111 UT")
        if i + 1 in truck_two.get_numbers():
            truck_two.update_address(i + 1, "410 S State St")
            truck_two.update_zip_code(i + 1, "84111 UT")
        if i + 1 in truck_three.get_numbers():
            truck_three.update_address(i + 1, "410 S State St")
            truck_three.update_zip_code(i + 1, "84111 UT")

start_mins = 480 #8:00 am in minutes since midnight
#stop_mins represents the time the simulation should stop at
stop_mins = 1439 #By default, the simulation runs all day or until completion

num: int = 0
print("Please keep times no earlier than 8:00 am and no later than 11:59 pm")
user_string = input("Please enter a time in (HH:MM am/pm) format:")# Get User Input
counter = 0
if not ":" in user_string: #Compensate for common spelling error
    counter = 1
if user_string == "EOD" or user_string == "eod": #Convenient shorthand option
    user_string = 1439
else: #Made sure to use a tolerant approach to input (case insensitive etcetera)
    if user_string[len(user_string) - 2] == "p" or user_string[len(user_string) - 2] == "P": #Identify if it is a pm value, this approach is tolerant of end omissions
        num = 720
    if user_string[0] == "0": #Adapt to the zerod format as necessary
        user_string = int(user_string[1]) * 60 + int(user_string[3 - counter] + user_string[4 - counter])
    elif len(user_string) == 8:
        user_string = int(user_string[0] + user_string[1]) * 60 + int(user_string[3 - counter] + user_string[4 - counter])
    else:
        user_string = int(user_string[0]) * 60 + int(user_string[2 - counter] + user_string[3 - counter])
stop_mins = user_string + num

#*** NEAREST NEIGHBOR ALGORITHM IS IN next_delivery() ***

#Contains the logic for a truck to deliver its next package
def next_delivery(truck: Truck, start_time, stop_time):
    candidates = sorted(truck.get_numbers()) #The algorithm considers these
    valid_candidates = []
    for candidate in candidates:
        if candidate not in delivered: #We don't want to redeliver packages
            valid_candidates.append(candidate)
        elif candidate in time_critical:
            valid_candidates = [candidate] #Give time critical packages priority
    if not valid_candidates:
        if start_time + truck.get_mins() + dist_minutes(get_distance(truck.get_location(), "Hub")) < stop_time:
            truck.set_mins(truck.get_mins() + dist_minutes(get_distance(truck.get_location(), "Hub")))
            truck.set_location("Hub") #We need to update trucks' locations to the destinations to simulate movement
            truck.set_distance(truck.get_distance() + get_distance(truck.get_location(), "Hub"))
            truck.set_stopped(True)
        else:
            truck.set_stopped(True)
    next_package: int
    next_distance = 1000 #Set arbitrarily high by default so it can be replaced
    destination: str
    for candidate in valid_candidates:
        info = hash_table.look_up(candidate)
        if get_distance(truck.get_location(), info[0]) < next_distance: #NEAREST NEIGHBOR LINE
            next_package = candidate #Information is replaced as better candidates are found during iteration
            next_distance = get_distance(truck.get_location(), info[0])
            destination = info[0]
    if start_time + truck.get_mins() + dist_minutes(next_distance) < stop_time:
        truck.set_mins(truck.get_mins() + dist_minutes(next_distance))
        new_status = "Delivered at " + real_time(start_time + truck.get_mins())
        truck.update_status(next_package, new_status)
        info = hash_table.look_up(next_package) #We need to look up to get all the information for full updates
        hash_table.update(next_package, info[0], info[1], info[2], info[3], info[4], new_status)
        truck.set_location(destination)
        truck.set_distance(truck.get_distance() + next_distance)
        delivered.append(next_package)
        truck.remove(next_package)
    else:
        truck.set_stopped(True)

#The function runs the simulation until the specified time
def simulate_until(stop_time: int):
    while truck_one.get_stopped() == False:
        next_delivery(truck_one, start_mins, stop_time)
        if truck_one.get_stopped() == False: #If still going pause three
            group = truck_one.get_numbers()
            for i in group: #Setting the status of packages to en route
                truck_one.update_status(i, "En route in " + truck_one.get_name())
                info = hash_table.look_up(i)
                hash_table.update(i, info[0], info[1], info[2], info[3], info[4], "En route in " + truck_one.get_name())
            truck_three.set_stopped(True)
    if not truck_one.get_numbers():
        truck_three.set_stopped(False)
    while truck_two.get_stopped() == False:
        next_delivery(truck_two, (start_mins + 65), stop_time) #Starts at 9:05am
        if truck_two.get_stopped() == False: #If still going pause three
            group = truck_two.get_numbers()
            for i in group: #Setting the status of packages to en route
                truck_two.update_status(i, "En route in " + truck_two.get_name())
                info = hash_table.look_up(i)
                hash_table.update(i, info[0], info[1], info[2], info[3], info[4], "En route in " + truck_two.get_name())
    while truck_three.get_stopped() == False:
        next_delivery(truck_three, start_mins + 143, stop_time) #Start after truck_one
        if truck_three.get_stopped() == False:
            group = truck_three.get_numbers()
            for i in group: #Setting the status of packages to en route
                truck_three.update_status(i, "En route in " + truck_three.get_name())
                info = hash_table.look_up(i)
                hash_table.update(i, info[0], info[1], info[2], info[3], info[4], "En route in " + truck_three.get_name())

#Need to properly make the trucks start delivering again after hitting stop times
def reset_trucks():
    if truck_one.get_numbers() or truck_one.get_location() != "Hub":
        truck_one.set_stopped(False)
    if truck_two.get_numbers() or truck_two.get_location() != "Hub":
        truck_two.set_stopped(False)
    if truck_three.get_numbers() or truck_three.get_location() != "Hub":
        truck_three.set_stopped(False)

#Simulation branching to make sure events are considered
if stop_mins > 620: #Calculating with the effects of flight delay and wrong address
    simulate_until(545)
    flight_arrives() #The flight carrying several delayed packages arrives
    reset_trucks()
    simulate_until(620)
    address_corrected() #WGUPS corrects package 9's address
    reset_trucks()
    simulate_until(stop_mins) #Finish running simulation after events
elif stop_mins > 545: #Calculating with the flight delay's effect
    simulate_until(545)
    flight_arrives() #The flight brings delayed packages to the hub
    reset_trucks()
    simulate_until(stop_mins)
else:
    simulate_until(stop_mins)

#*** The algorithm is mainly comprised of the functions next_delivery() through simulate_until() directly above ***

#Accumulating all distances traveled by the three trucks
total_distance = round(truck_one.get_distance() + truck_two.get_distance() + truck_three.get_distance(), 2)

#Displaying all relevant distance information
print("\nTOTAL DISTANCE TRAVELED: " + str(total_distance) + " miles")
print("TRUCK ONE TRAVELED: " + str(round(truck_one.get_distance(), 2)) + " miles")
print("TRUCK TWO TRAVELED: " + str(round(truck_two.get_distance(), 2)) + " miles")
print("TRUCK THREE TRAVELED: " + str(round(truck_three.get_distance(), 2)) + " miles")

#Displaying the state of packages as of the time entered as input
print("\n------ STATE OF PACKAGES AS OF " + real_time(stop_mins) + " ------")
hash_table.display()

#ALL CODE IS THE PROPERTY AND PRODUCT OF MATTHEW GLENN THOMAS
#ONLY SHARED FOR PROSPECTIVE EMPLOYERS, RECRUITERS, HR, AND OTHER APPLICABLE PERSONNEL'S VIEWING AND EVALUATION