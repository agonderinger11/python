import pytest
from television import *

class TestTelevision:

    def test_init(self):
        tv = Television()
        assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    
    def test_power(self):
        tv = Television()
        # Turn on
        tv.power()
        assert "Power = True" in str(tv)
        # Turn off
        tv.power()
        assert "Power = False" in str(tv)
    
    def test_mute(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()  # Volume = 2
        
        # Mute
        tv.mute()
        assert "Volume = 0" in str(tv)
        
        # Unmute - should restore volume
        tv.mute()
        assert "Volume = 2" in str(tv)
        
        # Test mute when off does nothing
        tv.power()
        tv.mute()
        assert "Power = False" in str(tv)
    
    def test_channel_up(self):
        tv = Television()
        tv.power()
        
        # Normal increment
        tv.channel_up()
        assert "Channel = 1" in str(tv)
        
        # Wrap around from max to min
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()  # Now at max (3)
        assert "Channel = 0" in str(tv)
        
        # Test when TV is off
        tv.power()
        tv.channel_up()
        assert "Channel = 0" in str(tv)

    def test_channel_down(self):
        tv = Television()
        tv.power()
        
        # Wrap around from min to max
        tv.channel_down()
        assert "Channel = 3" in str(tv)
        
        # Normal decrement
        tv.channel_down()
        assert "Channel = 2" in str(tv)
        
        # Test when TV is off
        tv.power()
        current_channel = "Channel = 2"
        tv.channel_down()
        assert current_channel in str(tv)
    
    def test_volume_up(self):
        tv = Television()
        tv.power()
        
        # Normal increment
        tv.volume_up()
        assert "Volume = 1" in str(tv)
        
        # At max volume
        tv.volume_up()
        tv.volume_up()  # Should stay at 2
        assert "Volume = 2" in str(tv)
        
        # Test when off
        tv.power()
        tv.volume_up()
        assert "Volume = 2" in str(tv)
        
        # Test when muted - should unmute and restore volume
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()  # Volume = 2
        tv.mute()  # Muted, volume = 0
        tv.volume_up()  # Should unmute and stay at 2 (max)
        assert "Volume = 2" in str(tv)
    
    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()  # Volume = 2
        
        # Normal decrement
        tv.volume_down()
        assert "Volume = 1" in str(tv)
        
        # At min volume
        tv.volume_down()
        tv.volume_down()  # Should stay at 0
        assert "Volume = 0" in str(tv)
        
        # Test when off
        tv.power()
        tv.volume_down()
        assert "Volume = 0" in str(tv)
        
        # Test when muted - should unmute and restore volume
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()  # Volume = 2
        tv.mute()  # Muted, volume = 0
        tv.volume_down()  # Should unmute and go to 1
        assert "Volume = 1" in str(tv)
    
    def test_str(self):
        tv = Television()
        tv.power()
        tv.channel_up()
        tv.channel_up()  # Channel = 2
        tv.volume_up()  # Volume = 1
        expected = "Power = True, Channel = 2, Volume = 1"
        assert str(tv) == expected


