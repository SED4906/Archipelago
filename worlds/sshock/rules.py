from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import SystemShockWorld

def set_all_rules(world: SystemShockWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: SystemShockWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    pass

def set_all_location_rules(world: SystemShockWorld) -> None:
    laser_button = world.get_location("Laser Button")
    laser_safety_switch = world.get_location("Laser Safety Interlock Access Switch")
    beta_grove_jettison_switch = world.get_location("Beta Grove Jettison Switch")
    robot_production_switch = world.get_location("Robot Production Switch")
    antennas_destroyed = world.get_location("Antennas Destroyed")
    systems_authorization_code = world.get_location("Systems Authorization Code")
    systems_authorization_code123 = world.get_location("Systems Authorization Code (First 3 Digits)")
    systems_authorization_code456 = world.get_location("Systems Authorization Code (Last 3 Digits)")
    final_stretch = world.get_location("Final Stretch")

    set_rule(laser_safety_switch, lambda state: state.has_all(("Radiation Shield Active", "Laser Safety Interlock Access"), world.player))
    set_rule(laser_button, lambda state: state.has_all(("Radiation Shield Active", "Laser Safety Interlock Disabled"), world.player))
    set_rule(robot_production_switch, lambda state: state.has("Robot Access Panel Unlocked", world.player))
    set_rule(beta_grove_jettison_switch, lambda state: state.has_all(("Laser Destroyed", "Beta Grove Elevator", "Delta Grove Safety Interlock Disabled", "Alpha Grove Safety Interlock Disabled", "Beta Grove Safety Interlock Disabled"), world.player))
    set_rule(antennas_destroyed, lambda state: state.has_all(("Laser Destroyed", "Beta Grove Jettisoned"), world.player))
    set_rule(systems_authorization_code, lambda state: state.has_all(("Laser Destroyed", "Beta Grove Jettisoned", "Level 8 Access"), world.player))
    set_rule(systems_authorization_code123, lambda state: state.has_all(("Laser Destroyed", "Beta Grove Jettisoned", "Level 8 Access"), world.player))
    set_rule(systems_authorization_code456, lambda state: state.has_all(("Laser Destroyed", "Beta Grove Jettisoned", "Level 8 Access"), world.player))
    set_rule(final_stretch, lambda state: state.has_all(("Laser Destroyed", "Delta Grove Safety Interlock Disabled", "Alpha Grove Safety Interlock Disabled", "Beta Grove Safety Interlock Disabled", "Beta Grove Jettisoned", "Level 8 Access", "Reactor Auto-Destruct Activated"), world.player))


def set_completion_condition(world: APQuestWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Finale", world.player)
