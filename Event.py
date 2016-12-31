import pygame
from pygame.locals import *


class Listener_List:
    # its own class so that different event types can have their own "handle" overhead.
    def __init__(self):
        self.callbacks = []

    def add(self, callback):
        self.callbacks.append(callback)

    def handle(self, event):
        # base behavior, overriden by other event types.
        for callback in self.callbacks:
            return callback(event)


class Event:
    def __init__(self):
        self.listeners = {}
        # leave these in instance, so they can be reassigned to new input schemes or peripherals.
        self.CLICK = MOUSEBUTTONUP
        self.KEY = KEYDOWN

    def subscribe(self, event_type, callback):
        if event_type not in self.listeners:
            self.listeners[event_type] = Listener_List()
        self.listeners[event_type].add(callback)

    def handle(self):
        # for non pygame, replace this with a call.
        events = [pygame.event.wait()] + pygame.event.get()
        for event in events:
            # for other event systems, get event type here.
            if event.type == QUIT:
                # TODO: implement:
                return GameResult.QUIT
            elif event.type in self.listeners:
                return self.listeners[event.type].handle(event)
