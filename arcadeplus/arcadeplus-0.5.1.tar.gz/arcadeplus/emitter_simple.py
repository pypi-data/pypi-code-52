"""
Convenience functions that provide a much simpler interface to Emitters and Particles.

These trade away some flexibility in favor of simplicity to allow beginners to start using particle systems.
"""

import arcadeplus
import random
from typing import Sequence, Type
from arcadeplus.arcade_types import Point
from arcadeplus.particle import FilenameOrTexture


def make_burst_emitter(
        center_xy: Point,
        filenames_and_textures: Sequence[FilenameOrTexture],
        particle_count: int,
        particle_speed: float,
        particle_lifetime_min: float,
        particle_lifetime_max: float,
        particle_scale: float = 1.0,
        fade_particles: bool = True):
    """Returns an emitter that emits all of its particles at once"""
    particle_factory: Type[arcadeplus.LifetimeParticle] = arcadeplus.LifetimeParticle
    if fade_particles:
        particle_factory = arcadeplus.FadeParticle
    return arcadeplus.Emitter(
        center_xy=center_xy,
        emit_controller=arcadeplus.EmitBurst(particle_count),
        particle_factory=lambda emitter: particle_factory(
            filename_or_texture=random.choice(filenames_and_textures),
            change_xy=arcadeplus.rand_in_circle((0.0, 0.0), particle_speed),
            lifetime=random.uniform(particle_lifetime_min, particle_lifetime_max),
            scale=particle_scale
        )
    )


def make_interval_emitter(
        center_xy: Point,
        filenames_and_textures: Sequence[FilenameOrTexture],
        emit_interval: float,
        emit_duration: float,
        particle_speed: float,
        particle_lifetime_min: float,
        particle_lifetime_max: float,
        particle_scale: float = 1.0,
        fade_particles: bool = True):
    """Returns an emitter that emits its particles at a constant rate for a given amount of time"""
    particle_factory: Type[arcadeplus.LifetimeParticle] = arcadeplus.LifetimeParticle
    if fade_particles:
        particle_factory = arcadeplus.FadeParticle
    return arcadeplus.Emitter(
        center_xy=center_xy,
        emit_controller=arcadeplus.EmitterIntervalWithTime(emit_interval, emit_duration),
        particle_factory=lambda emitter: particle_factory(
            filename_or_texture=random.choice(filenames_and_textures),
            change_xy=arcadeplus.rand_on_circle((0.0, 0.0), particle_speed),
            lifetime=random.uniform(particle_lifetime_min, particle_lifetime_max),
            scale=particle_scale
        )
    )
