import pdb
from models.member import Member
from models.gym_class import GymClass
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
gym_class_repository.delete_all()
booking_repository.delete_all()

member_1 = Member("Peter", "La Fleur")
member_repository.save(member_1)

member_2 = Member("Patches", "OHoulihan")
member_repository.save(member_2)

member_3 = Member("White", "Goodman")
member_repository.save(member_3)

gym_class_1 = GymClass("Dodge, Duck, Dip, Dive and Dodge")
gym_class_repository.save(gym_class_1)
gym_class_2 = GymClass("Swimming for Beginners")
gym_class_repository.save(gym_class_2)
gym_class_3 = GymClass("Strength and Conditioning")
gym_class_repository.save(gym_class_3)

