from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import SystemShockWorld

ITEM_NAME_TO_ID = {
    "Staminup": 1000,
    "Sight Patch": 1001,
    "B'serk": 1002,
    "Medipatch": 1003,
    "Reflex Patch": 1004,
    "Genius Patch": 1005,
    "Detox": 1006,
    "Radiation Shield Active": 0x6,
    "Laser Safety Interlock Disabled": 0x7,
    "Laser Destroyed": 0x8,
    "Delta Grove Safety Interlock Disabled": 0xa,
    "Alpha Grove Safety Interlock Disabled": 0xb,
    "Beta Grove Safety Interlock Disabled": 0xc,
    "Beta Grove Jettisoned": 0xf,
    "Robot Charge Interrupt": 0x10,
    "Laser Safety Interlock Access": 0x11,
    "Reactor Auto-Destruct Activated": 0x14,
    "Medical Armory": 0x1e,
    "Flight Bay 3": 0x20,
    "Beta Grove Elevator": 0x75,
    "Level 8 Access": 0x99,
    "Edward Diego's Storage Closet": 0xc0,
    "Flight Bay Armory": 0xc3,
    "Robot Access Panel Unlocked": 0xf7,
    "Robot Production Deactivated": 0xf9,
    "Blast Door": 0xfb,
    "Puzzle Lift": 0xfc,
    "Armory": 0xfe,
    "Level 4 Force Bridge": 0x10e,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Staminup": ItemClassification.filler,
    "Sight Patch": ItemClassification.filler,
    "B'serk": ItemClassification.filler,
    "Medipatch": ItemClassification.filler,
    "Reflex Patch": ItemClassification.filler,
    "Genius Patch": ItemClassification.filler,
    "Detox": ItemClassification.filler,
    "Radiation Shield Active": ItemClassification.progression,
    "Laser Safety Interlock Disabled": ItemClassification.progression,
    "Laser Destroyed": ItemClassification.progression,
    "Delta Grove Safety Interlock Disabled": ItemClassification.progression,
    "Alpha Grove Safety Interlock Disabled": ItemClassification.progression,
    "Beta Grove Safety Interlock Disabled": ItemClassification.progression,
    "Beta Grove Jettisoned": ItemClassification.progression,
    "Robot Charge Interrupt": ItemClassification.useful,
    "Laser Safety Interlock Access": ItemClassification.progression,
    "Reactor Auto-Destruct Activated": ItemClassification.progression,
    "Medical Armory": ItemClassification.useful,
    "Flight Bay 3": ItemClassification.useful,
    "Beta Grove Elevator": ItemClassification.progression,
    "Level 8 Access": ItemClassification.progression,
    "Edward Diego's Storage Closet": ItemClassification.useful,
    "Flight Bay Armory": ItemClassification.useful,
    "Robot Access Panel Unlocked": ItemClassification.progression | ItemClassification.useful,
    "Robot Production Deactivated": ItemClassification.useful,
    "Blast Door": ItemClassification.useful,
    "Puzzle Lift": ItemClassification.useful,
    "Armory": ItemClassification.useful,
    "Level 4 Force Bridge": ItemClassification.useful,
}

class SystemShockItem(Item):
    game = "System Shock"

def get_random_filler_item_name(world: SystemShockWorld) -> str:
    return ["Staminup", "Sight Patch", "B'serk", "Medipatch", "Reflex Patch", "Genius Patch", "Detox"][world.random.randint(0,6)]

def create_item_with_correct_classification(world: SystemShockWorld, name: str) -> SystemShockItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return SystemShockItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: SystemShockWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Radiation Shield Active"),
        world.create_item("Laser Safety Interlock Disabled"),
        world.create_item("Laser Destroyed"),
        world.create_item("Delta Grove Safety Interlock Disabled"),
        world.create_item("Alpha Grove Safety Interlock Disabled"),
        world.create_item("Beta Grove Safety Interlock Disabled"),
        world.create_item("Beta Grove Jettisoned"),
        world.create_item("Robot Charge Interrupt"),
        world.create_item("Laser Safety Interlock Access"),
        world.create_item("Reactor Auto-Destruct Activated"),
        world.create_item("Medical Armory"),
        world.create_item("Flight Bay 3"),
        world.create_item("Beta Grove Elevator"),
        world.create_item("Level 8 Access"),
        world.create_item("Edward Diego's Storage Closet"),
        world.create_item("Flight Bay Armory"),
        world.create_item("Robot Access Panel Unlocked"),
        world.create_item("Robot Production Deactivated"),
        world.create_item("Blast Door"),
        world.create_item("Puzzle Lift"),
        world.create_item("Armory"),
        world.create_item("Level 4 Force Bridge"),
    ]

    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
