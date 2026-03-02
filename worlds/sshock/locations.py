from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import SystemShockWorld

LOCATION_NAME_TO_ID = {
    "Radiation Shield Switch": 0x6,
    "Laser Safety Interlock Switch": 0x7,
    "Laser Button": 0x8,
    "Delta Grove Safety Interlock Switch": 0xa,
    "Alpha Grove Safety Interlock Switch": 0xb,
    "Beta Grove Safety Interlock Switch": 0xc,
    "Relay 428 Repaired": 0xe,
    "Beta Grove Jettison Switch": 0xf,
    "Robot Charge Interrupt Button": 0x10,
    "Laser Safety Interlock Access Switch": 0x11,
    "Systems Authorization Code (Last 3 Digits)": 0x13,
    "Systems Authorization Code": 0x14,
    "\"Camera Activating Security Door\"": 0x1c,
    "Level 1 Switching Node": 0x1e,
    "\"Step right into my trap, little hacker!\"": 0x1f,
    "Level 5 Switching Node 1": 0x20,
    "\"You are not welcome here. Remove yourself.\"": 0x23,
    "Level 1 Respawns": 0x64,
    "Level 3 Respawns": 0x65,
    "Level 6 Respawns": 0x66,
    "Level 6 Switching Node 2": 0x75,
    "Level 4 Respawns": 0x92,
    "Level 5 Respawns": 0x93,
    "Antennas Destroyed": 0x99,
    "Level 6 Switching Node 1": 0xc0,
    "Level 5 Switching Node 2": 0xc3,
    "Systems Authorization Code (First 3 Digits)": 0xf0,
    "\"Welcome to my death machine!\"": 0xf3,
    "Level 2 Respawns": 0xf6,
    "Robot Access Panel Switch": 0xf7,
    "Robot Production Switch": 0xf9,
    "Level 7 Respawns": 0xfa,
    "Level R Switching Node 1": 0xfb,
    "Level R Switching Node 2": 0xfe,
    "Lift Puzzle": 0xfc,
    "Level R Respawns": 0x100,
    "Level 4 Force Bridge Switch": 0x10e,
    "Level R Security 0%": 0x210,
    "Level 1 Security 0%": 0x211,
    "Level 2 Security 0%": 0x212,
    "Level 3 Security 0%": 0x213,
    "Level 4 Security 0%": 0x214,
    "Level 5 Security 0%": 0x215,
    "Level 6 Security 0%": 0x216,
    "Level 7 Security 0%": 0x217,
    "Level 8 Security 0%": 0x218,
}

class SystemShockLocation(Location):
    game = "System Shock"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: SystemShockWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: SystemShockWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
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

    level1_locations = get_location_names_with_ids(
        ["Level 1 Respawns", "Level 1 Security 0%", "Lift Puzzle", "\"Camera Activating Security Door\"", "Level 1 Switching Node"]
    )
    level1.add_locations(level1_locations, SystemShockLocation)

    level2_locations = get_location_names_with_ids(
        ["Level 2 Respawns", "Level 2 Security 0%", "Laser Button", "Laser Safety Interlock Access Switch", "Robot Access Panel Switch", "Robot Production Switch"]
    )
    level2.add_locations(level2_locations, SystemShockLocation)

    level3_locations = get_location_names_with_ids(
        ["Level 3 Respawns", "Level 3 Security 0%", "Relay 428 Repaired"]
    )
    level3.add_locations(level3_locations, SystemShockLocation)

    level4_locations = get_location_names_with_ids(
        ["Level 4 Respawns", "Level 4 Security 0%", "Level 4 Force Bridge Switch"]
    )
    level4.add_locations(level4_locations, SystemShockLocation)

    level5_locations = get_location_names_with_ids(
        ["Level 5 Respawns", "Level 5 Security 0%", "\"Step right into my trap, little hacker!\"", "\"You are not welcome here. Remove yourself.\"", "Level 5 Switching Node 1", "Level 5 Switching Node 2"]
    )
    level5.add_locations(level5_locations, SystemShockLocation)

    level6_locations = get_location_names_with_ids(
        ["Level 6 Respawns", "Level 6 Security 0%", "Level 6 Switching Node 1", "Level 6 Switching Node 2", "Beta Grove Jettison Switch"]
    )
    level6.add_locations(level6_locations, SystemShockLocation)

    level7_locations = get_location_names_with_ids(
        ["Level 7 Respawns", "Level 7 Security 0%", "Antennas Destroyed"]
    )
    level7.add_locations(level7_locations, SystemShockLocation)

    level8_locations = get_location_names_with_ids(
        ["Level 8 Security 0%", "Robot Charge Interrupt Button"]
    )
    level8.add_locations(level8_locations, SystemShockLocation)

    levelR_locations = get_location_names_with_ids(
        ["Level R Respawns", "Level R Security 0%", "Radiation Shield Switch", "Laser Safety Interlock Switch", "\"Welcome to my death machine!\"", "Level R Switching Node 1", "Level R Switching Node 2", "Systems Authorization Code (First 3 Digits)", "Systems Authorization Code (Last 3 Digits)", "Systems Authorization Code"]
    )
    levelR.add_locations(levelR_locations, SystemShockLocation)

    levelG1_locations = get_location_names_with_ids(
        ["Alpha Grove Safety Interlock Switch"]
    )
    levelG1.add_locations(levelG1_locations, SystemShockLocation)

    levelG2_locations = get_location_names_with_ids(
        ["Beta Grove Safety Interlock Switch"]
    )
    levelG2.add_locations(levelG2_locations, SystemShockLocation)

    levelG4_locations = get_location_names_with_ids(
        ["Delta Grove Safety Interlock Switch"]
    )
    levelG4.add_locations(levelG4_locations, SystemShockLocation)


def create_events(world: SystemShockWorld) -> None:
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

    level9.add_event(
        "Final Stretch", "Finale", location_type=SystemShockLocation, item_type=items.SystemShockItem
    )
