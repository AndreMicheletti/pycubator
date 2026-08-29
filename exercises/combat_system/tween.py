import arcade
import pytweening


class TweenTask:
    """Represents a single property animation or a delay wait action."""

    def __init__(
        self,
        sprite,
        property_name,
        start_val,
        end_val,
        duration,
        easing_func,
        callback=None,
    ):
        self.sprite = sprite  # The target arcade.Sprite
        self.property_name = property_name  # e.g., 'center_x', 'alpha', 'scale'
        self.start_val = start_val
        self.end_val = end_val
        self.duration = duration  # Duration in seconds
        self.easing_func = (
            easing_func  # pytweening function (e.g., pytweening.easeOutBounce)
        )
        self.callback = callback  # Action to run when this individual task finishes
        self.elapsed_time = 0.0

    def update(self, dt: float) -> bool:
        """Updates the tween. Returns True if completed."""
        self.elapsed_time += dt

        # Calculate progress normalized between 0.0 and 1.0
        progress = min(1.0, self.elapsed_time / self.duration)

        # Apply easing curve distortion
        eased_progress = self.easing_func(progress)

        # Calculate intermediate value via LERP
        current_val = arcade.math.lerp(self.start_val, self.end_val, eased_progress)

        # Apply property modification dynamically (if not a pure 'wait' task)
        if self.sprite and self.property_name:
            setattr(self.sprite, self.property_name, current_val)

        if progress >= 1.0:
            if self.callback:
                self.callback()
            return True  # Task finished
        return False


class TweenManager:
    """Static class that handles global sprite animation queues and delays."""

    _active_tweens = []

    @classmethod
    def to(
        cls,
        sprite,
        property_name: str,
        target_val: float,
        duration: float,
        easing_func=pytweening.linear,
        callback=None,
    ):
        """Animates a single sprite property instantly from its current state."""
        start_val = getattr(sprite, property_name)
        task = TweenTask(
            sprite,
            property_name,
            start_val,
            target_val,
            duration,
            easing_func,
            callback,
        )
        cls._active_tweens.append(task)

    @classmethod
    def wait(cls, duration: float, callback):
        """Waits for a set duration, then executes a callback function."""
        # Operates like a dummy tween with no property updates
        task = TweenTask(None, None, 0.0, 0.0, duration, pytweening.linear, callback)
        cls._active_tweens.append(task)

    @classmethod
    def update(cls, dt: float):
        """Must be called inside the main arcade Window's on_update() loop."""
        # Process and filter out finished tasks
        cls._active_tweens = [
            task for task in cls._active_tweens if not task.update(dt)
        ]
