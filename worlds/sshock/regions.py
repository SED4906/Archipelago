from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SystemShockWorld

def create_and_connect_regions(world: SystemShockWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: SystemShockWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    level1 = Region("Medical", world.player, world.multiworld)
    level2 = Region("Research", world.player, world.multiworld)
    level3 = Region("Maintenance", world.player, world.multiworld)
    level4 = Region("Storage", world.player, world.multiworld)
    level5 = Region("Flight Deck", world.player, world.multiworld)
    level6 = Region("Executive", world.player, world.multiworld)
    level7 = Region("Engineering", world.player, world.multiworld)
    level8 = Region("Security", world.player, world.multiworld)
    level9 = Region("Bridge", world.player, world.multiworld)
    levelG1 = Region("Alpha Grove", world.player, world.multiworld)
    levelG2 = Region("Beta Grove", world.player, world.multiworld)
    levelG4 = Region("Delta Grove", world.player, world.multiworld)
    levelR = Region("Reactor", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [level1, level2, level3, level4, level5, level6, level7, level8, level9, levelG1, levelG2, levelG4, levelR]

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions

def connect_regions(world: SystemShockWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    level1 = world.get_region("Medical")
    level2 = world.get_region("Research")
    level3 = world.get_region("Maintenance")
    level4 = world.get_region("Storage")
    level5 = world.get_region("Flight Deck")
    level6 = world.get_region("Executive")
    level7 = world.get_region("Engineering")
    level8 = world.get_region("Security")
    level9 = world.get_region("Bridge")
    levelG1 = world.get_region("Alpha Grove")
    levelG2 = world.get_region("Beta Grove")
    levelG4 = world.get_region("Delta Grove")
    levelR = world.get_region("Reactor")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    level1.connect(level2, "Elevator 1 to 2")
    level2.connect(levelR, "Elevator 2 to R")
    levelR.connect(level2, "Elevator R to 2")
    level2.connect(level3, "Elevator 2 to 3")
    level3.connect(level3, "Elevator 3 to 2")
    level3.connect(level4, "Elevator 3 to 4")
    level3.connect(level5, "Elevator 3 to 5")
    level3.connect(level6, "Elevator 3 to 6", lambda state: state.has("Laser Destroyed", world.player))
    level4.connect(level3, "Elevator 4 to 3")
    level4.connect(level5, "Elevator 4 to 5")
    level5.connect(level3, "Elevator 5 to 3")
    level5.connect(level4, "Elevator 5 to 4")
    level5.connect(level6, "Elevator 5 to 6", lambda state: state.has("Laser Destroyed", world.player))
    level6.connect(level3, "Elevator 6 to 3")
    level6.connect(level5, "Elevator 6 to 5")
    level6.connect(level7, "Elevator 6 to 7", lambda state: state.has("Beta Grove Jettisoned", world.player))
    level6.connect(levelG1, "Elevator 6 to G1")
    level6.connect(levelG2, "Elevator 6 to G2", lambda state: state.has("Beta Grove Elevator", world.player))
    level6.connect(levelG4, "Elevator 6 to G4")
    level7.connect(level6, "Elevator 7 to 6")
    level7.connect(level8, "Elevator 7 to 8", lambda state: state.has("Level 8 Access", world.player))
    level8.connect(level9, "Elevator 8 to 9", lambda state: state.has("Reactor Auto-Destruct Activated", world.player)) # One way, once you reach here you're on your own. Should probably just make reaching this the win condition.
    levelG1.connect(level6, "Elevator G1 to 6")
    levelG2.connect(level6, "Elevator G2 to 6")
    levelG4.connect(level6, "Elevator G4 to 6")
