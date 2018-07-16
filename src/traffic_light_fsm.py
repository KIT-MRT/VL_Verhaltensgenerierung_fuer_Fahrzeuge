from state_machine import StateMachine, State, Event


class Go(State):
    def run(self):
        print("vehicles: grn, pedestrians: red")

    def next(self, event):
        print(event)
        if event == TrafficLightFSM.button_pressed_event:
            return TrafficLightFSM.prepare_to_stop_state
        return TrafficLightFSM.go_state


class PrepareToStop(State):
    def run(self):
        print("vehicles: yel, pedestrians: yel")

    def next(self, event):
        print(event)
        if event == TrafficLightFSM.light_change_timer_elapsed_event:
            return TrafficLightFSM.stop_state
        return TrafficLightFSM.prepare_to_stop_state


class Stop(State):
    def run(self):
        print("vehicles: red, pedestrians: grn")

    def next(self, event):
        print(event)
        if event == TrafficLightFSM.pedestrian_green_timer_elapsed_event:
            return TrafficLightFSM.prepare_to_start_state
        return TrafficLightFSM.stop_state


class PrepareToStart(State):
    def run(self):
        print("vehicles: yel, pedestrians: yel")

    def next(self, event):
        print(event)
        if event == TrafficLightFSM.light_change_timer_elapsed_event:
            return TrafficLightFSM.go_state
        return TrafficLightFSM.prepare_to_start_state


class TrafficLightFSM(StateMachine):
    go_state = Go()
    prepare_to_stop_state = PrepareToStop()
    stop_state = Stop()
    prepare_to_start_state = PrepareToStart()

    button_pressed_event = Event("button pressed")
    light_change_timer_elapsed_event = Event("light change timer elapsed")
    pedestrian_green_timer_elapsed_event = Event("pedestrian green timer elapsed")

    def __init__(self):
        # Initial state
        StateMachine.__init__(self, TrafficLightFSM.go_state)
