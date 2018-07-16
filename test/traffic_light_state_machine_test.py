from traffic_light_fsm import TrafficLightFSM


class TestTrafficLightsStateMachine(object):
    def test_state_transitions(self):

        tl = TrafficLightFSM()
        assert tl.currentState == TrafficLightFSM.go_state

        tl.transition(TrafficLightFSM.light_change_timer_elapsed_event)
        assert tl.currentState == TrafficLightFSM.go_state

        tl.transition(TrafficLightFSM.button_pressed_event)
        assert tl.currentState == TrafficLightFSM.prepare_to_stop_state

        tl.transition(TrafficLightFSM.light_change_timer_elapsed_event)
        assert tl.currentState == TrafficLightFSM.stop_state

        tl.transition(TrafficLightFSM.button_pressed_event)
        assert tl.currentState == TrafficLightFSM.stop_state

        tl.transition(TrafficLightFSM.pedestrian_green_timer_elapsed_event)
        assert tl.currentState == TrafficLightFSM.prepare_to_start_state

        tl.transition(TrafficLightFSM.light_change_timer_elapsed_event)
        assert tl.currentState == TrafficLightFSM.go_state



