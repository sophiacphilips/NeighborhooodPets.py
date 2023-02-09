#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 02/08/2023
#This code is designed to read a json file containing data about neighborhood pets. Once the file is read,
#the user can look up information about the pet's name, species, and owner. new pets can be logged into the library
#and pets can also be deleted.



class DuplicateNameError(Exception):
    pass
#raises exception if a pet with the name of a pet already in the data is added
import json
class NeighborhoodPets:
    """
    neighborhood pets class will initialize a library of pets that will be read from a json file
    """
    def __init__(self):
        """
        initializing list of pets that will be read from json file
        """
        self._list_of_pets = {}

    def add_pet(self, name, species, owner):
        """
        parameters set to add new pets, species info, and owner names to list of neighborhood pets
        """
        if name not in self._list_of_pets: #iterates through pets to determine if they're already in the library
            self._list_of_pets[name] = {"species": species, "owner": owner}
        elif name in self._list_of_pets: #if pet is already listed, exception is raised
            raise DuplicateNameError

    def delete_pet(self, name):
        """
        deletes pet from list_of_pets
        """
        if name in self._list_of_pets:
            del self._list_of_pets[name]

    def get_owner(self, name):
        """
        gets owner's name from list_of_pets
        """
        if name in self._list_of_pets:
            return self._list_of_pets[name]["owner"]

    def save_as_json(self, file_name):
        """
        saves the json file so it can be manipulated by user
        """
        with open(file_name, 'w') as outfile:
            json.dump(self._list_of_pets, outfile)

    def read_json(self):
        """
        reads and loads the json file so it can be used
        """
        with open() as infile:
            self._list_of_pets = json.load(infile)

    def get_all_species(self):
        """
        returns set of species of all pets
        """
        species_of_pet = set()
        for name in self._list_of_pets:
            species_of_pet.add(self._list_of_pets[name]['species'])
        return species_of_pet

