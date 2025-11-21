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
        assert "Power = True, Channel = 0, Volume = 0" == str(tv)
        # Turn off
        tv.power()
        assert "Power = False, Channel = 0, Volume = 0" == str(tv)
    
    def test_mute(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()  # Volume = 2
        
        # Mute
        tv.mute()
        assert "Power = True, Channel = 0, Volume = 0" == str(tv)
        
        # Unmute - should restore volume
        tv.mute()
        assert "Power = True, Channel = 0, Volume = 2" == str(tv)
        
        # Test mute when off does nothing
        tv.power()
        tv.mute()
        assert "Power = False, Channel = 0, Volume = 2" == str(tv)
    
    def test_channel_up(self):
        tv = Television()
        tv.power()
        
        # Normal increment
        tv.channel_up()
        assert "Power = True, Channel = 1, Volume = 0" == str(tv)
        
        # Wrap around from max to min
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()  # Now at max (3)
        assert "Power = True, Channel = 0, Volume = 0" == str(tv)
        
        # Test when TV is off
        tv.power()
        tv.channel_up()
        assert "Power = False, Channel = 0, Volume = 0" == str(tv)

    def test_channel_down(self):
        tv = Television()
        tv.power()
        
        # Wrap around from min to max
        tv.channel_down()
        assert "Power = True, Channel = 3, Volume = 0" == str(tv)
        
        # Normal decrement
        tv.channel_down()
        assert "Power = True, Channel = 2, Volume = 0" == str(tv)
        
        # Test when TV is off
        tv.power()
        tv.channel_down()
        assert "Power = False, Channel = 2, Volume = 0" == str(tv)
    
    def test_volume_up(self):
        tv = Television()
        tv.power()
        
        # Normal increment
        tv.volume_up()
        assert "Power = True, Channel = 0, Volume = 1" == str(tv)
        
        # At max volume
        tv.volume_up()
        tv.volume_up()  # Should stay at 2
        assert "Power = True, Channel = 0, Volume = 2" == str(tv)
        
        # Test when off
        tv.volume_down() #Volume is now 1
        tv.power()
        tv.volume_up()
        assert "Power = False, Channel = 0, Volume = 1" == str(tv)
        
        # Test when muted - should unmute and restore volume
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()  # Volume = 2
        tv.mute()  # Muted, volume = 0
        tv.volume_up()  # Should unmute and stay at 2 (max)
        assert "Power = True, Channel = 0, Volume = 2" == str(tv)
    
    def test_volume_down(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()  # Volume = 2
        
        # Normal decrement
        tv.volume_down()
        assert "Power = True, Channel = 0, Volume = 1" == str(tv)
        
        # At min volume
        tv.volume_down()
        tv.volume_down()  # Should stay at 0
        assert "Power = True, Channel = 0, Volume = 0" == str(tv)
        
        # Test when off
        tv.power()
        tv.volume_down()
        assert "Power = False, Channel = 0, Volume = 0" == str(tv)
        
        # Test when muted - should unmute and restore volume
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.volume_up()  # Volume = 2
        tv.mute()  # Muted, volume = 0
        tv.volume_down()  # Should unmute and go to 1
        assert "Power = True, Channel = 0, Volume = 1" == str(tv)
    
    def test_str(self):
        tv = Television()
        tv.power()
        tv.channel_up()
        tv.channel_up()  # Channel = 2
        tv.volume_up()  # Volume = 1
        assert "Power = True, Channel = 2, Volume = 1" == str(tv)


