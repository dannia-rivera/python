from television import *

class Test:
    def setup_method(self):
        self.tele1 = Television()

    def teardown_method(self):
        assert self.tele1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        def test_power(self):
            self.tele1.power()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 0'
            self.tele1.power()
            assert self.tele1__str__() == 'Power = False, Channel = 0, Volume = 0'
            self.tele1.power()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 0'

        def test_mute(self):
            assert self.tele1.__str__() == 'Power = False, Channel = 0, Volume = 0'

            self.tele1.power()
            self.tele1.volume_up()
            self.tele1.mute()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 0'

            self.tele1.mute()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 1'

            self.tele1.power()
            self.tele1.mute()
            assert self.tele1__str__() == 'Power = False, Channel = 0, Volume = 0'

            self.tele1.mute()
            assert self.tele1__str__() == 'Power = False, Channel = 0, Volume = 0'

        def test_channel_up(self):
            self.tele1.channel_up()
            assert self.tele1__str__() == 'Power = False, Channel = 0, Volume = 0'

            self.tele1.power()
            self.tele1.channel_up()
            assert self.tele1__str__() == 'Power = True, Channel 1, Volume = 0'

            self.tele1.channel_up()
            self.tele1.channel_up()
            self.tele1.channel_up()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 0'

        def test_channel_down(self):
            self.tele1.channel_down()
            assert self.tele1__str__() == 'Power = False, Channel = 0, Volume = 0'

            self.tele1.power()
            self.tele1.channel_down()
            assert self.tele1__str__() == 'Power = True, Channel = 3, Volume = 0'

            self.tele1.channel_down()
            assert self.tele1__str__() == 'Power = True, Channel = 2, Volume = 0'

        def test_volume_up(self):
            self.tele1.volume_up()
            assert self.tele1__str__() == 'Power = False, Channel = 0, Volume = 0'

            self.tele1.power()
            self.tele1.volume_up()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 1'

            self.tele1.mute()
            self.tele1.volume_up()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 2'

            self.tele1.volume_up()
            self.tele1.volume_up()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 2'

            self.tele1.mute()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 0'

        def test_volume_down(self):
            self.tele1.volume_down()
            assert self.tele1__str__() == 'Power = False, Channel =0, Volume = 0'

            self.tele1.power()
            self.tele1.volume_up()
            self.tele1.volume_up()
            self.tele1.volume_down()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 1'

            self.tele1.mute()
            self.tele1.volume_down()
            assert self.tele1__str__() == 'Power = True, Channel = 0, Volume = 0'
